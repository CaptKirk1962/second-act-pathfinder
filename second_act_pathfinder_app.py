import streamlit as st
import json
from collections import Counter

# Load questions
with open("archetype_quiz_questions.json", "r") as f:
    questions = json.load(f)

st.set_page_config(page_title="Second Act Pathfinder", layout="centered")
st.title("🧭 Second Act Pathfinder")
st.subheader("Discover your Life Minus Work Archetype")

st.markdown("Answer the questions below to reveal your second act identity — and get your personalised lifestyle plan.")

if "responses" not in st.session_state:
    st.session_state.responses = []
if "page" not in st.session_state:
    st.session_state.page = 0

def reset_quiz():
    st.session_state.responses = []
    st.session_state.page = 0

if st.session_state.page < len(questions):
    q = questions[st.session_state.page]
    st.markdown(f"**Q{st.session_state.page + 1}: {q['question']}**")
    if f"answered_{st.session_state.page}" not in st.session_state:
        for archetype, answer in q["options"].items():
            if st.button(answer, key=f"{st.session_state.page}-{archetype}"):
                st.session_state.responses.append(archetype)
                st.session_state[f"answered_{st.session_state.page}"] = True
                st.session_state.page += 1
                st.rerun()
else:
    result = Counter(st.session_state.responses).most_common(1)[0][0]
    st.success(f"🎉 You're a **{result}**!")

    st.markdown(f"📥 Download your {result} Lifestyle Plan (coming soon)")

    st.markdown("---")
    st.button("🔄 Restart Quiz", on_click=reset_quiz)
