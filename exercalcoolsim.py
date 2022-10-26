alcool = float(input("digite o valor do alcool: "))
gasolina = float(input("digite o valor da gasolina: "))
formula = alcool/gasolina

print("resultado do calculo: ",formula)
if formula <= 0.70:
    print("compensa alcool")
else:
    print("compensa gaolina")









