import sys
import os
import random

root_path = os.path.abspath('..')
sys.path.append(root_path)


from bolib.Dimension import DiscreteDimension, NumericDimension
from bolib.Bo import Bo
from bolib.ComputeSpace import ComputeSpace


pet     = DiscreteDimension(elements=["cat", "dog","bird", "ape", "rabbit"] ,name = "pet")
age     = NumericDimension(min=1, max=10, name="age")

RANK_MAX = 5
RANK_MIN = 0

ranking = [ NumericDimension(min=RANK_MIN, max=RANK_MAX, name="Rating") ]
dimensions = [pet, age]
compSpace = ComputeSpace(x = dimensions, y = ranking)

optimizer = Bo(compSpace)
nguess = [random.random() for _ in dimensions]
print("I will guess your pet, for this I will tell you the animal, and an age.")
print(f"You rate how close I am on a scale from {RANK_MIN} to {RANK_MAX}.")
print("A good metric is, if the animal is correct, give 2 points, then")
print("add 1 point if the year is close,")
print("add 2 points if my guess 1 year off,")
print("add 3 points if my year is correct.")
input("ready?")

g = compSpace.denormalize(nguess)

while True:
  guess = compSpace.denormalize(nguess)
  guess[1] = age.new(round(guess[1].value)) 
  print(guess.to_dataframe()[['name', "value"]])
        
  try:
    feedback = float(input(f"Enter rating [{RANK_MIN} = fits not at all, {RANK_MAX} = fits very well]: "))        
  except:
    break
  if feedback == 5:
    print(f"You have a {guess[0].value} that is {guess[1].value} years old.")
    break
  compSpace.add_value(guess, feedback)
          
  nguess = optimizer.infer()        

