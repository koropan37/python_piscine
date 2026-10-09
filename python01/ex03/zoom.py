from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """Load an image, display its info, zoom/slice it and show the plot."""

    try:
        arr = ft_load("animal.jpeg")
        if arr is None:
            return
        print(arr)
        zoomed = arr[100:500, 450:850, 0:1]  # 多次元スライス[Y, X, color]
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        plt.imshow(zoomed, cmap="gray")
        plt.show()

    except Exception as e:
        print(f"error: {e}")


if __name__ == "__main__":
    main()
