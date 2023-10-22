from enum import Enum


from Dimension import Float01

class OptimizeFor(Enum):
    MIN = -1
    MAX = 1

class NumericNormalizer:

    _identity = None
    
    @classmethod
    def Identity(cls):
        if cls._identity is None:
            cls._identity = cls(0, 0) 
        return cls._identity
    
    def __init__(self, min: float, max: float, optimize_for: OptimizeFor = OptimizeFor.MAX) -> None:
        self._min = min
        self._max = max
        self._opt = optimize_for

    def normalize(self, value: float) -> Float01:
        if self._min == self._max == 0:
            return value
       
        n = 0
        if self._max == self._min:
            n = 0.5
        else:
            n = (value - self._min) / (self._max - self._min)
        
        if self._opt == OptimizeFor.MIN:
            n = 1 - n

        return Float01(n)

        
    
    def denormalize(self, normalized_value: Float01):
        if self._min == self._max == 0:
            return normalized_value
       

        if self._opt == OptimizeFor.MIN:
            normalized_value = 1 - normalized_value
        o= normalized_value * (self._max - self._min) + self._min
        
        return o
        
        



if __name__ == "__main__":
    bt = NumericNormalizer(-100, 100, OptimizeFor.MIN)
    print(bt.normalize(-100))
    print(bt.denormalize(1))