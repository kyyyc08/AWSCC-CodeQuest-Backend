print("Let's play a 2-player rock, paper, scissors game!")
print("Choices:\n[1] Rock\n[2] Paper\n[3] Scissor")

choice1 = int(input("Player 1: "))
choice2 = int(input("Player 2: "))

if (choice1 == choice2):
        print("It's a tie!")
elif (choice1 == 1 and choice2 == 2) or (choice1 == 2 and choice2 == 3) or (choice1 == 3 and choice2 == 1):
        print("Player 1 loses!")
else:
    print("Player 1 Wins!")