from abc import abstractmethod
from enum import Enum
from typing import List

from bolib.Float01 import Float01


class OptimizeFor(Enum):
    MIN = -1
    MAX = 1


class Normalizer:
    def __init__(self, space) -> None:
        self._space = space

    @abstractmethod
    def normalize(value: any) -> Float01:
        pass

    @abstractmethod
    def denormalize(value: Float01) -> any:
        pass

    
class IdentityNormalizer(Normalizer):
    def __init__(self, optimize_for = OptimizeFor.MAX) -> None:
        super().__init__((0, 1))
        
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
    
    
    def __init__(self, min: float, max: float, optimize_for: OptimizeFor = OptimizeFor.MAX) -> None:
        super().__init__((min, max))

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
        
        
class DiscreteNormalizer(Normalizer):
    
    def __init__(self, elems: List) -> None:
        super().__init__(elems)
        self._elems = elems
        

    def normalize(self, value) -> Float01:
        v = self._space.index(value) / len(self._elems)
        return Float01(v)

        
    
    def denormalize(self, normalized_value: Float01):
        v = round(normalized_value * len(self._elems))
        if v < 0:
            return self._elems[0]
        
        if v < len(self._elems):
            return self._elems[v]
        
        return self._elems[-1]
        
        
        
        


if __name__ == "__main__":
    """
    bt = NumericNormalizer(-100, 100, OptimizeFor.MIN)
    print(bt.normalize(-100))
    print(bt.denormalize(1))

    idn = IdentityNormalizer()
    print(idn.normalize(0))
    print(idn.normalize(1))

    print(idn.denormalize(0))
    print(idn.denormalize(1))
    """

    dn = DiscreteNormalizer(['Pizza', 'Burger', 'Tacos'])
    n = dn.normalize('Burger')
    nn = dn.denormalize(0.1)
    print(nn)
