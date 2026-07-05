import streamlit as st
import database as db

def render():
    st.button("🔙 Back to Dashboard", on_click=lambda: st.session_state.update({'page': 'dashboard'}))
    st.title("User Profile 👤")
    
    st.markdown(f"**Username:** {st.session_state.user['username']}")
    st.divider()
    
    st.subheader("Your Progress 📈")
    prog = db.get_progress(st.session_state.user['id'])
    
    if not prog:
        st.info("No progress yet. Start playing from the Dashboard!")
    else:
        # Get unique topics
        topics = []
        for p in prog:
            if p['topic_name'] not in topics:
                topics.append(p['topic_name'])
                
        for topic in topics:
            with st.expander(f"📚 {topic} Progress", expanded=True):
                topic_data = [p for p in prog if p['topic_name'] == topic]
                # Sort by round number
                topic_data = sorted(topic_data, key=lambda x: x['round_number'])
                
                # Format data for table
                table_data = []
                for p in topic_data:
                    table_data.append({
                        "Round": f"Round {p['round_number']}",
                        "Status": "✅ Passed" if p['passed'] else "❌ Attempting",
                        "High Score": f"{p['high_score']} / 10",
                        "Attempts": p['attempts']
                    })
                
                # Display as a table
                st.table(table_data)
                
    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Logout", type="primary", use_container_width=True):
            st.session_state.user = None
            st.session_state.page = "login"
            st.rerun()
