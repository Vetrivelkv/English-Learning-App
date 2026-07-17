import streamlit as st
import json
import database as db


COURSES = {
    "existing_english": {
        "title": "Existing English Class",
        "description": "Continue your current English learning path with the existing Noun, Pronoun, and Verb modules.",
        "curriculum": "data/curriculum.json",
        "questions": "data/questions.json",
        "show_challenges": True,
    },
    "udemy_scott_mendoza": {
        "title": "Udemey Scott Mendosa English Course",
        "description": "Study the Scott Mendoza Udemy course with video-based classes, subclasses, and quizzes.",
        "curriculum": "data/udemy_scott_mendoza_curriculum.json",
        "questions": "data/udemy_scott_mendoza_questions.json",
        "show_challenges": True,
    },
}


def selected_course():
    return COURSES.get(st.session_state.get("selected_course"))


def render_course_picker():
    st.title("Choose Your English Course")
    st.write("Pick the course you want to study today.")
    st.divider()

    cols = st.columns(2)
    for idx, (course_id, course) in enumerate(COURSES.items()):
        with cols[idx]:
            with st.container(border=True):
                st.subheader(course["title"])
                st.write(course["description"])
                if st.button("Open Course", key=f"course_{course_id}", use_container_width=True, type="primary"):
                    st.session_state.selected_course = course_id
                    st.rerun()


def render():
    course = selected_course()
    if not course:
        render_course_picker()
        return

    if st.button("Change Course"):
        st.session_state.selected_course = None
        st.rerun()

    st.title("Your Learning Dashboard")
    st.write(f"Welcome back, **{st.session_state.user['username']}**! Let's conquer some English concepts today.")
    st.caption(f"Current course: {course['title']}")
    st.divider()

    with open(course["curriculum"], "r", encoding="utf-8") as f:
        curriculum = json.load(f)

    challenge_data = None
    if course["show_challenges"] and course["questions"]:
        with open(course["questions"], "r", encoding="utf-8") as f:
            challenge_data = json.load(f)

    learn_prog = db.get_learning_progress(st.session_state.user["id"])
    chal_prog = db.get_progress(st.session_state.user["id"])

    l_map = {}
    for p in learn_prog:
        t = p["topic_name"]
        s = p["subtopic_id"]
        if t not in l_map:
            l_map[t] = {}
        l_map[t][s] = p

    c_map = {}
    for p in chal_prog:
        t = p["topic_name"]
        r = p["round_number"]
        if t not in c_map:
            c_map[t] = {}
        c_map[t][r] = p

    st.header("Learning Journey")
    st.write("Read the theory and pass the module quizzes to unlock the next topics.")

    for topic in curriculum["topics"]:
        t_name = topic["name"]
        with st.expander(f"{t_name} Modules", expanded=False):
            subtopics = topic["subtopics"]
            for i in range(0, len(subtopics), 3):
                cols = st.columns(3)
                for j, sub in enumerate(subtopics[i:i + 3]):
                    s_idx = i + j
                    s_id = sub["id"]

                    is_unlocked = True
                    if s_idx > 0:
                        prev_id = topic["subtopics"][s_idx - 1]["id"]
                        if not l_map.get(t_name, {}).get(prev_id, {}).get("passed", False):
                            is_unlocked = False

                    status = l_map.get(t_name, {}).get(s_id, {})
                    passed = status.get("passed", False)
                    h_score = status.get("high_score", 0)
                    question_count = len(sub.get("questions", []))

                    with cols[j]:
                        with st.container(border=True):
                            st.write(f"**{sub['title']}**")
                            if passed:
                                st.success(f"Learned ({h_score}/{question_count})")
                            elif is_unlocked:
                                st.info("Start Module")
                            else:
                                st.error("Locked")

                            if is_unlocked:
                                if st.button("Learn", key=f"learn_{s_id}", use_container_width=True, type="secondary"):
                                    st.session_state.learn_topic = t_name
                                    st.session_state.learn_subtopic = s_id
                                    st.session_state.page = "learn"
                                    st.rerun()
                            else:
                                st.button("Locked", key=f"lock_l_{s_id}", disabled=True, use_container_width=True)

    if not course["show_challenges"] or not challenge_data:
        return

    st.divider()
    st.header("Challenge Rounds")
    st.write("Test your knowledge. These are optional and independent of the learning journey.")

    for topic in challenge_data["topics"]:
        t_name = topic["name"]
        with st.expander(f"{t_name} Challenges", expanded=False):
            rounds = topic["rounds"]
            for i in range(0, len(rounds), 3):
                cols = st.columns(3)
                for j, rnd in enumerate(rounds[i:i + 3]):
                    r_num = rnd["round_number"]

                    is_unlocked = True
                    if r_num > 1:
                        if not c_map.get(t_name, {}).get(r_num - 1, {}).get("passed", False):
                            is_unlocked = False

                    status = c_map.get(t_name, {}).get(r_num, {})
                    passed = status.get("passed", False)
                    h_score = status.get("high_score", 0)
                    question_count = len(rnd.get("questions", []))

                    with cols[j]:
                        with st.container(border=True):
                            st.write(f"**Round {r_num}:** {rnd['title']}")
                            if passed:
                                st.success(f"Passed ({h_score}/{question_count})")
                            elif is_unlocked:
                                st.info("Ready")
                            else:
                                st.error("Locked")

                            if is_unlocked:
                                if st.button("Start Challenge", key=f"chal_{t_name}_{r_num}", use_container_width=True, type="primary"):
                                    st.session_state.current_topic = t_name
                                    st.session_state.current_round = r_num
                                    st.session_state.page = "quiz"
                                    st.rerun()
                            else:
                                st.button("Locked", key=f"lock_c_{t_name}_{r_num}", disabled=True, use_container_width=True)
