import torch
import random
from fun import optimize
def main():
    print("Welcome to the Number Guessing Game with Botorch!")
    print("The idea is that the computer must find the 2 values (Age, Gender) according to your feedback")
    print("Age is 35, Gender is 2")
    input("Press Enter when you're ready...")
    

    tries = 0
    est_age = random.randint(1, 100)
    est_gender = random.randint(1, 3)
    v_X = torch.tensor([],dtype=torch.double)
    v_Y = torch.tensor([], dtype=torch.double)

    while True:              
        print("\n----------------------")
        print(f"Age     =  {est_age}.")
        print(f"Gender  =  {est_gender}.")
                
        feedback = int(input("Please give a Rating between 1 and 10 where 1 is far away and 10 is very close: "))        


        

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