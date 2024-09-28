import pandas as pd


def load_data(file_path):
    """Load data from csv file and add some columns

    Args:
        file_path (str): path to csv file

    Returns:
        pd.DataFrame: data with some columns added
    """
    data = pd.read_csv(file_path)
    data['date'] = pd.to_datetime(data['date'])
    data['月日'] = data['date'].dt.strftime('%m-%d')
    data['year'] = data['date'].dt.year
    data['count'] = data.groupby('year')["num"].cumsum()
    data['month'] = data['date'].dt.month
    return data