#escreva um programa que solicite do usuario dois numeros e a operação que ele deseja efetuar,
#  em seguida mostre na tela o resultado da espressão numeria

n1=float(input('Digite um número: '))
operação=input('Digite a operação que deseja (+, - , * ou /? _')
n2=float(input('Digite um número: '))
if operação == '+':
    print(f'{n1}+{n2}={n1+n2}')
elif operação == '-':
    print(f'{n1}-{n2}={n1-n2}')
elif operação == '*':
    print(f'{n1}*{n2}={n1*n2}')
elif operação == '/':
    print(f'{n1}/{n2}={n1/n2}')
else:
    print('ERRO')

    #resultado = eval(f'{n1}{operação}{n2})
    


