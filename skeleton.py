import torch
import random

from bolib.Dimension import DiscreteDimension, NumericDimension



gender  = DiscreteDimension(elements=["male", "female", "diverse"] ,name = "gender")
age     = NumericDimension(min=18, max=99, name="age")
height  = NumericDimension(min=100, max=200, name="height")


#[ DiscreteDimension(elements=[i*10+j for j in range(10)]  ,name=f"p{i}") for i in range(blackbox_dims) ]

ranking = [ NumericDimension(min=0, max=10, name="Rating") ]


def main():
    print("Welcome to the character guessing game.")
    print("The idea is that the computer tells you a descroption of yourself and you have to indicate how accurate the description is.")
    
    dimensons = 

    
    print(f"The computer will give you a list of {blackbox_dims} numbers.")
    print(f"You tell the computer how good the guess is.")
    print("")
    print(f"Please make a single rating on a scale from 1 to 10")
    input("enter to proceed")
    print("Great! Now let's start")

    while True:                          
        
        feedback = int(input("Please tell me how many numbers I guessed correclty"))        
        

        

        if feedback == 10:
            print(f"Great! I guessed it in {tries} tries!")
            break
        feedback = feedback / 10.0
        print(feedback)
        
      
        t_X  = torch.tensor([[est_age, est_gender]], dtype=torch.double)
        t_Y = torch.tensor([[feedback, feedback]], dtype=torch.double)        
        
        v_X = torch.cat((v_X, t_X), dim=0)
        v_Y = torch.cat((v_Y, t_Y), dim=0)
            
        
        
        est_age, est_gender = optimize(v_X, v_Y)
        
        
        print(v_X)
        print("\n")
        print(v_Y)



        tries += 1

if __name__ == "__main__":
    main()