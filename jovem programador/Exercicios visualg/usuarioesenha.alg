algoritmo "  "



var
nome, nome2:caracter
senha, senha2: caracter

inicio
escreval ("Cadastre-se usando seu Nome e Definindo uma senha!")
 escreval ("Qual seu nome?")
 leia (nome)
 
 escreval ("Digite uma senha!")
 leia(senha)
 
escreval ("Vamos Fazer seu Login")

escreval("Digite seu nome!")
leia(nome2)

escreval ("Digite sua senha cadastrada")
leia(senha2)

se (senha = senha2)e (nome = nome2) entao
   escreva (" Conectado")
fimse

se (senha <> senha2) ou (nome <> nome2) entao
   escreva (" Não Conectado")
fimse



fimalgoritmo
