#escreva um programa que peça para o usuario digitar quantos numeros ele quiser,
#  adicione todos esse números a uma lista e informe na tela o maior numero e o menor

#faça exercicio 14 da lista de python 


lista=[]
while True:
    n=int(input('Digite um número: '))
    if n == '':
        break
    if n != '':
        lista.append(n)
        lista.sort(n)
        print(lista)
        print(lista[0,-1])
    



