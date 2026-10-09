from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Load an image, slice, transpose it manually and display."""

    try:
        arr = ft_load("animal.jpeg")
        if arr is None:
            return
        zoomed = arr[100:500, 450:850, 0:1]
        print(f"The shape of image is: {zoomed.shape}")
        print(zoomed)
        height = zoomed.shape[0]
        width = zoomed.shape[1]
        # 二重ループと同じ
        transposed = [
            [zoomed[y][x][0] for y in range(height)]
            for x in range(width)
        ]
        transposed_arr = np.array(transposed)
        print(f"New shape after transpose: {transposed_arr.shape}")
        print(transposed_arr)

        plt.imshow(transposed_arr, cmap="gray")
        plt.show()

    except Exception as e:
        print(f"error: {e}")


if __name__ == "__main__":
    main()
