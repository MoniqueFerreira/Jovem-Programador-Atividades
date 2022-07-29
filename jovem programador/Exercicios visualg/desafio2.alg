algoritmo "desafio2"

var

nome: caracter
sal, salf: real
desc: real

inicio

escreval ("Digite seu nome: ")
leia (nome)

escreval ("Qual seu salário: ")
leia (sal)

desc<- sal*0.10
salf<- sal-desc

escreva (nome, ", seu salário com o desconto do INSS é:" , salf, "reais")


fimalgoritmo
