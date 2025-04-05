def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.
    
    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """
    try:
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("non-numeric input")
        if operator=="+":
            return a+b
        elif operator=="-":
            return a-b
        elif operator=="*":
            return a*b
        elif operator=="/":
            if b==0:
                raise ZeroDivisionError("Division by zero not possible")
            return a/b
        elif operator=="%":
            if b==0:
                raise ZeroDivisionError("Modulo by zero not possible")
            return a%b
        elif operator=="**":
            return a**b
        else:
            raise ValueError("Error Message")
    
         
    except ZeroDivisionError as e:
        return e 
    except ValueError as e:
        return e  
    except TypeError as e:
        return e  
    except Exception as e:
        return e  
# Example Usage:
print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type"
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"
