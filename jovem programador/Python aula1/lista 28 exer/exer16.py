#Faça um programa que calcule as raízes de uma equação do segundo grau,
#  na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
#  informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa nã
# o deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre
#  o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a=int(input('Digite Valor de A: '))
if a !=0:
    b=int(input('Digite Valor de B: '))
    c=int(input('Digite Valor de C: '))

    delta= (b**2)- 4*a*c
    x1= (-b+ delta**(1/2))/ (2*a)
    x2= (-b- delta**(1/2))/ (2*a)


if delta==0:
    print("ERRO!!! Equação do segundo grau o A não pode ser igual a 0 ")
elif delta < 0:
    print(f'Delta deu um valor negativo, A equação não possui raizes reais')
elif delta > 0:
    print (f' as raizes são x1={x1}, x2={x2}')

