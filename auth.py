import streamlit as st
import database as db

def render():
    st.title("English Quiz Application 📚")
    
    if not db.is_db_connected():
        st.error("🚨 Supabase is not configured! Please follow the instructions to set up your database.")
        st.stop()
        
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.subheader("Login to your account")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login", use_container_width=True):
            if username and password:
                success, result = db.login_user(username, password)
                if success:
                    st.session_state.user = result
                    st.session_state.page = "dashboard"
                    st.rerun()
                else:
                    st.error(result)
            else:
                st.warning("Please fill in both fields.")
                
    with tab2:
        st.subheader("Create a new account")
        new_username = st.text_input("Username", key="reg_username")
        new_password = st.text_input("Password", type="password", key="reg_password")
        if st.button("Register", use_container_width=True):
            if new_username and new_password:
                success, result = db.register_user(new_username, new_password)
                if success:
                    st.success("Registration successful! You can now login.")
                else:
                    st.error(result)
            else:
                st.warning("Please fill in both fields.")
