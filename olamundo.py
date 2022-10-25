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

