def division_and_remainder(a, b):
    d = a // b  # Integer division
    r = a % b   # Remainder
    return d, r

# Read input values
a, b = map(int, input().split())

# Ensure b is greater than 0
if b <= 0:
    print("Error: b must be greater than 0")
else:
    # Calculate division and remainder
    d, r = division_and_remainder(a, b)
    # Print the result
    print(d, r)
