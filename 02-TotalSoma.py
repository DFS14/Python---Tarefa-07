#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Total da soma (cem primeiros números inteiros)


soma = 0
valor = 1
while valor <=100:
    soma = soma + valor  # ou soma +=valor
    valor = valor + 1    # ou valor += 1
    print("A soma dos cem primeiros números inteiros é: ", soma)
    