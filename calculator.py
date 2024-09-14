import os

def main():
    print("Welcome to the Simple Python Calculator!")
    
    # Detect if running in a CI environment (GitHub Actions)
    if os.getenv('CI', 'false') == 'true':
        choice = '1'  # Automatically select option 1 (Add) in CI
    else:
        print("Operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Enter choice (1/2/3/4): ")

    # Rest of your logic here...
    if choice == '1':
        print("You chose to add.")
        # Add your logic for addition here
    elif choice == '2':
        print("You chose to subtract.")
        # Subtraction logic...
    elif choice == '3':
        print("You chose to multiply.")
        # Multiplication logic...
    elif choice == '4':
        print("You chose to divide.")
        # Division logic...
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

