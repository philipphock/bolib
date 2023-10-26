from bolib.Dimension import DiscreteDimension, NumericDimension
from bolib.ComputeSpace import ComputeList, ComputeSpace
import random

gender      = DiscreteDimension(elements=["male", "female", "diverse"] ,name = "gender")
age         = NumericDimension(min=18, max=99, name="age")
height      = NumericDimension(min=100, max=200, name="height")
haircolor   = DiscreteDimension(elements=["blonde", "brown", "black", "grey", "red", "blue", "pink", "colorful"] ,name = "haircolor")
hairstyle   = DiscreteDimension(elements=["curly", "straight"] ,name = "hairstyle")
skintone    = DiscreteDimension(elements=["white", "black", "latino", "native american", "asian"] ,name = "skintone")
bodytype    = DiscreteDimension(elements=["slim", "athletic", "average", "curvy"], name = "body type")    

ranking = [ NumericDimension(min=1, max=10, name="Rating") ]
dimensions = [gender, age, height, haircolor, hairstyle, skintone, bodytype]
compSpace = ComputeSpace(x = dimensions, y = ranking)

init_middle = ComputeList([i.denorm(random.random()) for i in dimensions])

print(init_middle)
print("---")