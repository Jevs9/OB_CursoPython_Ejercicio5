def añoBisiesto(year):
    comp1 = year % 4
    comp2 = year % 100
    comp3 = year % 400
    if comp2 == 0 and comp3 != 0:
        print("No es año bisiesto")
    elif comp3 == 0 or comp1 == 0:
        print("Es año bisiesto")
    elif comp1 != 0:
        print("No es año bisiesto")
añoBisiesto(int(input("ingrese un año: ")))
