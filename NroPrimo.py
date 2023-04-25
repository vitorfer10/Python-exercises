nro = int(input("digite um nro: "))
primo = True
for i in range(2, nro):
    resto = nro%i
    print(str(nro) + "%" +str(i)  + "="+ str(resto) )
    if nro%i ==0:
        primo = False
        break

if primo == True:
    print("nro é primo ")
else:
     print("nro nao é primo")