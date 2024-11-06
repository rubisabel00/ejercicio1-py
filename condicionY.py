Num1 = int(input("digite el primer valor "))
Num2 = int(input("digite el segundo valor "))
Num3 = int(input("digite el tercer valor "))

if Num1 > Num2 and Num1 > Num3:
    print(Num1, "es mayor que ", Num2, " y ", Num3)
elif Num2 > Num1 and Num2 > Num3:
    print(Num2, " es mayor que ", Num1, " y ", Num3)
else:
    print(Num3, "es mayor que ", Num1 , " y ", Num2)

