class Calculator:
    """
    A Calculator class demonstrating the use of static and class methods.
    
    This class showcases:
    - @staticmethod: For utility functions that don't need class or instance data
    - @classmethod: For methods that need access to class-level attributes
    """
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        This method doesn't need access to class or instance attributes,
        so it's defined as a static method. It can be called without
        instantiating the class.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        This method uses the cls parameter to access class attributes.
        It prints the calculation_type before performing multiplication.
        
        Args:
            cls: Reference to the class itself
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b