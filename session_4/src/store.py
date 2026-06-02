import joblib
from datetime import datetime
from pathlib import Path


# Define models folder explicitly
MODELS_FOLDER = Path(__file__).parent.parent / "models"


def store_model(model, your_name: str) -> None:
    # Ensure folder exists
    MODELS_FOLDER.mkdir(parents=True, exist_ok=True)

    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Correct filename (uses parameter properly)
    model_filename = f"class_model-{your_name}-{timestamp}.joblib"

    # Full path
    model_path = MODELS_FOLDER / model_filename

    # Save model
    joblib.dump(model, model_path)

    print(f"Model stored as: {model_path}")
