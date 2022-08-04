# numeros = []
# while True:
#     numero = int(input('Digite um numero. | 0 para sair. '))
#     if numero == 0:
#         break
#     else:
#         numeros.append(numero)

# print(f'O maior número é: {numeros.sort()}')
# print(f'O menor número é: {min(numeros)}')

# contador = 0

# p1 = str(input('Telefonou para a vítima?')).lower()
# if p1 == 'sim':
#     contador += 1
# p2 = str(input('Esteve no local do crime?')).lower()
# if p2 == 'sim':
#     contador += 1
# p3 = str(input('Mora perto da vítima?')).lower()
# if p3 == 'sim':
#     contador += 1
# p4 = str(input('Devia para a vítima?')).lower()
# if p4 == 'sim':
#     contador += 1
# p5 = str(input('Já trabalhou com a vítima?')).lower()
# if p5 == 'sim':
#     contador += 1


# if contador < 2:
#     print('Inocente')
# elif contador == 2:
#     print('Suspeita')
# elif contador == 3 or contador == 4:
#     print('Cúmplice')
# elif contador == 5:
#     print('Assassino')            