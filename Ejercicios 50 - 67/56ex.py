import time

#PRINTS EL TIME ES PARA QUE QUEDE MAS BONITO

print("MENÚ")
time.sleep(0.3)
print("A. Bocadillo de calamares - 9 €")
time.sleep(0.3)
print("B. Bocadillo de chistorra - 4.5 €")
time.sleep(0.3)
print("C. Bikini de jamón - 2.5 €")
time.sleep(0.3)
print("COMPAÑAMIENTO")
time.sleep(0.3)
print("D. Patatas finas - 1.5 €")
time.sleep(0.3)
print("E. Patatas gruesas - 1.75 €")
time.sleep(0.3)
print("F. Patatas rústicas - 2 €")
time.sleep(0.3)
print("BEBIDAS")
time.sleep(0.3)
print("G. Monster - 2 €")
time.sleep(0.3)
print("H. Acuarius - 1.5 €")
time.sleep(0.3)
print("I. Agua - 1 €") 

#PRECIOS DE LOS PRODUCTOS

A = 9
B = 4.5
C = 2.5
D = 1.5
E = 1.75
F = 2
G = 2
H = 1.5
I = 1

total_pagar = 0

#AQUI ES CUANDO TE PIDE LOS PRODUCTOS Y LE PIDES LA CANTIDAD

while True:
    num_pedidos = 0
    total_pedido = 0
    productos_pedidos = [] 

    while True:
        opcion = input("Introduce el número de producto (0 para finalizar pedido): ")
        if opcion == "0":
            break

        cantidad = int(input("Introduce la cantidad: "))

        
        productos_pedidos.append((opcion, cantidad))

    num_pedidos += 1
    total_pagar += total_pedido

    # LO DE ABAJO QUEDA TAL QUE ASI
    # A x 3 = 27
    # I x 1 = 1

    print("Resumen del pedido:")
    print(f"Número de pedidos realizados: {num_pedidos}")
    
    # CALCULOS

    for producto, cantidad in productos_pedidos:
        precio_unitario = globals()[producto]
        subtotal_producto = precio_unitario * cantidad
        print(f"{cantidad} x {producto}: {subtotal_producto} €")
        total_pedido += subtotal_producto

    print(f"Total a pagar: {total_pedido} €")
    total_iva = total_pedido * 0.10
    print(f"Total con IVA (10%): {total_pedido + total_iva} €")

    if 20 <= total_pedido <= 30:
        descuento = total_pedido * 0.05
    elif total_pedido > 30:
        descuento = total_pedido * 0.15
    else:
        descuento = 0

    total_con_descuento = total_pedido - descuento
    print(f"Descuento aplicado: {descuento} €")
    print(f"Total con descuento: {total_con_descuento} €")
    
    #repetir el programa 
    
    otra_vez = input("\n¿Quieres gestionar otro pedido? (s/n): ")
    if otra_vez.lower() != "s":
        break

#PRINT DE EL TOTAL DE PAGAR ETC

print("Resumen final:")
print(f"Número total de pedidos realizados: {num_pedidos}")
print(f"Total a pagar por todos los pedidos: {total_pagar} €")
