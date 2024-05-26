#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Programa que possibilite calcular a área total de uma residência

areaTotal = 0
continuar = "SIM"

while continuar.upper() == "SIM":
    
    nomeDoComodo = (input ("Digite o cômodo: "))
    largura = float(input("Digite a largura do cômodo: "))
    comprimento = float(input("Digite o comprimento do cômodo: "))
    
    area = largura * comprimento
   
    print(nomeDoComodo, "tem área de", area, "m²")
    areaTotal += area
    continuar = input("Deseja continuar calculando novos cômodos? (SIM/NAO) ")
    
print("A área total da residência é: ", areaTotal, "m²")


