#Gerador de senha
from random import choice

tamanho=int(input("Quantos digitos vc quer em sua senha? "))

caracteres= 'a''b''c''d''e''f''g''h''i''j''k''i''j''l''m''n''o''p''q''r''s''t''u''v''x''z''1''2''3''4''5''6''7''8''9''0''!''@''#''$''%''¨''&''¨''*'
s=""
for i in range(tamanho):
    s +=choice(caracteres)
print(f"Sua senha é {s} ")



# Choices() em Python. O método choices() retorna vários elementos aleatórios da lista com 
# substituição. Você pode pesar a possibilidade de cada resultado com o weights parâmetro ou
#  o cum_weights parâmetro. Os elementos podem ser uma string, um intervalo, uma lista, uma 
#  tupla ou qualquer outro tipo de sequência