def time_convert(option, time):
    if option == '1':  # Seconds to minutes
        return time / 60
    elif option == '2':  # Minutes to seconds
        return time * 60
    elif option == '3':  # Seconds to hours
        return time / 3600  # 1 hour = 3600 seconds
    elif option == '4':  # Hours to seconds
        return time * 3600  # 1 hour = 3600 seconds
    elif option == '5':  # Days to hours
        return time * 24  # 1 day = 24 hours
    elif option == '6':  # Hours to days
        return time / 24  # 1 day = 24 hours
    else:
        print("Invalid option selected.")
        return None
    
def main():
    print("Welcome to the Time Converter!")
    print("Choose a conversion option")
    print("1. Seconds to minutes")
    print("2. Minutes to seconds")
    print("3. Seconds to hours")
    print("4. Hours to second") 
    print("5. Days to hours")
    print("6. Hours to days")
    
    
    option = input("Enter the option number (1-6)")
    
    try:
        time = float(input("Enter the time value to convert: "))
    except ValueError:
        print("Invalid input! please enter a numeric value for time.")
        return
    result = time_convert(option, time)
    if result is not None:
        print(f"Converted value: {result}")

if __name__ == "__main__":
    main()