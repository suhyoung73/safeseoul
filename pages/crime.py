import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.logo("logo.jpg", size="large")
st.title("5대 범죄 발생 현황")

crimedata = pd.read_csv("경찰청 서울특별시경찰청_5대범죄 발생 장소별 현황_20231231.csv", encoding="cp949")
summary = crimedata.groupby('범죄명')['발생건수'].sum().reset_index()
summary_txt = "2023년 한 해 동안 "
for _, row in summary.iterrows():
    summary_txt += f"{row['범죄명']} {row['발생건수']}건, "
summary_txt += f"총 {summary['발생건수'].sum()}건이 발생했습니다. "
summary_txt += "아래 버튼을 눌러 각 범죄가 발생한 장소를 확인해보세요."
st.write(summary_txt)


crime = crimedata['범죄명'].unique()
with st.form("input"):
    selected_crime = st.selectbox("범죄 종류를 선택하세요.", crime)
    submitted = st.form_submit_button("조회")
    if submitted:
        selected_data = crimedata.loc[(crimedata['범죄명'] == selected_crime) & crimedata['발생건수'] != 0]
        if not selected_data.empty:
            plt.figure(figsize=(12,6))
            plt.bar(selected_data['장소'], selected_data['발생건수'], color='skyblue')
            plt.xlabel('장소')
            plt.ylabel('발생건수')
            plt.title(f"{selected_crime} - 장소별 발생건수")
            plt.xticks(rotation=90)
            st.pyplot(plt)
        else:
            st.warning("선택한 범죄에 대한 데이터가 없습니다.")
