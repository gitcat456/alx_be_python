def divide(x, y):
    try:
        result = x/y
        return result
    except ZeroDivisionError:
        print('Error: cannot divide by zero.')
    except TypeError:
        print("Error: Voth arguments must be integers")
        

try:
    first_no = input("Enter first number:").strip()
    sec_no = input("Enter second number:").strip()
    
    if not first_no or not sec_no:
        print(f"please enter both the first and second number")
    else: 
        first_no = int(first_no)
        sec_no = int(sec_no)
except ValueError:
    print("please enter a valid integer")
    
else:
    divide(first_no , sec_no)





