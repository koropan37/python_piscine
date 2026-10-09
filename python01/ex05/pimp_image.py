import matplotlib.pyplot as plt
import numpy as np


def validate_array(array: np.ndarray) -> None:
    """Validate that the input is a valid 3D RGB image array."""
    if type(array) is not np.ndarray:
        raise TypeError("Array must be a numpy.ndarray.")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("Array must be a 3D RGB image (shape: (H, W, 3)).")
    if array.size == 0:
        raise ValueError("Array is empty.")


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    try:
        validate_array(array)

        inverted = 255 - array
        plt.imshow(inverted)
        plt.axis("off")
        plt.show()
        return inverted

    except Exception as e:
        print(f"Error: {e}")
        return None


def ft_red(array: np.ndarray) -> np.ndarray:
    """Applies a red filter to the image received."""
    try:
        validate_array(array)

        red = array * [1, 0, 0]
        plt.imshow(red)
        plt.axis("off")
        plt.show()
        return red

    except Exception as e:
        print(f"Error: {e}")
        return None


def ft_green(array: np.ndarray) -> np.ndarray:
    """Applies a green filter to the image received."""
    try:
        validate_array(array)

        green = array.copy()
        green[:, :, 0] = green[:, :, 0] - green[:, :, 0]  # R = 0
        green[:, :, 2] = green[:, :, 2] - green[:, :, 2]  # B = 0

        plt.imshow(green)
        plt.axis("off")
        plt.show()
        return green

    except Exception as e:
        print(f"Error: {e}")
        return None


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Applies a blue filter to the image received."""
    try:
        validate_array(array)

        blue = array.copy()
        blue[:, :, :2] = 0
        plt.imshow(blue)
        plt.axis("off")
        plt.show()
        return blue

    except Exception as e:
        print(f"Error: {e}")
        return None


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Applies a grey filter to the image received."""
    try:
        validate_array(array)

        rgb = array.sum(axis=2)
        grey_n = rgb / 3
        grey = array.copy()
        grey[:, :, 0] = grey_n
        grey[:, :, 1] = grey_n
        grey[:, :, 2] = grey_n
        plt.imshow(grey)
        plt.axis("off")
        plt.show()
        return grey

    except Exception as e:
        print(f"Error: {e}")
        return None
