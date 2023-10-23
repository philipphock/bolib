from bolib.Normalizer import NumericNormalizer, OptimizeFor
from bolib.Parameter import Parameter
from abc import abstractmethod
import pandas as pd
class Dimension:
    
    
    @abstractmethod
    def new(self, value) -> Parameter:
        pass
    
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

if __name__ == "__main__":
    ranking = NumericDimension(min=0, max=10, name="Ranking", optimize_for=OptimizeFor.MIN)
    rank0 = ranking.new(0)
    rank1 = ranking.new(5)
    rank2 = ranking.new(10)

    ranking.denorm(1)
    print(rank1)
    #print(rank0)
    #print(rank1)
    #print(rank2)