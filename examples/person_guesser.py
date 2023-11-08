
import sys
import os
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

from bolib import Parameter
from bolib.Dimension import DiscreteDimension, NumericDimension
from bolib.Bo import Bo
from bolib.ComputeSpace import ComputeList, ComputeSpace
from bolib.Parameter import ParamList
import random

gender      = DiscreteDimension(elements=["male", "female", "diverse"] ,name = "gender")
age         = NumericDimension(min=18, max=70, name="age")
height      = NumericDimension(min=160, max=190, name="height")
haircolor   = DiscreteDimension(elements=["blonde", "brown", "black", "grey", "red", "blue", "pink", "colorful"] ,name = "haircolor")
hairstyle   = DiscreteDimension(elements=["curly", "straight"] ,name = "hairstyle")
skintone    = DiscreteDimension(elements=["white", "black", "latino", "native american", "asian"] ,name = "skintone")
bodytype    = DiscreteDimension(elements=["slim", "athletic", "average", "curvy"], name = "body type")    

RANK_MAX = 5
RANK_MIN = 1

ranking = [ NumericDimension(min=1, max=5, name="Rating") ]
dimensions = [gender, age, height, haircolor, hairstyle, skintone, bodytype]
compSpace = ComputeSpace(x = dimensions, y = ranking)

optimizer = Bo(compSpace)


def get_rating(l: ParamList):
    p0 = 1 if l[0].value == "male" else 0
    
    p1 = 1-(abs(l[1].value-36))/l[1]._normalizer._max
    p2 = 1-(abs(l[2].value-176))/l[2]._normalizer._max
    
    p3 = 1 if l[3].value == "black" else 0
    p4 = 1 if l[4].value == "straight" else 0
    p5 = 1 if l[5].value == "white" else 0
    p6 = 1 if l[6].value == "average" else 0
    
    ret = [p0, p1, p2, p3, p4, p5, p6]
    return (sum(ret)/len(ret))*10
    


def main():
    normalized_guess = [random.random() for _ in dimensions]

    print("Welcome to the character guessing game.")
    print("The idea is that the computer tells you a descroption of yourself and you have to indicate how accurate the description is.")
    print(f"You tell the computer how good the guess is.")

    print("After some iterations, the description should fit")
    
    print("")
    print(f"Please make a single rating on a scale from {RANK_MIN} to {RANK_MAX}, how well the description fits you")
    print("")
    print(f"{RANK_MIN} = fits not at all")
    print(f"{RANK_MAX} = fits very well")
    print("")
    input("enter to proceed")

    print("Great! Now let's start")
    tries = 0
    while True:
        print("Are you this person?")
        guess = compSpace.denormalize(normalized_guess)
        print(guess.to_dataframe()[['name', "value"]])
        
        feedback = 0
        try:
            feedback = float(input(f"Enter rating [{RANK_MIN} = fits not at all, {RANK_MAX} = fits very well]: "))        
        except:
            break

        compSpace.add_value(guess, feedback)
        
        normalized_guess = optimizer.infer()        
        
        if feedback == RANK_MAX:
            print(f"Great! I guessed it in {tries} tries!")
            break        
        
        print("\n")
        


        tries += 1

if __name__ == "__main__":
    main()