import streamlit as st
import pandas as pd

from components.data_loader import load_data
from components.layout import show_sidebar
from components.plot import (
    plot_homerun_trends,
    plot_monthly_homeruns,
    show_monthly_homerun_table
)

data: pd.DataFrame = load_data("data/homerun.csv")
pivot_data: pd.DataFrame = data.pivot(index='月日', columns="year", values='count')
selected_years = show_sidebar(data)

st.title('大谷選手のホームラン数')

st.header('ホームラン数の推移')
plot_homerun_trends(data, selected_years)

st.header('月ごとのホームラン数')
all_years_monthly_data = data[data['year'].isin(selected_years)].groupby(['year', 'month'])['num'].sum().unstack(0)
plot_monthly_homeruns(all_years_monthly_data, selected_years)
show_monthly_homerun_table(all_years_monthly_data)
