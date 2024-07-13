#script that handles robust division

def safe_divide(numerator,denominator):
    try:
        num = float(numerator)
        den = float(denominator)


        result = num / den
        return f"The result of the division is {result:.1f}"

    except ZeroDivisionError:
        return "Error: Cannot be divided by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."