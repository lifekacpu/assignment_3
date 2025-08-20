
                   #task1



def factorial(n):
    """
    Calculate the factorial of a number using a loop.
    
    Args:
        n (int): The number to calculate factorial for
    
    Returns:
        int: The factorial of the number
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get input from user
try:
    num = int(input("Enter a number: "))
    
    # Calculate and display factorial
    result = factorial(num)
    print(f"Factorial of {num} is: {result}")
    
except ValueError:
    print("Please enter a valid integer!")




                      #task2


    import math

def main():
    """
    Calculate and display mathematical operations using the math module.
    """
    try:
        # Get input from user
        number = float(input("Enter a number: "))
        
        # Calculate the required values
        square_root = math.sqrt(number)
        logarithm = math.log(number)  # Natural logarithm (base e)
        sine = math.sin(number)       # Sine of the number in radians
        
        # Display the results
        print(f"Square root: {square_root}")
        print(f"Logarithm: {logarithm}")
        print(f"Sine: {sine}")
        
    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()