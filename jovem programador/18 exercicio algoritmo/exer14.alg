algoritmo "semnome"
//
// jo?o pescador
// 50kg de peixes ? o limite pra n?o pagar multa
//paga 4 reais por kilo excedido
var
p,excesso, multa: real

inicio
escreval("Quantos kilos de peixe? ")
leia(p)

excesso<- p-50
multa<-excesso*4

escreval ( "Jo?o tem que pagar multa de:", multa, " reais, pelo peso excedido")




fimalgoritmo
