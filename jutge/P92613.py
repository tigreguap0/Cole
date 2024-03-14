import math

def round_numbers(x):
    floor_x = math.floor(x)
    ceil_x = math.ceil(x)
    rounded_x = ceil_x if x - floor_x >= 0.5 else floor_x
    print(floor_x, ceil_x, rounded_x)

# Read the input
x = float(input())

# Call the function with the input value
round_numbers(x)