def añoBisiesto(year):
    if year%400 == 0 or (year%4==0 and year%100!=0):
        print("Año bisiesto")
    else:
        print("No es año bisiesto")
añoBisiesto(int(input("ingrese un año: ")))
