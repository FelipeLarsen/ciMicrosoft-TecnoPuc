#VARIAVEIS
precoEnergetico = 4.50
valorIcms = 0.18
valorIpi = 0.04
valorPis = 0.0186
valorCofins = 0.0854

#FUNCOES
def calculaIcms(totalMercadoria):
	icms = totalMercadoria * valorIcms
	return icms

def calculaIpi(totalMercadoria):
	ipi = totalMercadoria * valorIpi
	return ipi

def calculaPis(totalMercadoria):
	pis = totalMercadoria * valorPis
	return pis

def calculaCofins(totalMercadoria):
	cofins = totalMercadoria * valorCofins
	return cofins


def cadastraVenda():
	nomeEmpresa = input('Digite o nome da empresa: ')
	quantidade = input('Digite a quantidade desejada:')
	arrayEmpresa.append(nomeEmpresa)
	arrayQuantidade.append(quantidade)
	totalMercadoria = precoEnergetico * quantidade
	arrayTotalMercadoria.append(totalMercadoria)
	arrayIcms.append(calculaIcms(totalMercadoria))
	arrayIpi.append(calculaIpi(totalMercadoria))
	arrayPis.append(calculaPis(totalMercadoria))
	arrayCofins.append(calculaCofins(totalMercadoria))
	print('Venda cadastrada com sucesso!')

def relatorio():
	for i in arreyEmpresa:
		print('Cliente: ', arreyEmpresa[i])
		print('ICMS: R$ ', arrayIcms[i])
		print('IPI: R$ ', arrayIpi[i])
		print('PIS: R$ ', arrayPis[i])
		print('COFINS: R$ ', arrayCofins[i])
		total = arrayTotalMercadoria[i] + arrayIcms[i] + arrayIpi[i] + arrayPis[i] + arrayCofins[i]
		print('Total: R$ ', arrayIcms[i])
		print('=================================')
		totalImpostos = sum(arrayIcms) + sum(arrayIpi) + sum(arrayPis) + sum(arrayCofins)
		print('Total impostoss: R$', totalImpostos)
		print('Total Mercadoria: R$', sum(arrayTotalMercadoria))
		print('Total Geral: R$ ', totalImpostos + sum(arrayTotalMercadoria))

#PROGRAMA
arrayEmpresa = []
arrayQuantidade = []
arrayTotalMercadoria = []
arrayIcms = []
arrayIpi = []
arrayPis = []
arrayCofins = []


menu = '''
=================================
MENU
=================================
0-    Finaliza
1-    Cadastra Venda
2-    Relatorio

=================================
Escolha:
'''

while True:

    escolha = input(menu)
    if escolha == '1':
        cadastraVenda()
    elif escolha == '2':
        relatorio()
    elif escolha == '0':
        break
