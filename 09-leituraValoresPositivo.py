#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado


numero = int(input("Digite um número inteiro positivo: "))
maior = numero
menor = numero

while numero >= 0:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
        
    numero = int(input("Digite outro número inteiro positivo: "))
    
print("O maior número informado foi: ", maior)
print("O menor número informado foi: ", menor)

