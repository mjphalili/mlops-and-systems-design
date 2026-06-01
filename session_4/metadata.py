MODELS_FOLDER = "session_4/models"
DATASETS_FOLDER = "session_4/datasets"
MODEL_NAME = "decisiontree-model(trained_model)"

COLUMNS_TO_DROP = ["RowNumber", "CustomerId", "Surname"]
BINARY_FEATURES = [
    "Gender"
]
ONE_HOT_ENCODE_COLUMNS = [
    "Geography"
]
DT_PARAMS = {
    "criterion": "gini",
    "max_depth": 5,
    "random_state": 42
}
