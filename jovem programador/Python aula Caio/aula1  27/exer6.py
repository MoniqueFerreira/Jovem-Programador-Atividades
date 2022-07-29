#Pergunte o sexo da pessoa, se for masculino mostre a mensagem 
# "você se aposenta com65 anos" se for mulher mostre a mensagem 
# "Você pode se aposentar com 60 anos"

sexo=input('Qual seu sexo? Digite M para masculino e F para Feminino: \n')
sexo=(sexo.upper())

if sexo == "M":
    print('Você pode se aposentar com 65 anos de idade')
elif sexo=="F":
    print('Você pode se aposentar com 60 anos de idade')
else:
    print('Opção invalida, Digite M ou F')

    

