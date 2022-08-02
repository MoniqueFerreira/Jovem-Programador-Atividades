#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caractere;
#Idade: entre 0 e 70;
#Salário maior que zero;
#sexo 'f' ou 'm';
#estado civil: 's' , 'c' , 'v' , 'd';

nome= input('Digite seu nome: ')

while  len(nome) <= 3:

    print('Seu nome deve conter mais de 3 caractere!')
    nome= input('Digite seu nome: ')


idade= int(input('Digite sua idade: '))
while idade < 0 or idade >70:

    print('Sua idade tem que ser entra 0 a 70 anos ')
    idade= int(input('Digite sua idade: '))


salario=float(input('Digite seu salário: '))
while salario <= 0:
    print('o salário tem que ser maior que R$0,00')
    salario= float(input('Digite seu salário: '))



sexo= input('Qual seu sexo (f/m)? ')
sexo1= sexo.lower()
nome1=len(nome)
while sexo != 'f' and sexo != 'm':
    print('ERRO! digite f ou m conforme seu sexo')
    sexo= input('Qual seu sexo (f/m)? ')


estado_civil=input('Qual seu estado civil? (s/c/v/d)? ').lower()


while estado_civil != 's' or estado_civil != 'c' or estado_civil != 'v' or estado_civil != 'd':

    print('Tente novamente seu estado civil')
    estado_civil=input('Qual seu estado civil? (s/c/v/d)? ').lower()
    if estado_civil == 's' or estado_civil== 'c' or estado_civil == 'v' or estado_civil == 'd':
        print('Cadastrado com sucesso!')






