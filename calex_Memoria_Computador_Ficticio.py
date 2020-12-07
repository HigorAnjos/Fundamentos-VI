from sympy import *
#tam = qtdBits
bytes = 8
k = 2**10
m = 2**20
g = 2**30

########################
#preencher
#MP
bit = 8  # * qtd bits endereco
qtd_palavras = 1
e_qtd_bits = 8

#MC
tam_cache = 1*k*bytes  # * tamanho cache
qtd_palavras_cache = 8
#endereco decimal
endereco_mp_decimal = 53 #0x357
#######################


#Bits do sistema
bit = bit
tam_MP = 2**bit
qtd_palavras = qtd_palavras
e_qtd_bits = e_qtd_bits
tam_palavra_dados_bits = qtd_palavras* e_qtd_bits #Inserir valor em bits

print(f"Quantidade de enderecamento da Memoria princital: {tam_MP}bits")
print(f"Cada endereco guarda: {tam_palavra_dados_bits}bits = {tam_palavra_dados_bits/8}bytes")
print(f"Tamanho Memoria princital enderecoBits*palavraBits: {(tam_MP*tam_palavra_dados_bits)}bits = {(tam_MP*tam_palavra_dados_bits)/8}bytes "
      f"= {(tam_MP*tam_palavra_dados_bits)/k/8}kbytes = {(tam_MP*tam_palavra_dados_bits)/m/8}mbytes {(tam_MP*tam_palavra_dados_bits)/g/8}gbytes")



print(f'{log(round(tam_MP),2)} M')

print(f'\ncache ')
tam_cache = tam_cache
print(f'tam = {tam_cache}bits')
qtd_palavras_cache = qtd_palavras_cache
tam_palavra_dados_bits = qtd_palavras_cache * e_qtd_bits #cada palavra tem 2(bytes), e 1 bytes = 8bits, 2bytes = 16bits
qtd_linhas = tam_cache/tam_palavra_dados_bits
print(f'Quantidade de linhas : {qtd_linhas}linhas')

print(f'{log(round(qtd_linhas),2)} L  {log(round(qtd_palavras_cache),2)} D')




print(f'\nEndereco')
endereco_mp_decimal = endereco_mp_decimal
print(f'Vai para linha: {endereco_mp_decimal%qtd_linhas} da cache')


