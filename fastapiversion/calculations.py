def calculate(a: int|float = None, b: int|float = None, operation: str = "+") -> str | int | float:
    
    result = ""
    
    if a is not None and b is not None:
        match operation:
            case "+":
                result = a + b
                
            case "-":
                result = a - b
                
            case "*":
                result = a * b
                
            case "/":
                result = a / b
                
            case "//":
                result = a // b
            
            case "**":
                result = a ** b

    return result
    