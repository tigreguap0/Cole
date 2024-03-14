def compute_intersection(a1, b1, a2, b2):
    lower_bound = max(a1, a2)
    upper_bound = min(b1, b2)
    
    if lower_bound <= upper_bound:
        return [lower_bound, upper_bound]
    else:
        return "[]"

a1, b1, a2, b2 = map(int, input().split())

print(compute_intersection(a1,b1,a2,b2))
