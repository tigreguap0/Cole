def find_intersection(a1, b1, a2, b2):
    # Comprovem si els intervals són iguals
    if a1 == a2 and b1 == b2:
        return '=', [a1, b1]
    # Comprovem si el primer interval està dins del segon
    elif a1 >= a2 and b1 <= b2:
        return '1', [a1, b1]
    # Comprovem si el segon interval està dins del primer
    elif a2 >= a1 and b2 <= b1:
        return '2', [a2, b2]
    # Comprovem si hi ha intersecció
    elif b1 >= a2 and b2 >= a1:
        return '?', [max(a1, a2), min(b1, b2)]
    else:
        return '?', []

# Entrada
a1, b1, a2, b2 = map(int, input().split())

# Sortida
relation, intersection = find_intersection(a1, b1, a2, b2)
print(relation, ',', '[' + str(intersection[0]) + ',' + str(intersection[1]) + ']' if intersection else '[]')
