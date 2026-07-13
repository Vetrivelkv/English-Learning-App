import streamlit as st

st.set_page_config(page_title="English Learning Quiz", page_icon="📚", layout="wide")

import auth
import dashboard
import quiz
import learn
import profile
import session_manager

if 'page' not in st.session_state:
    st.session_state.page = 'login'
if 'user' not in st.session_state:
    st.session_state.user = None
if 'selected_course' not in st.session_state:
    st.session_state.selected_course = None
if 'session_token' not in st.session_state:
    st.session_state.session_token = None
if 'session_expired' not in st.session_state:
    st.session_state.session_expired = False

if st.session_state.user:
    session_manager.restore_or_refresh_session()
elif session_manager.restore_or_refresh_session():
    if st.session_state.page == 'login':
        st.session_state.page = 'dashboard'
elif st.session_state.page != 'login':
    if not session_manager.restore_or_refresh_session():
        st.session_state.page = 'login'

session_manager.render_expired_dialog()

# Top bar for user profile
if st.session_state.user:
    col1, col2 = st.columns([11, 1])
    with col2:
        if st.session_state.page != 'profile':
            if st.button("👤 Profile", help="User Profile", use_container_width=True):
                st.session_state.page = 'profile'
                st.rerun()

# Routing
if st.session_state.page == 'login':
    auth.render()
elif st.session_state.page == 'dashboard':
    if st.session_state.user:
        dashboard.render()
    else:
        st.session_state.page = 'login'
        st.rerun()
elif st.session_state.page == 'quiz':
    if st.session_state.user:
        quiz.render()
    else:
        st.session_state.page = 'login'
        st.rerun()
elif st.session_state.page == 'learn':
    if st.session_state.user:
        learn.render()
    else:
        st.session_state.page = 'login'
        st.rerun()
elif st.session_state.page == 'profile':
    if st.session_state.user:
        profile.render()
    else:
        st.session_state.page = 'login'
        st.rerun()
