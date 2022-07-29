algoritmo "semnome"
// quanto ganha por hr
// números de hrs trabalhadas no mês
// desconta 11% imposto de renda
// 8% para INSS
// 5% para sindicato
// salário bruto.
//quanto pagou ao INSS.
//quanto pagou ao sindicato.
//o salário líquido.
//calcule os descontos e o salário líquido, conforme a tabela abaixo:
var
gh, ht, bruto, impostorenda, inss, sindicato, liquido:real

inicio
escreval ("Quanto você ganha por hora trabalhada?")
leia(gh)

escreval ("Quantas horas você trabalhou esse mês?")
leia(ht)

bruto<-gh*ht
impostorenda<- bruto*0.11
inss<- bruto*0.08
sindicato<-bruto*0.05
liquido<- (bruto-impostorenda-inss-sindicato)

escreval ("Seu salario bruto é: ",bruto, "R$")
escreval ("Desconto inss é: ", inss,"R$")
escreval ("Desconto sindicato é: ", sindicato, "R$")
escreval ("Seu salário liquido é: ", liquido, "R$")
escreval
escreval("+ Salário Bruto :",bruto," R$")
escreval("- IR (11%) :",impostorenda , "R$")
escreval("- INSS (8%) :",inss,"R$")
escreval("- Sindicato ( 5%) :", sindicato, "R$")
escreval ("= Salário Liquido :", liquido," R$ ")





fimalgoritmo
