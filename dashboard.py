import streamlit as st
import json
import database as db

def render():
    st.title("🚀 Your Learning Dashboard")
    st.write(f"Welcome back, **{st.session_state.user['username']}**! Let's conquer some English concepts today.")
    st.divider()
    
    # --- LOAD DATA ---
    with open('data/curriculum.json', 'r', encoding='utf-8') as f:
        curriculum = json.load(f)
        
    with open('data/questions.json', 'r', encoding='utf-8') as f:
        challenge_data = json.load(f)
        
    learn_prog = db.get_learning_progress(st.session_state.user['id'])
    chal_prog = db.get_progress(st.session_state.user['id'])
    
    # Maps for easy lookup
    l_map = {}
    for p in learn_prog:
        t = p['topic_name']
        s = p['subtopic_id']
        if t not in l_map: l_map[t] = {}
        l_map[t][s] = p
        
    c_map = {}
    for p in chal_prog:
        t = p['topic_name']
        r = p['round_number']
        if t not in c_map: c_map[t] = {}
        c_map[t][r] = p

    # --- LEARNING JOURNEY ---
    st.header("📖 Learning Journey")
    st.write("Read the theory and pass the module quizzes to unlock the next topics.")
    
    for t_idx, topic in enumerate(curriculum['topics']):
        t_name = topic['name']
        st.subheader(f"📚 {t_name} Modules")
        
        # Display in rows of 3 for better UI responsiveness
        subtopics = topic['subtopics']
        for i in range(0, len(subtopics), 3):
            cols = st.columns(3)
            for j, sub in enumerate(subtopics[i:i+3]):
                s_idx = i + j
                s_id = sub['id']
                
                # Check if unlocked (must pass previous subtopic)
                is_unlocked = True
                if s_idx > 0:
                    prev_id = topic['subtopics'][s_idx - 1]['id']
                    if not l_map.get(t_name, {}).get(prev_id, {}).get('passed', False):
                        is_unlocked = False
                        
                status = l_map.get(t_name, {}).get(s_id, {})
                passed = status.get('passed', False)
                h_score = status.get('high_score', 0)
                
                with cols[j]:
                    with st.container(border=True):
                        st.write(f"**{sub['title']}**")
                        if passed:
                            st.success(f"✅ Learned ({h_score}/15)")
                        elif is_unlocked:
                            st.info(f"▶️ Start Module")
                        else:
                            st.error("🔒 Locked")
                            
                        st.write("")
                        if is_unlocked:
                            if st.button("Learn", key=f"learn_{s_id}", use_container_width=True, type="secondary"):
                                st.session_state.learn_topic = t_name
                                st.session_state.learn_subtopic = s_id
                                st.session_state.page = "learn"
                                st.rerun()
                        else:
                            st.button("Locked", key=f"lock_l_{s_id}", disabled=True, use_container_width=True)
                        
    st.divider()
    
    # --- CHALLENGE ROUNDS ---
    st.header("⚔️ Challenge Rounds")
    st.write("Test your knowledge. These are completely optional and independent of the learning journey.")
    
    for t_idx, topic in enumerate(challenge_data['topics']):
        t_name = topic['name']
        st.subheader(f"🎯 {t_name} Challenges")
        
        rounds = topic['rounds']
        for i in range(0, len(rounds), 3):
            cols = st.columns(3)
            for j, rnd in enumerate(rounds[i:i+3]):
                r_idx = i + j
                r_num = rnd['round_number']
                
                # Unlocked if previous challenge round passed
                is_unlocked = True
                if r_num > 1:
                    if not c_map.get(t_name, {}).get(r_num - 1, {}).get('passed', False):
                        is_unlocked = False
                        
                status = c_map.get(t_name, {}).get(r_num, {})
                passed = status.get('passed', False)
                h_score = status.get('high_score', 0)
                
                with cols[j]:
                    with st.container(border=True):
                        st.write(f"**Round {r_num}:** {rnd['title']}")
                        if passed:
                            st.success(f"✅ Passed ({h_score}/10)")
                        elif is_unlocked:
                            st.info(f"▶️ Ready")
                        else:
                            st.error("🔒 Locked")
                            
                        st.write("")
                        if is_unlocked:
                            if st.button("Start Challenge", key=f"chal_{t_name}_{r_num}", use_container_width=True, type="primary"):
                                st.session_state.current_topic = t_name
                                st.session_state.current_round = r_num
                                st.session_state.page = "quiz"
                                st.rerun()
                        else:
                            st.button("Locked", key=f"lock_c_{t_name}_{r_num}", disabled=True, use_container_width=True)
                        
    st.divider()
