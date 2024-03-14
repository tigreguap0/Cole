anio = int(input(""))
if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
else:
    print("NO")