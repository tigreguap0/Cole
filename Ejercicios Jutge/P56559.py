def interval_relation(a1, b1, a2, b2):
    if a1 == a2 and b1 == b2:
        return '='
    elif a1 >= a2 and b1 <= b2:
        return '1'
    elif a2 >= a1 and b2 <= b1:
        return '2'
    else:
        return '?'

# Input
a1, b1, a2, b2 = map(int, input().split())

# Output
print(interval_relation(a1, b1, a2, b2))
        