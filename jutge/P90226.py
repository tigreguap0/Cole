def compute_banknotes_and_coins(eur, cent):
    # Define the available denominations
    denominations = [
        (500, "euros"), (200, "euros"), (100, "euros"),
        (50, "euros"), (20, "euros"), (10, "euros"),
        (5, "euros"), (2, "euros"), (1, "euro"),
        (50, "cents"), (20, "cents"), (10, "cents"),
        (5, "cents"), (2, "cents"), (1, "cent")
    ]

    total_amount = eur * 100 + cent

    count_dict = {denom: 0 for _, denom in denominations}

    for value, denom in denominations:
        count = total_amount // value
        total_amount -= count * value
        count_dict[denom] = count

    # Print the results
    for value, denom in denominations:
        print(f"Banknotes of {value} {denom}: {count_dict[denom]}")

eur, cent = map(int, input().split())
compute_banknotes_and_coins(eur, cent)
