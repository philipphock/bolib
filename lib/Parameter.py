from Normalizer import Normalizer
from Float01 import Float01

class Parameter:
    def __init__(self, value, normalizer: Normalizer, name: str) -> None:
        self._value = value
        self._normalizer = normalizer
        self._normalized = normalizer.normalize(self._value)
        self._name = name

    def __repr__(self) -> str:
        n = "" if self._name == None else self._name

        return f"{n}\t= {self._value}\t{self._normalizer._min, self._normalizer._max}\t n={self.normalized}"

    
    @property    
    def normalized(self) -> Float01:
        return self._normalized

    @property
    def value(self) -> float:
        return self._value


if __name__ == "__main__":
    pass
    