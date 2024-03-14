def add_one_second(h, m, s):
    s += 1

    if s == 60:
        s = 0
        m += 1

    if m == 60:
        m = 0
        h += 1

    if h == 24:
        h = 0

    formatted_time = f"{h:02d}:{m:02d}:{s:02d}"
    return formatted_time

h, m, s = map(int, input().split())
new_time = add_one_second(h, m, s)
print(new_time)
