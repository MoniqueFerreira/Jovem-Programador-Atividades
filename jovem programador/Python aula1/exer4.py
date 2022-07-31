usuario='Monique'
senha='123'

usuariologin=input('Digite o usuario:_')
senhalogin=input('Digite a senha:_')

if usuariologin!= usuario:
    print('usuario incorreto')
elif senhalogin!= senha:
    print('Senha incorreta')
    print('Acesso Negado! ')
else:
    print('Acesso Autorizado!')