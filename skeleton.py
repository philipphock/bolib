
from bolib.Dimension import DiscreteDimension, NumericDimension
from bolib.Bo import Bo
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

optimizer = Bo(compSpace)

init_middle = ComputeList([i.denorm(random.random()) for i in dimensions])

print(init_middle)
print("---")
def main():
    print("Welcome to the character guessing game.")
    print("The idea is that the computer tells you a descroption of yourself and you have to indicate how accurate the description is.")
    print(f"You tell the computer how good the guess is.")

    print("After some iterations, the description should fit")
    
    print("")
    print(f"Please make a single rating on a scale from 1 to 10, how well the description fits you")
    print("")
    print(f"1 = fits not at all")
    print(f"10 = fits very well")
    print("")
    input("enter to proceed")

    print("Great! Now let's start")

    while True:

        inferences = optimizer.infer()        
        new_guess = compSpace.denormalize(inferences)
        print(new_guess)
        compSpace.add_values()
                          
        print("desciption here")
        try:
            feedback = int(input("Enter rating [1 = fits not at all, 10 = fits very well]: "))        
        except:
            feedback = 1
        

        if feedback == 10:
            print(f"Great! I guessed it in {tries} tries!")
            break
        feedback = feedback / 10.0
        print(feedback)
        
        
        print("\n")
        


        tries += 1

if __name__ == "__main__":
    main()