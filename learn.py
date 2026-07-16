import streamlit as st
import json
import database as db


COURSE_CURRICULUM = {
    "existing_english": "data/curriculum.json",
    "udemy_scott_mendoza": "data/udemy_scott_mendoza_curriculum.json",
}


def render():
    topic_name = st.session_state.get("learn_topic", "")
    subtopic_id = st.session_state.get("learn_subtopic", "")

    st.button("Back to Dashboard", on_click=lambda: st.session_state.update({"page": "dashboard"}))

    if not topic_name or not subtopic_id:
        st.error("No subtopic selected.")
        return

    curriculum_path = COURSE_CURRICULUM.get(st.session_state.get("selected_course"), "data/curriculum.json")
    with open(curriculum_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    topic = next((t for t in data["topics"] if t["name"] == topic_name), None)
    if not topic:
        st.error("Selected topic was not found.")
        return

    subtopic = next((s for s in topic["subtopics"] if s["id"] == subtopic_id), None)
    if not subtopic:
        st.error("Selected subtopic was not found.")
        return

    st.title(subtopic["title"])

    if "image" in subtopic and subtopic["image"]:
        st.image(subtopic["image"], use_column_width=True)

    with st.container(border=True):
        st.markdown(subtopic["content"])

    st.divider()
    st.subheader("Subtopic Quiz")

    questions = subtopic["questions"]
    required_score = len(questions)
    st.write(f"You must score a perfect {required_score}/{required_score} to pass this learning module.")

    with st.form("learn_quiz_form"):
        answers = {}
        for idx, q in enumerate(questions):
            st.markdown(f"**Q{idx + 1}: {q['question']}**")
            if q["type"] == "mcq":
                ans = st.radio("Select an option:", q["options"], key=f"q_{idx}", index=None)
                answers[idx] = ans
            elif q["type"] == "fill":
                ans = st.radio("Select the correct word to fill the blank:", q["options"], key=f"q_{idx}", index=None)
                answers[idx] = ans
            st.write("---")

        submitted = st.form_submit_button("Submit Answers", use_container_width=True, type="primary")

    if submitted:
        score = 0
        feedback = []
        for idx, q in enumerate(questions):
            user_ans = answers[idx]
            correct_index = q.get("correct", q.get("correct_option_index"))
            correct_ans = q["options"][correct_index]

            if user_ans == correct_ans:
                score += 1
                feedback.append({"idx": idx + 1, "status": "Correct", "expl": q["explanation"]})
            else:
                feedback.append({"idx": idx + 1, "status": f"Wrong. Correct: {correct_ans}", "expl": q["explanation"]})

        passed = score == required_score

        db.save_learning_progress(st.session_state.user["id"], topic_name, subtopic_id, passed, score)

        st.header("Results")
        st.subheader(f"Your Score: {score}/{required_score}")

        if passed:
            st.success(f"Outstanding! You scored a perfect {required_score}/{required_score}. The next subtopic is now unlocked.")
            st.balloons()
        else:
            st.error(f"You need {required_score}/{required_score} to pass this module. Review your mistakes below and try again.")

        for fb in feedback:
            with st.expander(f"Question {fb['idx']} - {fb['status']}"):
                st.write(fb["expl"])
