import streamlit as st
import json
import database as db

def render():
    st.title("🚀 Your Learning Dashboard")
    st.write(f"Welcome back, **{st.session_state.user['username']}**! Let's conquer some English concepts today.")
    st.divider()
    
    with open('data/questions.json', 'r') as f:
        data = json.load(f)
        
    topics = data['topics']
    progress_data = db.get_progress(st.session_state.user['id'])
    
    prog_map = {}
    for p in progress_data:
        t = p['topic_name']
        r = p['round_number']
        if t not in prog_map:
            prog_map[t] = {}
        prog_map[t][r] = p
        
    for i, topic in enumerate(topics):
        topic_name = topic['name']
        rounds = topic['rounds']
        
        topic_unlocked = True
        if i > 0:
            prev_topic = topics[i-1]
            prev_name = prev_topic['name']
            for pr in prev_topic['rounds']:
                pr_num = pr['round_number']
                if not prog_map.get(prev_name, {}).get(pr_num, {}).get('passed', False):
                    topic_unlocked = False
                    break
        
        st.header(f"📚 Topic: {topic_name}")
        
        if not topic_unlocked:
            st.warning(f"🔒 Complete the previous topic to unlock **{topic_name}**.")
            st.divider()
            continue
            
        # Create a grid for rounds using columns
        cols = st.columns(3)
        
        for idx, rnd in enumerate(rounds):
            r_num = rnd['round_number']
            title = rnd['title']
            
            round_unlocked = True
            if r_num > 1:
                if not prog_map.get(topic_name, {}).get(r_num - 1, {}).get('passed', False):
                    round_unlocked = False
                    
            status = prog_map.get(topic_name, {}).get(r_num, {})
            passed = status.get('passed', False)
            high_score = status.get('high_score', 0)
            
            with cols[idx % 3]:
                # Wrap each round in a styled container
                with st.container(border=True):
                    st.subheader(f"Round {r_num}")
                    st.write(f"**{title}**")
                    
                    if passed:
                        st.success(f"✅ Passed ({high_score}/10)")
                    elif round_unlocked:
                        st.info(f"▶️ Ready ({high_score}/10)")
                    else:
                        st.error("🔒 Locked")
                        
                    st.write("") # Spacer
                    if round_unlocked:
                        if st.button("Start Quiz", key=f"btn_{topic_name}_{r_num}", use_container_width=True, type="primary"):
                            st.session_state.current_topic = topic_name
                            st.session_state.current_round = r_num
                            st.session_state.page = "quiz"
                            st.rerun()
                    else:
                        st.button("Locked", key=f"lock_{topic_name}_{r_num}", disabled=True, use_container_width=True)
        
        st.divider()
