def interval_intersection(a1, b1, a2, b2):
    lower_bound = max(a1, a2)
    upper_bound = min(b1, b2)
    
    if lower_bound > upper_bound:
        return "[]"
    else:
        return "[" + str(lower_bound) + "," + str(upper_bound) + "]"

# Reading input
a1, b1, a2, b2 = map(int, input().split())

# Printing output
print(interval_intersection(a1, b1, a2, b2))
