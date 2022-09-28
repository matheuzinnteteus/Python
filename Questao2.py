
nota1 = float(input('Coloque a primeirs média: '))
nota2 = float(input('Coloque a segunda média: '))
nota3 = float(input('Coloque a terceira média: '))

media = (nota1 + nota2 + nota3) / 3
exame = 6 - media

if media < 3:
    print('Reprovado')
elif media >= 3 and media < 6:
    print(f'Você precisa fazer um Exame, presisará de {exame} para ser Aprovado')
elif media >= 6:
    print('Aprovado')

elif media >= 7:
    print('Aprovado')
