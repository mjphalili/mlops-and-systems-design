import pandas as pd


def load_data(file_name: str = "Churn_Modelling_train_test.csv") -> pd.DataFrame:
    return pd.read_csv(f"session_4/datasets/{file_name}")