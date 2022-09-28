num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
num3 = int(input('Insira o terceiro número: '))
num4 = int(input('Insira o quarto número aleatório: '))

if num4 > num3:
    print(f'A ordem decrescente dos números é {num1},{num2},{num3} e {num4} ')

if num4 > num2 and num3 > num4:
    print(f'A ordem decrescente dos números é: {num3},{num4},{num2} e {num1} ')

if num4 > num1 and num2 > num4:
    print(f'A ordem decrescente dos números é: {num4},{num2},{num3} e {num1} ')

if num4 > num1:
    print(f'A ordem decrescente dos números é: {num3},{num2},{num1} e {num4} ')


    