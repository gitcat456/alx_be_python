class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items"""
    
    def __init__(self, item_name):
        self.item_name = item_name
        
    #specifies which error message to be displayed when the exception is raised    
    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."
    
    
#sample product inventory
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0
}

def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase succesfull: {quantity} {item}(s)")
    except KeyError:
       print(f"Sorry, '{item}' is not available in our inventory.")

#testing the custom exception

try:
    purchase_item("apple", 3)
    purchase_item("orange", 1)
    purchase_item("watermelon", 4)
except OutOfStockError as e:
    print(e)