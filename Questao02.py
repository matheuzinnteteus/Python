pesoSaco = float(input("Digite o peso do saco de ração: "))
gramas = float(input("Digite a quantidade de ração dada para cada gato: "))

pesoFinal = pesoSaco - (gramas*2)/5

print(f"Sobrará {pesoFinal} quilogramas após 5 dias")