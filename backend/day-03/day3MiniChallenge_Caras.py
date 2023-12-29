number = int(input("Enter a number: "))

if number < 0:
    print(f"{number} is a Negative Number!")
elif number > 0:
    print(f"{number} is a Positive Number!")
else:
    print(f"{number} is a Zero!")