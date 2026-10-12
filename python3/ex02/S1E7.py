from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor by Baratheon"""
        super().__init__(first_name, is_alive)  # 親(super) class の機能を呼び出す
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        """Your docstring for die method by Baratheon"""
        self.is_alive = False

    def __str__(self) -> str:  # print(obj)で呼ばれる
        """Your docstring for __str__ method by Baratheon"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:  # log, debug 用
        """Your docstring for __repr__ method by Baratheon"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor by Lannister"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self) -> None:
        """Your docstring for die method by Lannister"""
        self.is_alive = False

    def __str__(self) -> str:
        """Your docstring for __str__ method by Lannister"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Your docstring for __repr__ method by Lannister"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod  # インスタンス化せずに呼び出せる
    def create_lannister(cls, first_name: str, is_alive: bool = True
                         ) -> "Lannister":  # == Self(3.11ver以上)
        """Class method to create characters in a chain."""
        return cls(first_name, is_alive)
