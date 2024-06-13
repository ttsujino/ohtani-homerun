import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data/homerun.csv")

data['date'] = pd.to_datetime(data['date'])
data['月日'] = data['date'].dt.strftime('%m-%d')

st.title('大谷のホームラン数の推移')

selected_all_years = st.multiselect('年度を選択してください', sorted(data['date'].dt.year.unique()))

data['year'] = data['date'].dt.year
pivot_data = data.pivot(index='月日', columns="year", values='count')

if selected_all_years:
    year_data = pivot_data[selected_all_years]
    st.line_chart(year_data)
else:
    st.write('何も選択されていません。')