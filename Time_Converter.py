def time_convert(conversion_choice, time_value, minutes=0): # Time conversion function
    """
    Converts time between seconds, minutes, hours, days, and fractional hours.

    Args:
        conversion_choice (int): integer value of the conversion option
        time_value (float): numeric value of time to convert
        minutes (int, optional): number of minutes for fractional hour conversion (default is 0)
    Returns:
        float or tuple: converted time value and its unit.
    """
    if conversion_choice == 1:  # seconds to minutes
        return time_value / 60, "minutes" # 1 minute = 60 seconds
    elif conversion_choice == 2:  # minutes to seconds
        return time_value * 60, "seconds" # 1 minute = 60 seconds
    elif conversion_choice == 3:  # seconds to hours
        return time_value / 3600, "hours" # 1 hour = 3600 seconds
    elif conversion_choice == 4:  # hours to seconds
        return time_value * 3600, "seconds" # 1 hour = 3600 seconds
    elif conversion_choice == 5:  # days to hours
        return time_value * 24, "hours" # 1 day = 24 hours
    elif conversion_choice == 6:  # hours to days
        return time_value / 24, "days" # 1 day = 24 hours
    elif conversion_choice == 7: # fractional hours to normal hours and minutes
        hours = int(time_value)  # whole hours
        minutes = int((time_value - hours) * 60)  # fractional hours to normal minutes
        return (hours, minutes), "hours and minutes"
    elif conversion_choice == 8:  # normal hours and minutes to fractional hours
        fractional_hours = time_value + (minutes / 60)
        return fractional_hours, "fractional hours"

def get_time_value():  # Helper function to get time value
    """
    Gets a valid time value from the user with error handling and warnings for edge cases.

    Returns:
        float: Valid time value or None if input is invalid.
    """
    try: # get the time value from the user
        time_value = float(input("Enter the time value: ")) # get the time value
        if time_value < 0: # negative time value
            print("\nWarning: Negative time value entered. Please ensure it's correct.")
            return None # return None for negative time value
        elif time_value > 1e9: # very large number
            print("\nWarning: This is a very large number. Please ensure it's correct.")
        elif time_value < 1e-10: # very small number
            print("\nWarning: This is a very small number. Please ensure it's correct.")
        return time_value # return the valid time value
    except ValueError: # invalid input
        print("\nInvalid input! Please enter a valid number.")
        return None # return None for invalid input

def main():  # main function
    """
    Main function to run the time converter program.
    """
    print("Welcome to the Time Converter!")
    while True:  # run the program until the user exits
        print("\nChoose an option to convert the time:")
        print("1. Seconds to minutes")
        print("2. Minutes to seconds")
        print("3. Seconds to hours")
        print("4. Hours to seconds")
        print("5. Days to hours")
        print("6. Hours to days")
        print("7. Fractional hours to normal hours and minutes")
        print("8. Normal hours and minutes to fractional hours")
        print("9. Exit")

        try:  # get the conversion choice
            conversion_choice = int(input("Enter the option number (1-9): "))
        except ValueError:  # invalid input
            print("\nInvalid input! Please enter a valid number between (1-9)")
            input("Press Enter to continue...")
            continue  # go back to the start of the loop
        
        if conversion_choice == 9:  # exit the program
            print("\nThank you for using the Time Converter!")
            break  # exit the loop

        if conversion_choice < 1 or conversion_choice > 8:  # invalid option
            print("\nInvalid option! Please enter a number between 1 and 8.")
            input("Press Enter to continue...")
            continue  # go back to the start of the loop

        time_value = get_time_value()  # Get the time value using the helper function
        if time_value is None:  # If the input is invalid, go back to the start of the loop
            continue # go back to the start of the loop

        if conversion_choice == 8:  # If it's normal hours and minutes to fractional, get minutes
            try: # get the number of minutes
                minutes = int(input("Enter the number of minutes (0-59): "))
                if minutes < 0 or minutes >= 60: # Check if the minutes are valid
                    print("\nInvalid minutes! Please enter a value between 0 and 59.")
                    continue # go back to the start of the loop
            except ValueError:
                print("\nInvalid input! Minutes should be a whole number.")
                continue # go back to the start of the loop
            result, unit = time_convert(conversion_choice, time_value, minutes)  # Call the function with minutes
        else: # Otherwise
            result, unit = time_convert(conversion_choice, time_value) # Call the function without minutes

        if result is not None:  # valid option
            if conversion_choice == 7:  # If it's fractional hours to normal hours and minutes
                print(f"\nConverted value: {result[0]} hours and {result[1]} minutes")
            else:  # Otherwise, print the converted value with the unit
                print(f"\nConverted value: {result:.2f} {unit}")
            input("Press Enter to continue...")
        else:  # invalid
            print("Conversion failed. Please try again.")

if __name__ == "__main__": # run the program if it's the main module
    main()  # call the main function
