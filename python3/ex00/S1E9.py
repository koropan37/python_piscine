from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Character class"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Your docstring for Constructor by Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Your docstring for die method by Charactor"""
        pass


class Stark(Character):
    """Your docstring for Stark class"""

    def die(self) -> None:
        """Your docstring for die method by Stark"""
        self.is_alive = False
