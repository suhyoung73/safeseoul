import streamlit as st
import pandas as pd
import random
from streamlit_folium import st_folium
import folium

st.logo("logo.jpg", size="large")
st.title("우리 동네 CCTV 현황")

cctvdata = pd.read_csv("서울시 안심이 CCTV 연계 현황.csv", encoding="cp949")
cctvdata = cctvdata.copy().fillna(0)
cctvdata = cctvdata.loc[:, ['자치구', '위도', '경도']]
region = cctvdata['자치구'].unique()
def generate_color_map(region):
    return {r: [random.randint(0, 255) for _ in range(3)] for r in region}
color = generate_color_map(region)
cctvdata.loc[:, 'color'] = cctvdata.copy().loc[:, '자치구'].map(color)
st.map(cctvdata, latitude='위도', longitude='경도', color="color")

with st.form("input"):
    selected_region = st.multiselect("우리 동네(자치구)를 선택하세요.", region)
    submitted = st.form_submit_button("조회")
    if submitted:
        selected_data = cctvdata.loc[cctvdata['자치구'] == selected_region[0]]
        st.map(selected_data, latitude='위도', longitude='경도')
        print(selected_data)
        m = folium.Map(location=selected_data.iloc[0, 1:3], zoom_start=15, width="800")
        for s in range(1, len(selected_data)):
            folium.Marker(
                selected_data.iloc[s, 1:3],
                icon=folium.Icon(color='blue',icon='star')
            ).add_to(m)
        st_data = st_folium(m)