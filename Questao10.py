print('1ª DATA')
dia1 = int(input('Insira o dia: '))
mes1 = int(input('Insira o mês: '))
ano1 = int(input('Insira o ano: '))

print('2ª DATA')
dia2 = int(input('Insira o dia: '))
mes2 = int(input('Insira o mês: '))
ano2 = int(input('Insira o ano: '))


if ano1 > ano2:
        print(f'A maior data é {dia1}.{mes1}.{ano1}')
elif ano2 > ano1:
        print(f'A maior data é {dia2}.{mes2}.{ano2}')


if mes1 > mes2:
    if ano1 > ano2:
        print(f'A maior data é {dia1}.{mes1}.{ano1}')
    elif ano2 > ano1:
        print(f'A maior data é {dia2}.{mes2}.{ano2}')

elif mes2 > mes1:
    if ano1 > ano2:
        print(f'A maior data é {dia1}.{mes1}.{ano1}')
    elif ano2 > ano1:
        print(f'A maior data é {dia2}.{mes2}.{ano2}')


if dia1> dia2:
    if ano1 > ano2:
        print(f'A maior data é {dia1}.{mes1}.{ano1}')
    elif ano2 > ano1:    
        print(f'A maior data é {dia1}.{mes1}.{ano2}')

elif dia2 > dia1:
    if ano1 > ano2:
        print(f'A maior data é {dia2}.{mes1}.{ano1}')
        
    elif ano2 > ano1:
        print(f'A maior data é {dia2}.{mes2}.{ano2}')
        