nota1 = float(input('Acrescente a nota do TDL: '))
nota2 = float(input('Acrescente a nota da AvaliaçãoSemestral: '))
nota3 = float(input('Acrescente a nota do Exame: '))

mediaPonderada = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

if mediaPonderada < 5:
    print('Conceito E')
else:
    if mediaPonderada < 6:
        print('Conceito D')
    else:
        if mediaPonderada < 7:
            print('Conceito C')
        else:
            if mediaPonderada < 8:
                print('Conceito B')
            else:
                print('Conceito A')
