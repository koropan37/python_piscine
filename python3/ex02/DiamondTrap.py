from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Your docstring for King class"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Your docstring for Constructor by King"""
        super().__init__(first_name, is_alive)
        # King > Baratheon > Lannister > Character の順に呼ばれる
        # 最終的に Baratheon の値に上書きされる

    @property
    def eyes(self) -> str:
        """Getter for eyes property."""
        return self.__dict__["eyes"]
    # self.eyes とすると無限ループ
    # 一般的には _eyes とするが、課題に合わせるための書き方

    @eyes.setter
    def eyes(self, value: str) -> None:
        """Setter for eyes property."""
        self.__dict__["eyes"] = value

    def get_eyes(self) -> str:  # property と同じ
        """Getter eyes."""
        return self.eyes

    def set_eyes(self, value: str) -> None:  # @x.setter と同じ
        """Setter eyes."""
        self.eyes = value

    @property
    def hairs(self) -> str:
        """Getter for hairs property."""
        return self.__dict__["hairs"]

    @hairs.setter
    def hairs(self, value: str) -> None:
        """Setter for hairs property."""
        self.__dict__["hairs"] = value

    def get_hairs(self) -> str:
        """Getter hairs."""
        return self.hairs

    def set_hairs(self, value: str) -> None:
        """Setter hairs."""
        self.hairs = value
