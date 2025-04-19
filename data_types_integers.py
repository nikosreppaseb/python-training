import math

age = 30

print(type(age))
#Integer Type
print(type(age)) #<class 'int'>
#Integer Length
print(len(str(age))) #2
#Integer Indexing
print(str(age)[0]) #3  

# Convert to string once and store result
age_str = str(age)

def get_digit(num_str: str, position: int) -> str:
    """Safely get a digit at the specified position."""
    try:
        return num_str[position]
    except IndexError:
        return f"Error: Position {position} is out of range for number {num_str}"

# Get individual digits
print(get_digit(age_str, 1))  # Second digit: 0

# Demonstrate string slicing with better comments
print(age_str[0:1])  # Extract first digit: 3
print(str(age)[1:2]) #0
print(str(age)[:1]) #3
print(str(age)[1:]) #0

print(age.numerator) #3
print(age.denominator) #1
print(age.real) #30
print(age.imag) #0