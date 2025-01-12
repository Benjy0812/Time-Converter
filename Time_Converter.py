import sys

def menu():
    print(
        """
Welcome to the Time Converter
\nChoose an option to convert the time:
1. Seconds to minutes
2. Minutes to seconds
3. Seconds to hours
4. Hours to seconds
5. Days to hours
6. Hours to days
7. Fractional hours to normal hours and minutes
8. Normal hours and minutes to fractional hours
9. Exit
"""
    )


def getUserChoice():
    while True:
        try:
            choice = int(input("Enter the option number (1-9): ").strip())
            if choice < 1 or choice > 9:
                print("Invalid option! Please enter a number between 1 and 9.")
            else:
                return choice
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def getUserInputTime():
    while True:
        try:
            time = float(input("Enter the time to convert: ").strip())
            if time < 0:
                print("Warning: Negative number entered. Please ensure it's correct.")
                continue
            elif time > 1e9:
                print("Warning: This is a very large number. Please ensure it's correct.")
            elif time < 1e-10:
                print("Warning: This is a very small number. Please ensure it's correct.")
            return time
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def convertUserChoice(conversion_choice, user_input_time):
    if conversion_choice == 1: # Seconds to minutes
        return user_input_time / 60, "minutes"
    elif conversion_choice == 2: # Minutes to seconds
        return user_input_time * 60, "seconds"
    elif conversion_choice == 3: # Seconds to hours
        return user_input_time / 3600, "hours"
    elif conversion_choice == 4: # Hours to seconds
        return user_input_time * 3600, "seconds"
    elif conversion_choice == 5: # Days to hours
        return user_input_time * 24, "hours"
    elif conversion_choice == 6: # Hours to days
        return user_input_time / 24, "days"
    elif conversion_choice == 7: # Fractional hours to normal hours and minutes
        hours = int(user_input_time)
        minutes = int((user_input_time - hours) * 60)
        return (hours, minutes), "hours and minutes"
    elif conversion_choice == 8: # Normal hours and minutes to fractional hours
        fractional_hours = user_input_time / 60
        return fractional_hours, "fractional hours"
    else:
        return None, None


def displayResult(result, conversion_choice):
    if result is not None:
        if conversion_choice == 7:
            print(f"\nConverted value: {result[0]} hours and {result[1]} minutes")
        else:
            print(f"\nConverted value: {result[0]:.2f} {result[1]}")
    else:
        print("Conversion failed. Please try again.")
    input("Press Enter to continue...")


def main():
    while True:
        menu()
        user_choice = getUserChoice()
        if user_choice == 9:
            print("\nThank you for using the Time Converter!")
            sys.exit()
        user_input_time = getUserInputTime()
        converted_result = convertUserChoice(user_choice, user_input_time)
        displayResult(converted_result, user_choice)


if __name__ == "__main__":
    main()
