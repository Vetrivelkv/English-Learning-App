import streamlit as st
import json
import database as db

def render():
    topic_name = st.session_state.current_topic
    round_num = st.session_state.current_round
    
    st.button("🔙 Back to Dashboard", on_click=lambda: st.session_state.update({'page': 'dashboard'}))
    st.title(f"Quiz: {topic_name} - Round {round_num}")
    
    with open('data/questions.json', 'r') as f:
        data = json.load(f)
        
    topic = next(t for t in data['topics'] if t['name'] == topic_name)
    rnd = next(r for r in topic['rounds'] if r['round_number'] == round_num)
    questions = rnd['questions']
    
    with st.form("quiz_form"):
        answers = {}
        for idx, q in enumerate(questions):
            st.markdown(f"**Q{idx+1}: {q['question']}**")
            if q['type'] == 'mcq':
                ans = st.radio("Select an option:", q['options'], key=f"q_{idx}", index=None)
                answers[idx] = ans
            elif q['type'] == 'fib':
                ans = st.text_input("Your answer:", key=f"q_{idx}")
                answers[idx] = ans
            st.write("---")
            
        submitted = st.form_submit_button("Submit Answers", use_container_width=True)
        
    if submitted:
        score = 0
        feedback = []
        for idx, q in enumerate(questions):
            user_ans = answers[idx]
            is_correct = False
            
            if q['type'] == 'mcq':
                correct_ans = q['options'][q['correct_option_index']]
                if user_ans == correct_ans:
                    is_correct = True
            elif q['type'] == 'fib':
                if user_ans and user_ans.strip().lower() == q['answer'].lower():
                    is_correct = True
                    
            if is_correct:
                score += 1
                feedback.append({"idx": idx+1, "status": "✅ Correct", "expl": q['explanation']})
            else:
                correct_txt = q['options'][q['correct_option_index']] if q['type']=='mcq' else q['answer']
                feedback.append({"idx": idx+1, "status": f"❌ Wrong. (Correct answer: {correct_txt})", "expl": q['explanation']})
                
        passed = score == 10
        
        db.save_progress(st.session_state.user['id'], topic_name, round_num, passed, score)
        
        st.header("Results 📊")
        st.subheader(f"Your Score: {score}/10")
        
        if passed:
            st.success("🎉 Congratulations! You scored a perfect 10/10! The next round is now unlocked.")
            st.balloons()
        else:
            st.error("⚠️ You need 10/10 to pass. Please review your mistakes below and try again.")
            
        for fb in feedback:
            with st.expander(f"Question {fb['idx']} - {fb['status']}"):
                st.write(fb['expl'])
