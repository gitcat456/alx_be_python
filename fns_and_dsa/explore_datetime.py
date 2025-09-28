
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_datetime}")
    return current_date

def calculate_future_date():
    """
    Calculate future date based on user input days
    """
    # Get current date
    current_date = datetime.now()
    
    # Prompt user for number of days
    try:
        days = int(input("Enter number of days to add: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    
    # Calculate future date
    future_date = current_date + timedelta(days=days)  # Save future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    print(f"Future Date after {days} days: {formatted_future_date}")
    return future_date

# Main execution
if __name__ == "__main__":
    # Part 1: Display current datetime
    current = display_current_datetime()
    
    print()  # Empty line for readability
    
    # Part 2: Calculate future date
    future = calculate_future_date()  