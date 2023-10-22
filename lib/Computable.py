from typing import List
import torch
from Normalizer import Normalizer

class Computable:

    
    def __init__(self, original_values: List[float], normalizer: Normalizer = Normalizer.Identity()) -> None:
        self._original = original_values        
        transformed = normalizer.to_normalized_space(original_values)
        self._computable = torch.tensor([transformed], dtype=torch.double)

 
    def __repr__(self) -> str:
        #return f"{self._computable} ({self._original})"
        return f"{self._original}"
        
    @property
    def values(self):
        return self._computable

    def get_raw_tensor_values(self):
        return self._computable.detach().cpu().numpy().tolist()

    @property
    def original(self):
        return self._original
    
if __name__ == "__main__":
    norm = Normalizer(0, 40)
    bt = Computable([10, 20, 30, 40], norm)
    print(bt.values)
    