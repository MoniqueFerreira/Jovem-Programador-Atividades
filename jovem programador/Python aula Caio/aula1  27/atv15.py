#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
#descontados 11% para o Imposto de Renda,
#8% para o INSS e 
#5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

ganha_por_hora= int(input("Quanto você ganha por hora? : \n"))
numero_de_hora= int(input("Quantas horas você trabalhou?: \n"))
bruto=ganha_por_hora*numero_de_hora
impderenda=bruto*0.11
inss=bruto*0.08
sindicato=bruto*0.05
liquido=bruto-inss-sindicato-impderenda

print('\n Bruto: {} \n desconto inss: {}\n desconto sindicato {}\n desconto imposto de renda: {}\n Salário liquido: {}'.format(bruto,inss, sindicato, impderenda, liquido))


