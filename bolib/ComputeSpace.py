from typing import List

from bolib.Dimension import Dimension, NumericDimension
from bolib.Parameter import ParamList
import pandas as pd
class ComputeList(list):
    def __init__(self, data: List[ParamList] = []):
        super().__init__(data)

    def to_dataframe(self):
        return pd.concat([x.to_dataframe() for x in self], axis=0).reset_index(drop=True)

    def __repr__(self) -> str:  
        return str(self.to_dataframe())

    @property
    def values(self):
        return [i.values for i in self]
    
    @property
    def normalized(self):
        return [i.normalized for i in self]      
    
class ComputeSpace:

    def __init__(self, x: List[Dimension], y: List[Dimension]) -> None:
        self._x = x
        self._y = y

        self._x_data: ComputeList = ComputeList()
        self._y_data: ComputeList = ComputeList()

        self.xdim = len(x)
        self.ydim = len(y)




    def add_value(self, xs: List, ys: List, axis = "xy"):

        if type(xs) == type(ParamList()):
            xs = xs.values
        if type(ys) == type(ParamList()):
            ys = ys.values
        if isinstance(xs, float):
            xs = [xs]
        if isinstance(ys, float):
            ys = [ys]   

        if isinstance(xs, int):
            xs = [float(xs)]
        if isinstance(ys, int):
            ys = [float(ys)]   


        self.add_values([xs], [ys])

    def add_values(self, xs: List[List], ys: List[List], axis = "xy"):
        if len(xs) != len(ys):
            raise AttributeError(f"length of xs and ys must be equal. len(xs) = {len(xs)}, len(ys)={len(ys)}.")
        if len(xs) == 0:
            raise AttributeError(f"zero lenght parameter are not allowed")
        
        if isinstance(xs, list):
            if not isinstance(xs[0], list):
                raise AttributeError(f"xs must be of type List[List], your xs is of type List[{type(ys[0])}].")
        else:
            raise AttributeError(f"xs must be of type List[List], your xs is of type {type(ys)}.")
        
        if isinstance(ys, list):
            if not isinstance(ys[0], list):
                raise AttributeError(f"ys must be of type List[List], your ys is of type List[{type(ys[0])}].")
        else:
            raise AttributeError(f"ys must be of type List[List], your ys is of type {type(ys)}.")
        
        if "x" in axis:
            self._newdim(xs, self._x_data, self._x)
        
        if "y" in axis:
            self._newdim(ys, self._y_data, self._y)
    
    def __repr__(self) -> str:         
        return f"dim: [{self.xdim, self.ydim}]\nx:\n{self.x}\n\n-----\n\ny:\n{self.y}"
            
    def denormalize(self, value):
        
        l = ParamList()
        for i in range(self.xdim):
            l.append(self._x[i].denorm(value[i]))
        return l

    @property 
    def normalized(self):
        return (self.x.normalized, self.y.normalized)
    
    
    @property
    def x(self):
        return self._x_data

    @property
    def y(self):
        return self._y_data

    def clear_data(self):
        self._x_data = ComputeList()
        self._y_data = ComputeList()


    def to_computeList(self, l: List[List], dim: List[Dimension], update: ComputeList |None = None):
        if update is not None:
            ret = update
        else:
            ret = ComputeList()

        for elem in l: 
            #print("elem", elem)
            plist = ParamList()                             # xs = [[10, 1], [30, 2], [70, 1]]; elem =  [10, 1]
            for index_attr, attr in enumerate(dim):         # _x = [x0, x1]; xattr = x0                
                #print("attr", attr)
                elem_i = elem[index_attr]                   # elem_i = 10
                #print("elemI", elem_i)
                newdim = attr.new(elem_i)
                plist.append(newdim)
            ret.append(plist)
        return ret

    def _newdim(self, l: List[List], p: ComputeList, dim: List[Dimension]):
        self.to_computeList(l, dim, p)
                
            
        

        
if __name__ == "__main__":
    
    x0 = NumericDimension(min=0, max=100, name="p0")
    x1 = NumericDimension(min=0, max=3, name="p1")
    ranking_y = NumericDimension(min=0, max=10, name="Ranking")

    compSpace = ComputeSpace([x0], [ranking_y])

    compSpace.add_value(0,0)
    print(compSpace)
    print(compSpace.normalized)
    
    