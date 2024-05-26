#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Resultados da soma e da média aritmética dos valores pares situados na faixa numérica de 50 a 70.

soma = 0
contador = 0
valor = 50
while valor <= 70:
    
    if valor % 2 == 0:
        
        soma = soma + valor # soma += valor
        contador = contador + 1 #contador += 1
        valor = valor + 1 # valor += 1
        
media = soma / contador
print("A soma dos valores pares de 50 a 70 é: ", soma)
print("A média dos valores pares de 50 a 70 é: ", media)