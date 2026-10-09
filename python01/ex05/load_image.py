import os
from PIL import Image
import numpy as np


def validate_input(path: str) -> None:
    """Validate that input parameters for ft_load are valid."""
    if type(path) is not str:
        raise TypeError("Path must be a string.")
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    if not os.path.isfile(path):
        raise IsADirectoryError(f"Path is a directory, not a file: {path}")
    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("Only JPG and JPEG formats are supported.")


def ft_load(path: str) -> np.ndarray:
    """Load an image, print its shape and return RGB pixel array."""
    try:
        validate_input(path)
        # with のインデントを抜けたら img.close()される
        with Image.open(path) as img:
            rgb = img.convert("RGB")
            arr = np.array(rgb)

        print(f"The shape of image is: {arr.shape}")
        return arr

    except Exception as e:
        print(f"Error: {e}")
        return None
