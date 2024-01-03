import random

print("\nPlay Rock, Paper, Scissors with the Computer!")
p1_choice = input("Choose rock, paper, or scissors: ").lower()
choices = ["rock", "paper", "scissors"]
comp_choice = random.choice(choices)

if p1_choice == comp_choice:
    print(f"\nThe computer also chooses {comp_choice}. It's a tie!!!\n")
elif (p1_choice == "rock" and comp_choice == "scissors") or (p1_choice == "scissors" and comp_choice == "paper") or (p1_choice == "paper" and comp_choice == "rock"):
    print(f"\nThe computer chooses {comp_choice}. You win!!!\n")
else:
    print(f"\nThe computer chooses {comp_choice}. You lose!!!\n")