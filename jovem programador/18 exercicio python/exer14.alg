algoritmo "semnome"
//
// joão pescador
// 50kg de peixes é o limite pra não pagar multa
//paga 4 reais por kilo excedido
var
p,excesso, multa: real

inicio
escreval("Quantos kilos de peixe? ")
leia(p)

excesso<- p-50
multa<-excesso*4

escreval ( "João tem que pagar multa de:", multa, " reais, pelo peso excedido")




fimalgoritmo
