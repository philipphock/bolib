import random
from fun import fit

def main():
    print("Welcome to the Number Guessing Game with Botorch!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    input("Press Enter when you're ready...")
    guess_bounds = (1, 100)  # Bounds for the guess


    tries = 0
    guesses = []
    feedbacks = []
    estimation = random.randint(1, 100)
    while True:              
        
  
        print(f"My estimation is ${estimation}.")
        feedback = int(input("How close was the last guess? (1=error > 10, 2=error < 10, 3=error < 5, 4=correct): "))        
        feedbacks.append(feedback)

        if feedback == 4:
            print(f"Great! I guessed it in {tries} tries!")
            break

        estimation = fit(estimation, feedback, guess_bounds)
        
        tries += 1

if __name__ == "__main__":
    main()