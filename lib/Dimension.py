from Normalizer import NumericNormalizer, OptimizeFor
from Parameter import Parameter
from abc import abstractmethod

class Dimension:
    
    @abstractmethod
    def new(self, value) -> Parameter:
        pass


class NumericDimension(Dimension):
    
    def __init__(self, name: str = "Numeric", min: float = 0.0, max: float = 1.0, optimize_for = OptimizeFor.MAX) -> None:
        super().__init_()
        self._name = name
        self._normalizer = NumericNormalizer(min, max, optimize_for=optimize_for)
        
    def new(self, value: float) -> Parameter:
        return Parameter(value, self._normalizer, self._name)        

if __name__ == "__main__":
    ranking = NumericDimension(min=0, max=10, name="Ranking", optimize_for=OptimizeFor.MIN)
    rank0 = ranking.new(0)
    rank1 = ranking.new(5)
    rank2 = ranking.new(10)
    print(rank0)
    print(rank1)
    print(rank2)