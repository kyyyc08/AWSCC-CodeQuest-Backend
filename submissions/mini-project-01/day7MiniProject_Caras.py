print("\n===== WELCOME TO YOUR SHOPPING LIST =====")


shopping_list = []

while True:
    print("\n\n Options: \n 1. Add item to the shopping list \n 2. View shopping list \n 3. Remove item from the shopping list \n 4. Quit")
    choice = int(input("\n Enter your choice: "))
    
    if(choice == 1):
        add_item = input("Enter the item you want to add: ")
        shopping_list.append(add_item)
        print(add_item, "has been added to your shopping list.")
        
    elif(choice == 2):
        print("Your shopping list: ")
        for item in shopping_list:
             print(item)
        
    elif(choice == 3):
        remove_item = input("Enter the item you want to remove: ")
        
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
            print(remove_item, "has been removed from your shopping list.")
        else:
            print("Item does not exist")
        
    elif(choice == 4):
            print("\nGoodbye!")
            break
        
    else:
        print("Incorrect answer. Please Re-run the program to try again.")    