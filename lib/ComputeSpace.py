from typing import List

from Dimension import Dimension


class ComputeSpace:

    def __init__(self, x: List[Dimension], y: List[Dimension]) -> None:
        self._x = x
        self._y = y

        self._x_raw_data = []
        self._y_raw_data = []

        
    def add_floats(self, xs: List, ys: List):
        # TODO add checks for lengh and data
        self._x_raw_data.append(ys)
        self._x_raw_data.append(xs)

        for index, elem in enumerate(xs):
            x.new()
        

        
    

