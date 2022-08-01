import random

pc = random.randint(1, 100)
resposta_certa = pc
contador = 0

numero = int(input("Adivinhe o número: "))
print(pc)
while True:
    contador += 1
    if contador >= 5:
        print('Você perdeu!')
        break
    if numero == pc:
        print(f' {pc} é o número certo. Você acertou!!')
        break

    elif numero < pc:
        numero=int(input('O número é maior'))
    elif numero > pc:
        numero=int(input('O número é menor'))
    
