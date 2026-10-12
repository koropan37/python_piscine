class calculator:
    """Calculator class for vector calculations."""

    def __init__(self, vector: list) -> None:
        """Initialize calculator with a vector."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add the vector by a scalar and print result."""
        self.vector = [float(x + object) for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply the vector by a scalar and print result."""
        self.vector = [float(x * object) for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract the vector by a scalar and print result."""
        self.vector = [float(x - object) for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide the vector by a scalar and print result."""
        try:
            self.vector = [float(x / object) for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
