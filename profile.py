import json

import streamlit as st
import database as db
import session_manager


COURSES = {
    "existing_english": {
        "title": "Existing English Class",
        "curriculum": "data/curriculum.json",
        "questions": "data/questions.json",
        "show_challenges": True,
    },
    "udemy_scott_mendoza": {
        "title": "Udemey Scott Mendosa English Course",
        "curriculum": "data/udemy_scott_mendoza_curriculum.json",
        "questions": "data/udemy_scott_mendoza_questions.json",
        "show_challenges": True,
    },
}


def _selected_course():
    return COURSES.get(st.session_state.get("selected_course"))


def _topic_names(path: str, child_key: str):
    if not path:
        return set()
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {topic["name"] for topic in data["topics"] if child_key in topic}


def _learning_question_counts(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {
        subtopic["id"]: len(subtopic.get("questions", []))
        for topic in data["topics"]
        for subtopic in topic.get("subtopics", [])
    }


def _learning_table(progress_rows, question_counts):
    return [
        {
            "Module ID": row["subtopic_id"],
            "Status": "Learned" if row["passed"] else "Attempting",
            "High Score": f"{row['high_score']} / {question_counts.get(row['subtopic_id'], 15)}",
            "Attempts": row["attempts"],
        }
        for row in progress_rows
    ]


def _challenge_table(progress_rows):
    return [
        {
            "Round": f"Round {row['round_number']}",
            "Status": "Passed" if row["passed"] else "Attempting",
            "High Score": f"{row['high_score']} / 10",
            "Attempts": row["attempts"],
        }
        for row in progress_rows
    ]


def render():
    st.button("Back to Dashboard", on_click=lambda: st.session_state.update({"page": "dashboard"}))
    st.title("User Profile")
    st.markdown(f"### Hello, {st.session_state.user['username']}!")

    course = _selected_course()
    if not course:
        st.info("Choose a course from the dashboard to see course-specific progress.")
        return

    st.caption(f"Showing progress for: {course['title']}")

    learning_topics = _topic_names(course["curriculum"], "subtopics")
    learning_question_counts = _learning_question_counts(course["curriculum"])
    challenge_topics = _topic_names(course["questions"], "rounds") if course["show_challenges"] else set()

    l_prog = [
        row
        for row in db.get_learning_progress(st.session_state.user["id"])
        if row["topic_name"] in learning_topics
    ]
    c_prog = [
        row
        for row in db.get_progress(st.session_state.user["id"])
        if row["topic_name"] in challenge_topics
    ]

    st.divider()
    st.subheader("Learning Journey Progress")
    if not l_prog:
        st.info("You haven't started this course's learning journey yet.")
    else:
        for topic in sorted({row["topic_name"] for row in l_prog}):
            with st.expander(f"{topic} Learning Modules", expanded=False):
                topic_rows = sorted(
                    [row for row in l_prog if row["topic_name"] == topic],
                    key=lambda row: row["subtopic_id"],
                )
                st.table(_learning_table(topic_rows, learning_question_counts))

    st.divider()
    st.subheader("Challenge Rounds Progress")
    if not course["show_challenges"]:
        st.info("This course uses subclass quizzes only, so there are no separate challenge rounds.")
    elif not c_prog:
        st.info("You haven't attempted this course's challenge rounds yet.")
    else:
        for topic in sorted({row["topic_name"] for row in c_prog}):
            with st.expander(f"{topic} Challenge Details", expanded=False):
                topic_rows = sorted(
                    [row for row in c_prog if row["topic_name"] == topic],
                    key=lambda row: row["round_number"],
                )
                st.table(_challenge_table(topic_rows))

    st.divider()

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Logout", type="primary", use_container_width=True):
            session_manager.end_session()
            st.rerun()
