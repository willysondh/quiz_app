import streamlit as st

st.title("간단한 퀴즈 서비스")

st.header("1. 객관식 퀴즈")
q1 = st.radio(
    "왕이 넘어지면?",
    ["킹콩", "고릴라", "침팬지", "원숭이"]
)

st.header("2. 주관식 퀴즈")
q2 = st.text_input("광운대 교수님 중에서 가장 외모가 뛰어난 분은?")

if st.button("제출"):
    score = 0

    if q1 == "킹콩":
        score += 1
    if q2.strip().lower() == "박규동":
        score += 1

    st.success(f"총 {score}/2 정답입니다.")
    if score == 2:
        st.balloons()