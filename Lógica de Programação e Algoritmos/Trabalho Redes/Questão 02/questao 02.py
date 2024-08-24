print('Bem Vindo a Lanchonete de Alisson de Souza Rodrigues')

print('=' * 20 + ' CARDÁPIO ' + '=' * 20)
print('| Código |' + '         Descrição         ' + '| Valor (R$) |')
print('|  100   |' + '      Cachorro-Quente      ' + '|    09,00   |')
print('|  101   |' + '   Cachorro-Quente Duplo  ' + ' |    11,00   |')
print('|  102   |' + '           X-Egg           ' + '|    12,00   |')
print('|  103   |' + '          X-Salada         ' + '|    13,00   |')
print('|  104   |' + '          X-Bacon          ' + '|    14,00   |')
print('|  105   |' + '           X-Tudo          ' + '|    17,00   |')
print('|  200   |' + '     Refrigerente Lata     ' + '|    05,00   |')
print('|  201   |' + '         Chá Gelado        ' + '|    04,00   |')

pedido = 0 # código do produto solicitado
conta = 0 # valor total da conta

while True:
	pedido = int(input('Entre com o código do produto desejado: '))
	
	if pedido == 100:
		print('Você pediu um Cachorro-Quente no valor de R$09,00')
		conta += 9 # adiciona o valor do produto escolhido ao valor total da conta
	
		resposta = int(input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 0 - Não \n'))
		if resposta == 1:
			# volta para o início do laço
			continue 
		elif resposta == 0:
			# termina o laço
			break
	elif pedido == 101:
		print('Você pediu um Cachorro-Quente Duplo no valor de R$11,00')
		conta += 11
	
		resposta = int(input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 0 - Não \n'))
		if resposta == 1:
			continue
		elif resposta == 0:
			break
	elif pedido == 102:
		print('Você pediu um X-Egg no valor de R$12,00')
		conta += 12
	
		resposta = int(input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 0 - Não \n'))
		if resposta == 1:
			continue
		elif resposta == 0:
			break
	elif pedido == 103:
		print('Você pediu um X-Salada no valor de R$13,00')
		conta += 13
	
		resposta = int(input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 0 - Não \n'))
		if resposta == 1:
			continue
		elif resposta == 0:
			break	
	elif pedido == 104:
		print('Você pediu um X-Bacon no valor de R$14,00')
		conta += 14
	
		resposta = int(input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 0 - Não \n'))
		if resposta == 1:
			continue
		elif resposta == 0:
			break			
	elif pedido == 105:
		print('Você pediu um X-Tudo no valor de R$17,00')
		conta += 17
	
		resposta = int(input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 0 - Não \n'))
		if resposta == 1:
			continue
		elif resposta == 0:
			break			
	elif pedido == 200:
		print('Você pediu um Refrigerante Lata no valor de R$5,00')
		conta += 5
	
		resposta = int(input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 0 - Não \n'))
		if resposta == 1:
			continue
		elif resposta == 0:
			break
	elif pedido == 201:
		print('Você pediu um Chá Gelado no valor de R$04,00')
		conta += 4
	
		resposta = int(input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 0 - Não \n'))
		if resposta == 0:
			break
		elif resposta == 1:
			continue			
	else:
			# volta para o início do laço caso um código de produto inexistente for digitado
			print('Opção Inválida')
			continue	
			
print('\nSua conta deu R${:.2f}'.format(conta))
