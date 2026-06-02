import pandas as pd
from pathlib import Path


def load_data(file_name: str = "Churn_Modelling_train_test.csv") -> pd.DataFrame:
    base_path = Path(__file__).parent.parent  # goes to session_4/
    file_path = base_path / "datasets" / file_name
    return pd.read_csv(file_path)