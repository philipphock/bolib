from enum import Enum

from typing import List

class OptimizeFor(Enum):
    MIN = -1
    MAX = 1

class Normalizer:

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

    def _normalize(self, values: List[float], min_val: List[float], max_val: List[float]):
        ret = []
        for v in values:
            if max_val == min_val:
                n = 0.5
            else:
                n = (v - min_val) / (max_val - min_val)
            
            if self._opt == OptimizeFor.MIN:
                n = 1 - n

            ret.append(n)
        return ret

        
    
    def _denormalize(self, normalized_value: float, min_val: List[float], max_val: List[float]):

        self._check_if_normalized(normalized_value)
        ret = []        
        for v in normalized_value:
            if self._opt == OptimizeFor.MIN:
                v = 1 - v
            o= v * (max_val - min_val) + min_val
            
            ret.append(o)
        
        return o
    
    def to_normalized_space(self, values: List[float]):
        if self._min == self._max == 0:
            return values
        
        return self._normalize(values, self._min, self._max)
    
    def to_original_space(self, values: List[float]):
        if self._min == self._max == 0:
            return values
        
        self._check_if_normalized(values)
        return self._denormalize(values, self._min, self._max)

    def _check_if_normalized(self, values: List[float]):
        for v in values:
            if v > 1 or v < 0:
                raise AttributeError(f"computable values must be between 0 and 1, yours it {value}")
        

if __name__ == "__main__":
    bt = Normalizer(-100, 100, OptimizeFor.MIN)
    print(bt.to_normalized_space([-100, 100]))
    print(bt.to_original_space([0.5]))