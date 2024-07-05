#create the empty list for shopping list
shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
    #simple functionalities to the list

def add_to_list(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the list")



def remove_from_list(shopping_list):
    item = input("Enter the item to remove: ")
    if item not in shopping_list:
        print(f"{item} cannot be found in the list please, please check the name and try again.")
    else:
        shopping_list.remove(item)
        print(f"{item} has been successfully removed")



def view_list(shopping_list):
    if shopping_list == []:
        print("shopping list is currently empty, add more items to the list please.")
    else:
       for item in shopping_list:
        print(f"-{item}")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_to_list(shopping_list)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove_from_list(shopping_list)
            pass
        elif choice == '3':
            # Display the shopping list
            view_list(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()