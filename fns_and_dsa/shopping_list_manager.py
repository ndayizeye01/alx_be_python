def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            shopping_list.append(input("Add item to the shopping list: "))
        elif choice == '2':
            # Prompt for and remove an item
            user_input = input("Enter item to Remove from the shopping list: ")
            if user_input not in shopping_list:
                print("Item not in shopping list")
            else:
                shopping_list.remove(user_input)
        elif choice == '3':
            # Display the shopping list
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()