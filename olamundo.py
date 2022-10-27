#coletando dados do usuario
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))
imc= peso/altura**2
print("-"* 30)
print("os dados coletados foram: ")
print("seu nome: ",nome)
print("idade: ",idade," anos")
print("altura: ",altura)
print("peso:  ",peso, " kgs")
print("seu IMC = ",imc)



if imc < 16:
    print("Magreza grave!")
elif imc < 18.5:
    print("magreza leve")
elif imc < 24.9:
    print("peso normal")
elif imc < 29.9:
    print("excesso de peso")
elif imc < 34.9:
    print("obesidade classe1")
elif imc < 39.9:
    print("obesi.classe2")
else:
     print("obesso alertamaximo")
