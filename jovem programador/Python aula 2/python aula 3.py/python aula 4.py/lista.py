#crie 3 listas
   #uma com 10 numeros
   #uma com numeros pares
   #uma com numeros impares
#em seguida crie um programa que faça essa distribuição dos elementos

numero=[0,1,2,3,4,5,6,7,8,9]
par = []
impar=[]

for i in range(10):
    resto=(numero[i]%2)
    if resto==0:
        par.append(numero[i])
    else:
        impar.append(numero[i])
    
print(f'pares: {par}\n impares: {impar}')