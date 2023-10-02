import os


def soma (a, b):
    return a + b

def multiplica (a, b):
    return a * b

def subtracao (a, b):
    return a - b

def divisao (a, b):
    return a / b


print('='*45)
print(' + - * /   CALCULADORA DO BORBA      + - * /       ')
print('='*45)

print(' Escolha o sinal da operação que deseja realizar o cálculo ou Digite sair para encerrar. ')
print('-'*25)
operadores = str(input(' SOMA(+)\n SUBTRAÇÃO(-)\n DIVISÃO(/)\n MULTIPLICAÇÃO(*)\n'))
os.system("clear")
while operadores != 'sair':
    if operadores != '+' and operadores != '-' and operadores != '/' and operadores != '*':
       print('OPERAÇÃO INVÁLIDA!')
       print('Digite a  operação correta, MACHO !')
    else:
        n1 = float(input('Digite o 1º valor: '))
        print('-'*25)
        n2 = float(input('Digite o 2º valor: '))
        print('-'*25)

        if operadores == '+':
            print('RESULTADO')
            print(soma (n1, n2))

        elif operadores == '-':
            print('RESULTADO')
            print(subtracao (n1, n2))

        elif operadores == '*':
            print('RESULTADO')
            print(multiplica (n1, n2))

        elif operadores == '/':
            print('RESULTADO')
            print(divisao (n1, n2))

    print(' ')
    print('-' *25)
    print(' Escolha o sinal da operação que deseja realizar o cálculo ou Digite sair para encerrar. ')
    print('-'*25)
    operadores = str(input(' SOMA(+)\n SUBTRAÇÃO(-)\n DIVISÃO(/)\n MULTIPLICAÇÃO(*)\n'))
    os.system("clear")
