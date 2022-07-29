algoritmo "Aposentadoria"



var

nome:caractere
sexo:caractere
idade:inteiro
idF, idM: inteiro



inicio
escreval ( "Qual é seu nome?")
leia (nome)

escreval ("Qual seu sexo? (F/M) digite F para Feminino ou M para Masculino!")
leia (sexo)

escreval ("Qual sua idade?")
leia (idade)

idF<- 60-idade
idM<- 65-idade


se (sexo = "f") ou (sexo="F") entao
   escreva (" Faltam para se aposentar" ,idF, " anos!")
   
 fimse
 
se (sexo = "m") ou (sexo = "M") entao
   escreva ("Faltam para se aposentar" ,idM , " anos!")
fimse












fimalgoritmo
