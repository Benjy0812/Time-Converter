def time_convert(option, time):  # time_convert function
    """
    Converts time between seconds, minutes, hours, and days.

    Args:
        option (int): integer value of the conversion option
        time (float): numeric value of time to convert
    Returns:
        float: converted time value
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
    else:  # if everything fails
        return None, None  # invalid option


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
        print("7. Exit")

        try: # get the option number
            option = int(input("Enter the option number (1-7): "))  # get the option number
        except ValueError: # invalid input
            print("Invalid input! Please enter a number between 1 and 7.") # invalid input
            continue # go back to the start of the loop

        if option == 7:  # exit the program
            print("Exiting the converter. Goodbye!") # exit message
            break  # exit the loop

        if option < 1 or option > 6:  # invalid option
            print("Invalid option selected. Please try again.") # invalid option
            continue # go back to the start of the loop

        try: # get the time value
            time = float(input("Enter the time value to convert: "))  # get the time value
        except ValueError:  # invalid input
            print("Invalid input! Please enter a numeric value for time.") # invalid input
            continue # go back to the start of the loop

        result, unit = time_convert(option, time)  # call the time_convert function
        if result is not None:  # valid option
            print(f"Converted value: {result:.2f} {unit}") # display the result
        else: # invalid
            print("Conversion failed. Please try again.")  # invalid option


if __name__ == "__main__":  # run the main function
    main()  # call the main function
