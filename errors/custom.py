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

