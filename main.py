import streamlit as st
import pandas as pd

st.logo("logo.jpg", size="large", )
st.title("안심 서울시")

st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("##### 서울시 안심이 앱")
    st.image("ansimi.jpg")
    st.write("폰 위치정보와 서울시 CCTV를 통해 시민들에게 안전한 귀가길을 제공하기 위해 서울시에서 제공하는 앱입니다.")
    st.page_link("https://play.google.com/store/apps/details?id=kr.go.seoul.ansimi.woman&hl=ko", label="Playstore 앱 다운로드", icon="📥")
    st.page_link("https://apps.apple.com/kr/app/%EC%84%9C%EC%9A%B8%EC%8B%9C-%EC%95%88%EC%8B%AC%EC%9D%B4/id1204100862", label="Appstore 앱 다운로드", icon="📥")

with col2:
    st.markdown("##### 우리 동네 CCTV 현황")
    st.image("cctv.jpg")
    st.write("우리 동네에는 방법용 CCTV가 어디에 구석구석 설치되어 있는지 한 눈에 확인해보세요.")
    st.page_link("pages\cctv.py", label="CCTV 위치 보러가기", icon="📹")

with col3:
    st.markdown("##### 5대 범죄 발생 현황")
    st.image("crime.jpg")
    st.write("2023년에 일어난 5대 범죄(살인, 강도, 강간 및 추행, 절도, 폭력) 발생 현황을 종류별, 장소별로 확인해보세요.")
    st.write()
    st.page_link("pages\crime.py", label="5대 범죄 통계 보러가기", icon="🚨")
    
st.divider()
st.markdown("##### 시민 게시판")
st.page_link("pages\opinion.py", label="안심 서울시를 위한 시민 여러분의 의견을 자유롭게 나눠주세요.", icon="🙌")
