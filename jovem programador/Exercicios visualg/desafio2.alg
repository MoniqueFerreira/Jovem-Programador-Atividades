algoritmo "desafio2"

var

nome: caracter
sal, salf: real
desc: real

inicio

escreval ("Digite seu nome: ")
leia (nome)

escreval ("Qual seu sal?rio: ")
leia (sal)

desc<- sal*0.10
salf<- sal-desc

escreva (nome, ", seu sal?rio com o desconto do INSS ?:" , salf, "reais")


fimalgoritmo
