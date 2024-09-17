#Convert hours to minutes and minutes to seconds
print("""
        TIME CONVERTION
    [hours-minutes-seconds]
""")
while True:
    try:
        choose = int(input("""
    Choose what to convert: 
    1. Hour(s) to minute(s)
    2. Hour(s) to second(s)
    3. Minute(s) to second(s)
    4. Minute(s) to hour(s)
    5. Second(s) to hour(s)
    6. Second(s) to minute(s)
            
    Enter the NUMBER of your choice: """))

        if choose < 1 or choose > 6:
            print("Invalid choice. Please enter a number from (1-6).")
            continue

        if choose == 1: #Hour(s) to minute(s)
            hours = int(input("Enter how many hour(s): "))
            print(f"{hours} hour(s) is equal to {hours * 60} minutes.")
        elif choose == 2: #Hour(s) to second(s)
            hours = int(input("Enter how many hour(s): "))
            print(f"{hours} hour(s) is equal to {hours * 3600} seconds.")
        elif choose == 3: #Minute(s) to second(s)
            minutes = int(input("Enter how many minutes(s): "))
            print(f"{minutes} minute(s) is equal to {minutes * 60} seconds.")
        elif choose == 4: #Minute(s) to hour(s)
            minutes = int(input("Enter how many minutes(s): "))
            print(f"{minutes} minute(s) is equal to {minutes / 60} hours.")
        elif choose == 5: #Second(s) to hour(s)
            seconds = int(input("Enter how many second(s): "))
            print(f"{seconds} second(s) is equal to {seconds / 3600} hours.")
        elif choose == 6: #Second(s) to minute(s)
            seconds = int(input("Enter how many second(s): "))
            print(f"{seconds} second(s) is equal to {seconds / 60} minutes.")

        choice = input("Do you want to continue? [Y/N]: ")
        if choice.lower() != 'y':
            print("Arigato Salamat!")
            break

    except ValueError:
        print("    Invalid choice. Please enter an integer type.")