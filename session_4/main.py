from Class_Notes.src.load import load_data
from Class_Notes.src.transform import Transformer, balance_dataset
from Class_Notes.src.train import train_model
from Class_Notes.src.store import store_model
from metadata import MODEL_NAME


def main():
    df = load_data(file_name="datasets/bank-full_train_test.csv")
    df = balance_dataset(df)
    df = Transformer().transform(df)
    lr_model = train_model(df=df, target_column="y")
    store_model(model=lr_model, model_name=MODEL_NAME)


if __name__ == "__main__":
    main()