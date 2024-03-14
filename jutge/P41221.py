var1=input()
lista1=var1.split()
while len(lista1)!=3:
    if len(lista1)==1:
        var2=input()
        if var2.isnumeric():
            lista1.append(var2)
    if len(lista1)==2:
        var3=input()
        if var3.isnumeric():
            lista1.append(var3)

var4=int(lista1[0])+int(lista1[1])+int(lista1[2])
print(var4)