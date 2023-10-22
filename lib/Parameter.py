from Dimension import Dimension, Float01
from Normalizer import NumericNormalizer, OptimizeFor

class NumericParameter():
    
    def __init__(self, value: float, min: float, max: float, optimize_for = OptimizeFor.MAX, name = None) -> None:
        super().__init__(value)
        self._name = name
        self._normalizer = NumericNormalizer(min, max, optimize_for=optimize_for)
        

    @property
    def normalized(self) -> Float01:
        return self._normalizer.normalize(self._value)

    @property
    def value(self):
        return self._normalizer.denormalize(self._value)
    
    def 
    def __repr__(self) -> str:
        n = None if self._name == None else self._name

        return f"{n}\t= {self._value}\t{self._normalizer._min, self._normalizer._max}\t n={self.normalized}"


if __name__ == "__main__":
    p0 = NumericParameter(value=10, min=0, max=10, name="Ranking")
    p1 = p0.new(0)
    print(p0)
    print(p1)