algoritmo "desafio3"
    //escrever um programa que pede 2 valores, calculo de área
    //da hipotenusa de um valor
   // cateto A e cateto B
    //Hipotenusa é = A² + b²
var
va1, va2,h, hipo: real

inicio

escreval ("digite o primeiro valor")
leia (va1)

escreval ("digite o segundo valor")
leia (va2)

h<- (va1^2+va2^2)
hipo<- raizq(h)

escreva ("O valor da hipotenusa é:" , hipo)






fimalgoritmo
