day = input("Enter a day of the week (Monday-Sunday): ")

match day.lower():
    case "monday":
     print("Uggh, Mondays.....")
    case "tuesday":
     print("At least it not moday")
    case "wednesday":
     print("Hump Day!")
    case "thursday":
     print("Almost there...")
    case "friday":
     print("TGIF!")
    case "saturday" | "sunday": 
     print("Weekend vibes!")
    case _:
        print("Invalid day entered.")
        
        
value = input("Enter a value (any data type you can think of): ")

match value:
    case int():
        print("you entered an integer:", value)
    case str():
        print("You entered a string:", value)
    case float():
        print ("you entered a float:", value)
    case _:
        print("Invalid data type entered.")