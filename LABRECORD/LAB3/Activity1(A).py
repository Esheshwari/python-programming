# Program to perform various operations on a list
def list_operations():
    my_list = []  # Initialize an empty list

    while True:
        # Display menu
        print("\nList Operations:")
        print("1. Insert an element")
        print("2. Delete an element")
        print("3. Find an element")
        print("4. Display the list")
        print("5. Sort the list")
        print("6. Reverse the list")
        print("7. Exit")

        # Get user choice
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")
            continue

        if choice == 1:  # Insert an element
            element = input("Enter element to insert: ")
            my_list.append(element)
            print(f"Element '{element}' inserted.")
        elif choice == 2:  # Delete an element
            element = input("Enter element to delete: ")
            if element in my_list:
                my_list.remove(element)
                print(f"Element '{element}' deleted.")
            else:
                print(f"Element '{element}' not found.")
        elif choice == 3:  # Find an element
            element = input("Enter element to find: ")
            if element in my_list:
                print(f"Element '{element}' found.")
            else:
                print(f"Element '{element}' not found.")
        elif choice == 4:  # Display the list
            print(f"Current list: {my_list}")
        elif choice == 5:  # Sort the list
            my_list.sort()  # Sorts the list in ascending order
            print(f"List sorted: {my_list}")
        elif choice == 6:  # Reverse the list
            my_list.reverse()  # Reverses the list
            print(f"List reversed: {my_list}")
        elif choice == 7:  # Exit the program
            print("Exiting the program. Goodbye!")
            break
        else:  # Invalid choice
            print("Invalid choice, please try again.")

# Run the program
list_operations()
