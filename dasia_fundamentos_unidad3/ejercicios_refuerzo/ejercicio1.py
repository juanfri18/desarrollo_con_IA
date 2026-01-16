temperatura=float(input("dime un tempertura:"))
unidad_origen=input("Unidad de origen (C/F/K):").upper()
unidad_destino=input("Unidad de destino (C/F/K):").upper()
if(unidad_origen=="C" and unidad_destino=="F"):
    temperatura_conver=(temperatura*(9/5))+32
    print(temperatura_conver)
elif(unidad_origen=="C" and unidad_destino=="K"):
    temperatura_conver= temperatura + 273.15
    print(temperatura_conver)
elif(unidad_origen=="F" and unidad_destino=="C"):
    temperatura_conver= (temperatura - 32)*(5/9)
    print(temperatura_conver)
else:
    print(f"No has escrito una opcion correcta")