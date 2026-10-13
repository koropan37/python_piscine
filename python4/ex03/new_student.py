import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character lowercase ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass  # init や repr を自動で作ってくれる
class Student:
    """Student dataclass representing student information."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)  # init=False で 初期化の引数に含めない
    id: str = field(init=False, default_factory=generate_id)
    # default_factory インスタンス別に呼ばれる
    # list や dict で主に使われる(無いとインスタンス間で共有される)

    def __post_init__(self):
        """Initialize login attribute after dataclass initialization."""
        self.login = self.name[:1].capitalize() + self.surname
