algoritmo "semnome"
// quanto ganha por hr
// n?meros de hrs trabalhadas no m?s
// desconta 11% imposto de renda
// 8% para INSS
// 5% para sindicato
// sal?rio bruto.
//quanto pagou ao INSS.
//quanto pagou ao sindicato.
//o sal?rio l?quido.
//calcule os descontos e o sal?rio l?quido, conforme a tabela abaixo:
var
gh, ht, bruto, impostorenda, inss, sindicato, liquido:real

inicio
escreval ("Quanto voc? ganha por hora trabalhada?")
leia(gh)

escreval ("Quantas horas voc? trabalhou esse m?s?")
leia(ht)

bruto<-gh*ht
impostorenda<- bruto*0.11
inss<- bruto*0.08
sindicato<-bruto*0.05
liquido<- (bruto-impostorenda-inss-sindicato)

escreval ("Seu salario bruto ?: ",bruto, "R$")
escreval ("Desconto inss ?: ", inss,"R$")
escreval ("Desconto sindicato ?: ", sindicato, "R$")
escreval ("Seu sal?rio liquido ?: ", liquido, "R$")
escreval
escreval("+ Sal?rio Bruto :",bruto," R$")
escreval("- IR (11%) :",impostorenda , "R$")
escreval("- INSS (8%) :",inss,"R$")
escreval("- Sindicato ( 5%) :", sindicato, "R$")
escreval ("= Sal?rio Liquido :", liquido," R$ ")





fimalgoritmo
