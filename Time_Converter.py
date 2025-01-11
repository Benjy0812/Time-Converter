def time_convert(conversion_choice, time_value, minutes=0):
    """ Convert time values between seconds, minutes, hours, and days, fractional hours.

    Args:
        conversion_choice (int): _description_
        time_value (float): returned time_value
        minutes (int, optional): _description_. Defaults to 0.

    Returns:
        float: converted time value
    """
    if conversion_choice == 1:  # seconds to minutes
        return time_value / 60, "minutes"
    elif conversion_choice == 2:  # minutes to seconds
        return time_value * 60, "seconds"
    elif conversion_choice == 3:  # seconds to hours
        return time_value / 3600, "hours"
    elif conversion_choice == 4:  # hours to seconds
        return time_value * 3600, "seconds"
    elif conversion_choice == 5:  # days to hours
        return time_value * 24, "hours"
    elif conversion_choice == 6:  # hours to days
        return time_value / 24, "days"
    elif conversion_choice == 7:  # fractional hours to normal hours and minutes
        hours = int(time_value)
        minutes = int((time_value - hours) * 60)
        return (hours, minutes), "hours and minutes"
    elif conversion_choice == 8:  # normal hours and minutes to fractional hours
        fractional_hours = time_value + (minutes / 60)
        return fractional_hours, "fractional hours"


def get_time_value():
    """
    Gets a valid time value from the user with error handling and warnings for edge cases.

    Returns:
        float: Valid time value or None if input is invalid.
    """
    try:
        time_value = float(input("Enter the time value: ").strip())
        
        if time_value < 0:
            print("\nWarning: Negative time value entered. Please ensure it's correct.")
            return None
        elif time_value > 1e9:
            print("\nWarning: This is a very large number. Please ensure it's correct.")
        elif time_value < 1e-10:
            print("\nWarning: This is a very small number. Please ensure it's correct.")
        return time_value
    except ValueError:
        print("\nInvalid input! Please enter a valid number.")
        return None


def main():
    """
    Main function to run the time converter program.
    """
    print("Welcome to the Time Converter!")
    while True:
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

        try:
            conversion_choice = int(input("Enter the option number (1-9): ").strip())
        except ValueError:
            print("\nInvalid input! Please enter a valid number between 1 and 9.")
            input("Press Enter to continue...")
            continue

        if conversion_choice == 9:
            print("\nThank you for using the Time Converter!")
            break

        if conversion_choice < 1 or conversion_choice > 8:
            print("\nInvalid option! Please enter a number between 1 and 8.")
            input("Press Enter to continue...")
            continue

        time_value = get_time_value()
        if time_value is None:
            continue

        if conversion_choice == 8:
            try:
                minutes = int(input("Enter the number of minutes (0-59): ").strip())
                if minutes < 0 or minutes >= 60:
                    print("\nInvalid minutes! Please enter a value between 0 and 59.")
                    continue
            except ValueError:
                print("\nInvalid input! Minutes should be a whole number.")
                continue
            result, unit = time_convert(conversion_choice, time_value, minutes)
        else:
            result, unit = time_convert(conversion_choice, time_value)

        if result is not None:
            if conversion_choice == 7:
                print(f"\nConverted value: {result[0]} hours and {result[1]} minutes")
                input("Press Enter to continue...")
            else:
                print(f"\nConverted value: {result:.2f} {unit}")
                input("Press Enter to continue...")
        else:
            print("Conversion failed. Please try again.")


if __name__ == "__main__":
    main()
