#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Leitura de 10 valores numéricos e apresente no final o total do somatório e a média aritmética dos valores lidos.

soma = 0
valor = 1
while valor <= 10:
    numero = int(input("Digite o número: "))
    soma += numero
    valor += 1
    
media = soma / 10
print("A soma é: ", soma)
print("A média é: ", media)

