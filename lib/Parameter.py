from Dimension import Dimension, Float01
from Normalizer import NumericNormalizer, OptimizeFor

class NumericParameter(Dimension):
    
    def __init__(self, value: float, min: float, max: float, optimize_for = OptimizeFor.MAX, name = None) -> None:
        super().__init__()
        self._value = value
        self._normalizer = NumericNormalizer(min, max, optimize_for=optimize_for)
        

    def for_optimizer(self) -> Float01:
        return self._normalizer.normalize(self._value)

    def for_user(self):
        return self._normalizer.denormalize(self._value)
    
    