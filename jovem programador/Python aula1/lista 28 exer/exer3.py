#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo=input('Digite F para Feminino ou M para Masculino:_ ').lower()
while sexo != 'f' or sexo != 'm':
    print('Sexo Inválido Digite novamente ')
    sexo=input('Digite F para Feminino ou M para Masculino:_ ').lower()
if sexo == 'f':
    print('Sexo Feminino')
elif sexo == 'm':
    print('Sexo Masculino')
