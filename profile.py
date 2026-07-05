import streamlit as st
import database as db

def render():
    st.button("🔙 Back to Dashboard", on_click=lambda: st.session_state.update({'page': 'dashboard'}))
    st.title("👤 User Profile")
    st.markdown(f"### Hello, {st.session_state.user['username']}!")
    
    l_prog = db.get_learning_progress(st.session_state.user['id'])
    c_prog = db.get_progress(st.session_state.user['id'])
    
    st.divider()
    
    # --- LEARNING PROGRESS ---
    st.subheader("📖 Learning Journey Progress")
    if not l_prog:
        st.info("You haven't started your learning journey yet.")
    else:
        l_topics = list(set([p['topic_name'] for p in l_prog]))
        for topic in l_topics:
            with st.expander(f"📚 {topic} Learning Modules", expanded=True):
                t_data = [p for p in l_prog if p['topic_name'] == topic]
                # Try sorting by subtopic id assuming format noun_sub_1
                t_data = sorted(t_data, key=lambda x: x['subtopic_id'])
                
                table_data = []
                for p in t_data:
                    table_data.append({
                        "Module ID": p['subtopic_id'],
                        "Status": "✅ Learned" if p['passed'] else "❌ Attempting",
                        "High Score": f"{p['high_score']} / 15",
                        "Attempts": p['attempts']
                    })
                st.table(table_data)

    st.divider()
    
    # --- CHALLENGE PROGRESS ---
    st.subheader("⚔️ Challenge Rounds Progress")
    if not c_prog:
        st.info("You haven't attempted any challenge rounds yet.")
    else:
        c_topics = list(set([p['topic_name'] for p in c_prog]))
        for topic in c_topics:
            with st.expander(f"🎯 {topic} Challenge Details", expanded=True):
                t_data = [p for p in c_prog if p['topic_name'] == topic]
                t_data = sorted(t_data, key=lambda x: x['round_number'])
                
                table_data = []
                for p in t_data:
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
