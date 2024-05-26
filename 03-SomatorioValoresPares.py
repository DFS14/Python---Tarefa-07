
#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício:  Somatório dos valores pares existentes na faixa de 1 até 500.

soma = 0
i = 1
while i <= 500:
    if i % 2 == 0:
        soma += i
    i += 1
print("A soma dos valores pares de 1 a 500 é: ", soma)