from typing import List

from Dimension import Dimension, NumericDimension
from Parameter import ParamList, Parameter


class ComputeSpace:

    def __init__(self, x: List[Dimension], y: List[Dimension]) -> None:
        self._x = x
        self._y = y

        self._x_data: List[ParamList] = []
        self._y_data: List[ParamList] = []

        
    def add_floats(self, xs: List[List[float]], ys: List[List[float]]):
        if len(xs) != len(ys):
            raise AttributeError(f"length of xs and ys must be equal. len(xs) = {len(xs)}, len(ys)={len(ys)}.")
        
        self._newdim(xs, self._x_data, self._x)
        self._newdim(ys, self._y_data, self._y)
    
    def __repr__(self) -> str:        
            #rank0.to_dataframe()
            #result = pd.concat([rank0.to_dataframe(), rank1.to_dataframe()], axis=0)
            #result = result.reset_index(drop=True)
            
            self._x_data[0]

            #xs = ',\n'.join(map(str,compSpace.x))            

            #ys = ',\n'.join(map(str,compSpace.y))
            #return f"x:\n{xs}\n\ny:\n{ys}"
            return xs

    
    @property
    def x(self):
        return self._x_data

    @property
    def y(self):
        return self._y_data

    def _newdim(self, l: List[List[float]], p: List[ParamList], dim: List[Dimension]):
        for elem in l: 
            print(elem)  
            group = []                                   # xs = [[10, 1], [30, 2], [70, 1]]; elem =  [10, 1]
            for index_attr, attr in enumerate(dim):         # _x = [x0, x1]; xattr = x0
                print(attr) 
                elem_i = elem[index_attr]                   # elem_i = 10
                newdim = attr.new(elem_i)
                group.append(newdim)
            p.append(group)
                
                
            
        

        
if __name__ == "__main__":
    x0 = NumericDimension(min=0, max=100, name="p0")
    x1 = NumericDimension(min=0, max=3, name="p1")
    ranking_y = NumericDimension(min=0, max=10, name="Ranking")

    compSpace = ComputeSpace([x0, x1], [ranking_y])
    compSpace.add_floats(xs = [[100, 2], [10, 1]], ys=[[10],[0]])
    print(compSpace)
    #print(xs)   
    #print()
    #print(ys)   

    