#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Tabuada de multiplicar

numero = int(input("Digite um número: "))

valor = 1
while valor <= 10:
    print(numero, "x", valor, "=", numero * valor)
    valor += 1