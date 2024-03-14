def minimum_change(euros, cents):
    total_cents = euros * 100 + cents
    denominations = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    names = ["Banknotes of 500 euros", "Banknotes of 200 euros", "Banknotes of 100 euros", "Banknotes of 50 euros",
             "Banknotes of 20 euros", "Banknotes of 10 euros", "Banknotes of 5 euros", "Coins of 2 euros",
             "Coins of 1 euro", "Coins of 50 cents", "Coins of 20 cents", "Coins of 10 cents", "Coins of 5 cents",
             "Coins of 2 cents", "Coins of 1 cent"]
    
    for i in range(len(denominations)):
        count = total_cents // denominations[i]
        total_cents -= count * denominations[i]
        print(f"{names[i]}: {count}")

# Input en estilo "9999 99"
input_str = input("")
euros, cents = map(int, input_str.split())

# Llamada a la función con los valores ingresados
minimum_change(euros, cents)