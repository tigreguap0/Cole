def add_one_second(h, m, s):
    # Increment seconds
    s += 1

    # Handle carry-over to minutes
    if s == 60:
        s = 0
        m += 1

    # Handle carry-over to hours
    if m == 60:
        m = 0
        h += 1

    # Handle midnight (24:00:00)
    if h == 24:
        h = 0

    # Format the output
    formatted_time = f"{h:02d}:{m:02d}:{s:02d}"
    return formatted_time

# Example usage
h, m, s = map(int, input().split())
new_time = add_one_second(h, m, s)
print(new_time)
