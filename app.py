import streamlit as st
import auth
import dashboard
import quiz
import profile

st.set_page_config(page_title="English Learning Quiz", page_icon="📚", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'login'
if 'user' not in st.session_state:
    st.session_state.user = None

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
elif st.session_state.page == 'profile':
    if st.session_state.user:
        profile.render()
    else:
        st.session_state.page = 'login'
        st.rerun()
