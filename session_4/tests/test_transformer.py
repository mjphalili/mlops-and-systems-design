from src.transform import Transformer
import pandas as pd


def create_test_df():
    return pd.DataFrame(
        {
            "RowNumber": [1],
            "CustomerId": [123456],
            "Surname": ["Smith"],
            "CreditScore": [600],
            "Geography": ["France"],
            "Gender": ["Male"],
            "Age": [40],
            "Tenure": [5],
            "Balance": [1000],
            "NumOfProducts": [2],
            "HasCrCard": [1],
            "IsActiveMember": [1],
            "EstimatedSalary": [50000],
            "Exited": [0],
        }
    )


def test_transform_returns_dataframe():

    df = create_test_df()

    transformed_df = Transformer().transform(df)

    assert isinstance(transformed_df, pd.DataFrame)


def test_transform_has_no_nulls():

    df = create_test_df()

    transformed_df = Transformer().transform(df)

    assert transformed_df.isnull().sum().sum() == 0


def test_target_column_exists():

    df = create_test_df()

    transformed_df = Transformer().transform(df)

    assert "Exited" in transformed_df.columns