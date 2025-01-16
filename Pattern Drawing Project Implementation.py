import colorama
from colorama import Fore
colorama.init(autoreset=True)


# 🖼️ Python Pattern Drawing Project

while True:
    # Step 1: Display a menu to the user
    print("🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")

    # Step 2: Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5]:  # Patterns that need size
        size = int(input("Enter the size of the square: "))

    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle

        for row in range(1, rows + 1):
            for col in range(1, row + 1):
                print(Fore.RED + '*', end="")
            print()

    elif choice == 2:  # Square with Hollow Center

        for row in range(1, size + 1):

            if row == 1 or row == size:
                for col in range(1, size + 1):
                    print(Fore.GREEN + "*", end="")

            else:
                for col in range(1, size + 1):
                    if col == 1 or col == size:
                        print(Fore.LIGHTYELLOW_EX +"*", end="")
                    else:
                        print(end=" ")
            print()

    elif choice == 3:  # Diamond
        for row in range(1, rows + 1):
            spc = " " * (rows - row)
            print(spc + (Fore.MAGENTA + "*" * (2 * row - 1)) + spc)

        for row in range(rows - 1, 0, -1):
            spc = " " * (rows - row)
            print(spc + (Fore.CYAN + "*" * (2 * row - 1)) + spc)

    elif choice == 4:  # Left-angled Triangle

        for row in range(1, rows + 1):
            for col in range((rows + 1) - row):
                print(Fore.BLUE + "*", end="")
            print()

    elif choice == 5:  # Hollow Square
        for row in range(1, size + 1):

            if row == 1 or row == size:
                for col in range(1, size + 1):
                    print(Fore.LIGHTCYAN_EX + "*", end="")

            else:
                for col in range(1, size + 1):
                    if col == 1 or col == size:
                        print(Fore.LIGHTCYAN_EX + "*", end="")
                    else:
                        print(end=" ")
            print()

    elif choice == 6:  # Pyramid
        for row in range(1, rows + 1):
            spc = " " * (rows - row)
            print(spc + (Fore.LIGHTMAGENTA_EX + "*" * (2 * row - 1)) + spc)



    elif choice == 7:  # Reverse Pyramid
        for row in range(rows, 0, -1):
            spc = " " * (rows - row)
            print(spc + (Fore.LIGHTRED_EX + "*" * (2 * row - 1)) + spc)

    elif choice == 8:  # Rectangle with Hollow Center
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))

        for row in range(1, height + 1):

            if row == 1 or row == height:
                for col in range(1, width + 1):
                    print(Fore.LIGHTYELLOW_EX + "*", end="")

            else:
                for col in range(1, width + 1):
                    if col == 1 or col == width:
                        print(Fore.LIGHTGREEN_EX + "*", end="")
                    else:
                        print(end=" ")
            print()

    else:
        print("❌ Invalid choice! Please restart the program.")

    #User is given a choice how to proceed
    print("What do you want to do next?")
    print('1. Restart')
    print('2. Exit')

    #Takes input from the menu above
    final_choice = int(input())

    #If the input is not corresponding to the choices given, prints an error message
    #and takes input again.
    #Then the program restarts or exits depending on the choice.

    while final_choice != 1 and final_choice != 2:
        print('Error. Please enter a valid choice.')
        final_choice = int(input())

    if final_choice == 2:
        print('Bye!')
        break




