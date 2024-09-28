import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_homerun_trends(data: pd.DataFrame, selected_years: list):
    """Plot homerun trends

    Args:
        data (pd.DataFrame): data
        selected_years (list): List of selected years
    """
    pivot_data = data.pivot(index='月日', columns="year", values='count')
    year_data = pivot_data[selected_years]
    st.line_chart(year_data)


def plot_monthly_homeruns(data: pd.DataFrame, selected_years: list):
    """Plot monthly homeruns

    Args:
        data (pd.DataFrame): data
        selected_years (list): List of selected years
    """
    fig, ax = plt.subplots()
    x = np.arange(len(data.index))
    width = 0.1

    for i, year in enumerate(sorted(selected_years)):
        ax.bar(x + i*width, data[year], width=width, label=str(year))

    ax.set_xticks(x + width * len(selected_years) / 2 - width / 2)
    ax.set_xticklabels(data.index)
    ax.set_xlabel('Month')
    ax.set_ylabel('Num of Homerun')
    ax.set_title('Monthly Num of Homerun')
    ax.legend(title='Year', loc='upper right')
    st.pyplot(fig)


def show_monthly_homerun_table(data: pd.DataFrame):
    """Show num of monthly homerun table

    Args:
        data (pd.DataFrame): data
    """
    st.dataframe(data.T.style.format("{:.0f}")
                 .applymap(lambda x: 'background-color: lightblue' if x >= 10 else ('background-color: lightpink' if x <= 3 else ''), subset=data.T.columns)
                 .set_caption("月ごとのホームラン数")
    )