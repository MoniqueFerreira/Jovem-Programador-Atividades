algoritmo "Idade para tirar a carteira"

var

nome:caracter
idade:inteiro
falta, passou, igual:inteiro
inicio

escreval ("Qual o seu nome?")
leia (nome)

escreval ("Qual sua idade?")
leia (idade)


falta<- 18- idade
passou<- idade-18


se idade > 18 entao
  escreva (nome, ", você já pode tirar a carteira a " , passou, " anos!")
fimse


se idade < 18 entao
  escreva (nome, ", ainda faltam" , falta, " anos pra você tirar a carteira!" )
  
fimse

se idade = 18 entao
    escreva ("Você já pode tirar sua carteira")
fimse






fimalgoritmo
