def convert_seconds_to_hms(total_seconds):
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return hours, minutes, seconds

total_seconds = int(input())
hours, minutes, seconds = convert_seconds_to_hms(total_seconds)
print(f"{hours} {minutes} {seconds}")
