# Function to calculate the area of a rectangle
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
    length(float): The length of the rectangle
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width

# Function to greet the user
def greet_user(name):
    """
    Print a greeting message to the user.

    Args:
    name (str): The name of the user.
    """
    print(f"Hello, {name}! Welcome to the program.")

# Main script    
name= input("Enter your name: ") # Get the user's name
greet_user(name) # Call the greet_user function

try:
    length= float(input ("Enter the length of the rectangle: ")) #Input rectangle length
    width = float(input("Enter the width of the rectangle: "))  #Input rectangle width
    area = calculate_area(length, width)  # Call calculate_area function
    print(f"The area of the rectangle is {area}.")

except ValueError:
    print("Error: Please enter valid numbers for length and width.")