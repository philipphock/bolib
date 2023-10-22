from abc import abstractmethod

class Float01(float):
    def __new__(cls, value):
        if 0 <= value <= 1:
            return super(Float01, cls).__new__(cls, value)
        else:
            raise ValueError("Value must be between 0 and 1")

class Dimension:
    def __init__(self) -> None:
        pass

    @property
    @abstractmethod
    def for_optimizer(self) -> Float01:
        pass

    @property
    @abstractmethod
    def for_user(self) -> float:
        pass


if __name__ == "__main__":
    pass
    