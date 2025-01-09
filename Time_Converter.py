def time_convert(option, time, minutes=0):  # time_convert function
    """
    Converts time between seconds, minutes, hours, days, and fractional hours.

    Args:
        option (int): integer value of the conversion option
        time (float): numeric value of time to convert
        minutes (int, optional): number of minutes for fractional hour conversion (default is 0)
    Returns:
        float or tuple: converted time value and its unit.
    """
    if option == 1:  # seconds to minutes
        return time / 60, "minutes"
    elif option == 2:  # minutes to seconds
        return time * 60, "seconds"
    elif option == 3:  # seconds to hours
        return time / 3600, "hours"
    elif option == 4:  # hours to seconds
        return time * 3600, "seconds"
    elif option == 5:  # days to hours
        return time * 24, "hours"
    elif option == 6:  # hours to days
        return time / 24, "days"
    elif option == 7:
        hours = int(time)  # fractional hours to normal hours
        minutes = int((time - hours) * 60)  # fractional hours to normal minutes
        return (hours, minutes), "hours and minutes"
    elif option == 8:  # normal hours and minutes to fractional hours
        fractional_hours = time + (minutes / 60)
        return fractional_hours, "fractional hours"

def main():  # main function
    """
    Main function to run the time converter program.
    """
    print("Welcome to the Time Converter!")  # welcome message
    while True:  # run the program until the user exits
        print("\nChoose a conversion option:")
        print("1. Seconds to minutes")
        print("2. Minutes to seconds")
        print("3. Seconds to hours")
        print("4. Hours to seconds")
        print("5. Days to hours")
        print("6. Hours to days")
        print("7. Fractional hours to normal hours and minutes")
        print("8. Normal hours and minutes to fractional hours")
        print("9. Exit")

        try:  # get the option number
            option = int(input("Enter the option number (1-9): "))  # updated prompt
        except ValueError:  # invalid input
            print("Invalid input! Please enter a number between 1 and 9.")
            continue  # go back to the start of the loop

        if option == 9:  # exit the program
            print("Exiting the converter. Goodbye!")
            break  # exit the loop

        if option < 1 or option > 8:  # invalid option
            print("Invalid option selected. Please try again.")
            continue  # go back to the start of the loop

        try:  # get the time value
            time = float(input("Enter the time value to convert: "))
            if time < 0:  # negative number warning
                print("Time cannot be negative.")
                continue  # go back to the start of the loop

            elif time > 1e9:  # large number warning
                print("Warning: This is an unusually large number. Please ensure it's correct.")

            elif time < 1e-10:  # Check for very small times
                print("Warning: This is a very small time value. Conversion may result in an imprecise output.")
        except ValueError:  # invalid input
            print("Invalid input! Please enter a numeric value for time.")
            continue  # go back to the start of the loop

        # For option 8, get minutes as input as well
        if option == 8:
            minutes = int(input("Enter the number of minutes: "))  # Get minutes for fractional conversion
            result, unit = time_convert(option, time, minutes)
        else:
            result, unit = time_convert(option, time)

        if result is not None:  # valid option
            if option == 7:
                # If it's fractional hours to normal, print with hours and minutes
                print(f"Converted value: {result[0]} hours and {result[1]} minutes")
            else:
                print(f"Converted value: {result:.6f} {unit}")  # display the result
        else:  # invalid
            print("Conversion failed. Please try again.")

if __name__ == "__main__":  # run the main function
    main()  # call the main function
