from abc import abstractmethod
from enum import Enum

from bolib.Float01 import Float01


class OptimizeFor(Enum):
    MIN = -1
    MAX = 1


class Normalizer:
    
    @abstractmethod
    def normalize(value: any) -> Float01:
        pass

    @abstractmethod
    def denormalize(value: Float01) -> any:
        pass

class IdentityNormalizer(Normalizer):
    def __init__(self, optimize_for = OptimizeFor.MAX) -> None:
        self._min = 0
        self._max = 1
        self._opt = optimize_for
        
    def normalize(self, value: any) -> Float01:
        if self._opt == OptimizeFor.MIN:
            return 1-value
        return value
    
    def denormalize(self, value: Float01) -> any:
        if self._opt == OptimizeFor.MIN:
            return 1 - value
        
        return value




class NumericNormalizer(Normalizer):

    _identity = None
    
    
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

    idn = IdentityNormalizer()
    print(idn.normalize(0))
    print(idn.normalize(1))

    print(idn.denormalize(0))
    print(idn.denormalize(1))