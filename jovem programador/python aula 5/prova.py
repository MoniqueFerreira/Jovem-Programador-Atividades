#Crie um VALIDADOR DE CPF

# O CPF é formado por 11 dígitos numéricos que seguem a máscara "###.###.###-##", 
# a verificação do CPF acontece utilizando os 9 primeiros dígitos e, com um cálculo simples,
#  verificando se o resultado corresponde aos dois últimos dígitos (depois do sinal "-").
      #Vamos usar como exemplo, um CPF fictício "529.982.247-25".

# cpf=int(input("digite seu cpf: "))
# lista=[cpf]
# for i in range(11,0):
#     lista1[1*i]
    
# print(lista)


# from Cpf import Cpf

# cpf = "52998224725"
#objeto_cpf = Cpf(cpf)

n= int(input("Digite o cpf: "))
cpf=[n]
qtdd=len(n)
if qtdd ==11:
    for cpf in range[0,10]:
        n1=cpf[0]
        n2=cpf[1]
        n3=cpf[2]
        n4=cpf[3]
        n5=cpf[4]
        n6=cpf[5]
        n7=cpf[6]
        n8=cpf[7]
        n9=cpf[8]
        dig1=cpf[9]
        dig2=cpf[10]
        
        n1= cpf[0*10]
        n2 = cpf[1*9]
        n3 = cpf[2*8]
        n4 = cpf[3*7]
        n5 = cpf[4*6]
        n6 = cpf[5*5]
        n7 = cpf[6*4]
        n8= cpf[7*3]
        n9=cpf[8*2]


soma=n1+n2+n3+n4+n5+n6+n7+n8+n9
mult=(soma)/11
if mult % 2 ==dig1:

    print('primeira parte valida')
print(dig1)


