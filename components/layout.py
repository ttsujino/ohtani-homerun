import streamlit as st


def show_sidebar(data):
    """Show sidebar to select years

    Args:
        data (pd.DataFrame): data

    Returns:
        list: selected years
    """
    years = sorted(data['year'].unique())
    selected_years = st.sidebar.multiselect('表示する年を選択してください', years, default=years)
    return selected_years or sorted(data['date'].dt.year.unique())
