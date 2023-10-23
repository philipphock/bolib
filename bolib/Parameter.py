from typing import List
from bolib.Normalizer import IdentityNormalizer, Normalizer
from bolib.Float01 import Float01
import pandas as pd


class Parameter:
    def __init__(self, value, name: str, normalizer: Normalizer = IdentityNormalizer()) -> None:
        self._value = value
        self._normalizer = normalizer
        self._normalized = normalizer.normalize(self._value)
        self._name = name
    
    def __repr__(self) -> str:     
        df = self.to_dataframe().to_string()
        return df

    def to_dataframe(self):
        data = [[self._name, self._value, self._normalizer._min, self._normalizer._max, self._normalized]]
        columns = ['name', 'value', 'min', 'max', 'normalized']
        df = pd.DataFrame(data, columns=columns)

        return df
        
        

    @property    
    def normalized(self) -> Float01:
        return self._normalized

    @property
    def value(self) -> float:
        return self._value


class ParamList(list):
    def __init__(self, data: List[Parameter] = [], printheader=True):
        super().__init__(data)
        self._printheader = printheader
    
    def to_dataframe(self):
        return pd.concat([x.to_dataframe() for x in self], axis=0).reset_index(drop=True)
    
    @property
    def normalized(self):
        return [i.normalized for i in self]
    
    def __repr__(self) -> str:
        return self.to_dataframe().to_string(header=self._printheader)
        


if __name__ == "__main__":
    p0 = Parameter(0, "p0")
    p1 = Parameter(1, "p1")    
    l = ParamList([p0, p1])

    print(l)
    print(l.normalized)

    

    