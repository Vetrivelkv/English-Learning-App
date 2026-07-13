import base64
import hashlib
import hmac
import json
import secrets
import time
from datetime import datetime, timedelta, timezone

import extra_streamlit_components as stx
import streamlit as st


SESSION_SECONDS = 2 * 60 * 60
COOKIE_NAME = "english_quiz_session"
OLD_SESSION_QUERY_PARAM = "session_token"
COOKIE_MANAGER_STATE_KEY = "_english_quiz_cookie_manager"


def _cookie_manager():
    if COOKIE_MANAGER_STATE_KEY not in st.session_state:
        st.session_state[COOKIE_MANAGER_STATE_KEY] = stx.CookieManager(key="english_quiz_cookie_init")
    return st.session_state[COOKIE_MANAGER_STATE_KEY]


def _component_key(action: str) -> str:
    counter_key = f"_english_quiz_cookie_{action}_counter"
    st.session_state[counter_key] = st.session_state.get(counter_key, 0) + 1
    return f"english_quiz_cookie_{action}_{st.session_state[counter_key]}"


def _b64_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _b64_decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode((data + padding).encode("ascii"))


def _session_secret() -> str:
    try:
        return st.secrets.get("SESSION_SECRET", st.secrets.get("SUPABASE_KEY", "local-session-secret"))
    except Exception:
        return "local-session-secret"


def _sign(message: str) -> str:
    digest = hmac.new(_session_secret().encode("utf-8"), message.encode("ascii"), hashlib.sha256).digest()
    return _b64_encode(digest)


def _make_token(user: dict) -> str:
    now = int(time.time())
    payload = {
        "sub": str(user["id"]),
        "username": user["username"],
        "iat": now,
        "exp": now + SESSION_SECONDS,
        "nonce": secrets.token_urlsafe(12),
    }
    header = {"alg": "HS256", "typ": "JWT"}
    header_part = _b64_encode(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    payload_part = _b64_encode(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    signing_input = f"{header_part}.{payload_part}"
    return f"{signing_input}.{_sign(signing_input)}"


def _cookie_expires_at():
    return datetime.now(timezone.utc) + timedelta(seconds=SESSION_SECONDS)


def _read_cookie_token():
    try:
        return _cookie_manager().get(COOKIE_NAME)
    except Exception:
        return None


def _write_cookie_token(token: str) -> None:
    _cookie_manager().set(COOKIE_NAME, token, key=_component_key("set"), expires_at=_cookie_expires_at())


def _clear_cookie_token() -> None:
    try:
        _cookie_manager().delete(COOKIE_NAME, key=_component_key("delete"))
    except Exception:
        pass


def _remove_legacy_url_token() -> None:
    if OLD_SESSION_QUERY_PARAM in st.query_params:
        del st.query_params[OLD_SESSION_QUERY_PARAM]


def _validate_token(token: str):
    try:
        header_part, payload_part, signature = token.split(".")
    except ValueError:
        return None

    signing_input = f"{header_part}.{payload_part}"
    if not hmac.compare_digest(signature, _sign(signing_input)):
        return None

    try:
        payload = json.loads(_b64_decode(payload_part))
    except (ValueError, json.JSONDecodeError):
        return None

    if int(payload.get("exp", 0)) <= int(time.time()):
        return None

    return payload


def start_session(user: dict) -> None:
    _remove_legacy_url_token()
    safe_user = {"id": user["id"], "username": user["username"]}
    token = _make_token(safe_user)
    st.session_state.user = safe_user
    st.session_state.session_token = token
    st.session_state.session_expired = False
    _write_cookie_token(token)


def end_session(expired: bool = False) -> None:
    _remove_legacy_url_token()
    st.session_state.user = None
    st.session_state.selected_course = None
    st.session_state.session_token = None
    st.session_state.page = "login"
    st.session_state.session_expired = expired
    _clear_cookie_token()


def restore_or_refresh_session() -> bool:
    _remove_legacy_url_token()
    token = st.session_state.get("session_token") or _read_cookie_token()
    if not token:
        return False

    payload = _validate_token(token)
    if not payload:
        end_session(expired=True)
        return False

    safe_user = {"id": payload["sub"], "username": payload["username"]}
    refreshed_token = _make_token(safe_user)
    st.session_state.user = safe_user
    st.session_state.session_token = refreshed_token
    st.session_state.session_expired = False
    _write_cookie_token(refreshed_token)
    return True


def render_expired_dialog() -> None:
    if not st.session_state.get("session_expired"):
        return

    def acknowledge():
        st.session_state.session_expired = False
        st.session_state.page = "login"
        st.rerun()

    if hasattr(st, "dialog"):
        @st.dialog("Session ended")
        def _dialog():
            st.write("Session ended. Click OK to begin a new session.")
            if st.button("OK", type="primary", use_container_width=True):
                acknowledge()

        _dialog()
    else:
        st.warning("Session ended. Click OK to begin a new session.")
        if st.button("OK", type="primary"):
            acknowledge()
