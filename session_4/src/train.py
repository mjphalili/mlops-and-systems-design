import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from metadata import DT_PARAMS


def train_model(df: pd.DataFrame, target_column: str) -> DecisionTreeClassifier:

    # Split features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Initialize model
    model = DecisionTreeClassifier(**DT_PARAMS)

    # Train
    model.fit(X_train, y_train)

    return model