print('Menu de Opções:')
print('  1. Somar dois números')
print('  2. Raíz quadrada de um número')
opc = int(input('Digite sua opção: '))

if opc == 1:
    num1 = int(input('Insira o úmero: '))
    num2 = int(input('Insira outro número: '))

    resultado = num1 + num2
    print(f'A soma foi {resultado} ')

import math
if opc == 2:
    num = int(input('Insira o número: '))

    print(f'A raíz quadrada é {math.sqrt(num)} ')




