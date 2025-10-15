class ValueTooHighError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"The value {self.value} exceeds the max limit of 100"

try:
    number = input("Enter a number: ").strip()

    if not number:
        print("Number cannot be empty.")
    else:
        number = int(number)

        if number > 100:
            raise ValueTooHighError(number)
        else:
            print(f"Valid number entered: {number}")

except ValueError:
    print("Please enter a valid integer.")
except ValueTooHighError as e:
    print(e)
