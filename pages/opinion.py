import streamlit as st
import pandas as pd

st.logo("logo.jpg", size="large")
st.title("시민 게시판")

if 'posts' not in st.session_state:
    st.session_state['posts'] = ["강간이나 추행이 가장 많이 일어나는 지하철/전철에도 CCTV를 확대 설치하면 좋겠어요😥"]

with st.form("new_post"):
    opinion = st.text_input("안심 서울시를 위한 시민 여러분의 의견을 자유롭게 나눠주세요.", placeholder="여기에 내용을 입력하세요.")
    submit_button = st.form_submit_button("등록")
    if submit_button:
        if opinion.strip():
            st.session_state['posts'].append(opinion)
            st.success("게시글이 등록되었습니다!")
            opinion = ""
        else:
            st.warning("내용을 다시 입력해주세요.")


st.subheader("게시판")
post_num = 0
if st.session_state['posts']:
    for idx, post in enumerate(st.session_state['posts'], start=2):
        st.write(f"-   {post}")
else:
    st.info("아직 등록된 게시글이 없습니다.")
