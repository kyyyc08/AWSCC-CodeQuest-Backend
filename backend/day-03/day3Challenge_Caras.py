print("\nThere's a man asking for shelter, would you let him in?")
print("[1] Yes\n[2] No\n")

answer = int(input("Answer: "))
             
if answer == 2:
    print("\nPolice arrived & Asked whether thief is inside. Is he inside?\n[1] Yes\n[2] No")
    answer2 = int(input("Answer: "))
    
    if answer2 == 2:
        print("\nGame Over!!!")
    elif answer2 == 1:
        print("\nYou Win!")
    else:
        print("Incorrect answer. Please Re-run the program to try again.")

elif answer == 1:
    print("\nHe attacked on you. Will you knock him down?\n[1] Yes\n[2] No")
    answer2 = int(input("Answer: "))
    
    if answer2 == 2:
        print("\nGame Over!!!")
    elif answer2 == 1:
        print("\nYou Win!")
    else:
        print("Incorrect answer. Please Re-run the program to try again.")
    
else:
    print("Incorrect answer. Please Re-run the program to try again.")    
