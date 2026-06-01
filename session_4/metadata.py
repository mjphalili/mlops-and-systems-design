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
MODEL_PARAMS = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "multi_class": "auto",
    "random_state": 8888,
}
