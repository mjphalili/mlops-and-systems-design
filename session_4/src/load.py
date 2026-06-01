import pandas as pd
from metadata import DATASETS_FOLDER


def load_data(file_name: str = "Churn_Modelling_train_test.csv") -> pd.DataFrame:
    return pd.read_csv(f"{DATASETS_FOLDER}/{file_name}")
