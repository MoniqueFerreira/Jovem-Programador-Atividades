#Faça um Programa que leia três números e mostre o maior deles.
n1=int(input('Digite um número:__'))
n2=int(input('Digite o segundo número:__'))
n3=int(input('Digite o terceiro número:__'))

if n1 > n2 and n1 > n3:
    print(f'{n1} é maior que {n2} e que {n3}')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é maior que {n1} e que {n3}')
elif n3 > n1 and n3 > n2:
    print(f'{n3} é maior que {n1} e {n2}')
