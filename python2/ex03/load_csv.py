import os
import pandas as pd


def validate_path(path: str) -> None:
    """Validate that input parameters for load are valid."""
    if type(path) is not str:
        raise TypeError("Path must be a string.")
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    if not os.path.isfile(path):
        raise IsADirectoryError(f"Path is a directory, not a file: {path}")
    if not path.lower().endswith(".csv"):
        raise ValueError("File format must be CSV.")


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV dataset and return its DataFrame."""
    try:
        validate_path(path)

        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
