import streamlit as st
import database as db

def render():
    st.button("🔙 Back to Dashboard", on_click=lambda: st.session_state.update({'page': 'dashboard'}))
    st.title("👤 User Profile")
    st.markdown(f"### Hello, {st.session_state.user['username']}!")
    
    prog = db.get_progress(st.session_state.user['id'])
    
    st.divider()
    st.subheader("📊 Overall Performance")
    
    if not prog:
        st.info("No progress yet. Start playing from the Dashboard!")
    else:
        total_rounds_attempted = len(prog)
        total_rounds_passed = sum(1 for p in prog if p['passed'])
        total_attempts = sum(p['attempts'] for p in prog)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Rounds Attempted", total_rounds_attempted)
        col2.metric("Rounds Passed", total_rounds_passed)
        col3.metric("Total Quiz Attempts", total_attempts)
        
        st.divider()
        st.subheader("📚 Topic Breakdown")
        
        # Get unique topics
        topics = []
        for p in prog:
            if p['topic_name'] not in topics:
                topics.append(p['topic_name'])
                
        for topic in topics:
            with st.expander(f"📖 {topic} Progress Details", expanded=True):
                topic_data = [p for p in prog if p['topic_name'] == topic]
                topic_data = sorted(topic_data, key=lambda x: x['round_number'])
                
                table_data = []
                for p in topic_data:
                    table_data.append({
                        "Round": f"Round {p['round_number']}",
                        "Status": "✅ Passed" if p['passed'] else "❌ Attempting",
                        "High Score": f"{p['high_score']} / 10",
                        "Attempts": p['attempts']
                    })
                
                st.table(table_data)
                
    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Logout", type="primary", use_container_width=True):
            st.session_state.user = None
            st.session_state.page = "login"
            st.rerun()
