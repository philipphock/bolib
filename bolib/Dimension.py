from typing import List
from bolib.Normalizer import DiscreteNormalizer, NumericNormalizer, OptimizeFor
from bolib.Parameter import Parameter
from abc import abstractmethod
import pandas as pd
class Dimension:
    
    
    @abstractmethod
    def new(self, value) -> Parameter:
        pass
    
    @abstractmethod
    def denorm(self, v) -> Parameter:
        pass 


class NumericDimension(Dimension):
    
    def __init__(self, name: str = "Numeric", min: float = 0.0, max: float = 1.0, optimize_for = OptimizeFor.MAX) -> None:
        self._name = name
        self._normalizer = NumericNormalizer(min, max, optimize_for=optimize_for)
        
    def new(self, value: float) -> Parameter:
        return Parameter(value, self._name, self._normalizer)        

    def denorm(self, v: float) -> Parameter:
        v = self._normalizer.denormalize(v)
        return Parameter(v, self._name, self._normalizer) 
    

class DiscreteDimension(Dimension):
    def __init__(self, elements: List, name: str = "Distinct") -> None:
        self._name = name
        self._elements = elements
        self._normalizer = DiscreteNormalizer(elems=elements)

    def new(self, value) -> Parameter:
        return Parameter(value, self._name, self._normalizer)        

    def denorm(self, v: float) -> Parameter:
        v = self._normalizer.denormalize(v)
        return Parameter(v, self._name, self._normalizer) 
        
if __name__ == "__main__":
    """
    ranking = NumericDimension(min=0, max=10, name="Ranking", optimize_for=OptimizeFor.MIN)
    rank0 = ranking.new(0)
    rank1 = ranking.new(5)
    rank2 = ranking.new(10)

    ranking.denorm(1)
    print(rank1)

    
    #print(rank0)
    #print(rank1)
    #print(rank2)
    """

    ddim = DiscreteDimension([0, 1,2,3,4,5])
    ddim.new(6)