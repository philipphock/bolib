from typing import List
import torch
import itertools
from Normalizer import Normalizer

class Computable:

    
    def __init__(self, original_values: List[float], normalizer: Normalizer) -> None:
        self._original = original_values
        transformed = normalizer.to_normalized_space(original_values)
        self._computable = torch.tensor([transformed], dtype=torch.double)

 
        
    @property
    def values(self):
        return self._computable

    @property
    def original(self):
        return self._original
    
if __name__ == "__main__":
    norm = Normalizer(0, 40)
    bt = Computable([10, 20, 30, 40], norm)
    print(bt.values)
    