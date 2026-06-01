from src.source import load_data
from src.transform import Transformer, balance_dataset
from src.train import train_model
from src.store import store_model


def main():
    # 1. Load data
    df = load_data(file_name="Churn_Modelling_train_test.csv")

    # 2. Balance dataset
    df = balance_dataset(df)

    # 3. Transform data
    df = Transformer().transform(df)

    # 4. Train model
    model = train_model(df=df, target_column="Exited")

    # 5. Store model
    store_model(model=model, your_name="mjphalili")


if __name__ == "__main__":
    main()