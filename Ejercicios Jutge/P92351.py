def division_and_remainder(a, b):
    d = a // b
    r = a % b
    return d, r

a, b = map(int, input().split())
d, r = division_and_remainder(a, b)
print(d, r)