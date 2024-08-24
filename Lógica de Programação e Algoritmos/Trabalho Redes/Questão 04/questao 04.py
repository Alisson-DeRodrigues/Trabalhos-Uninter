print('Bem Vindo ao Controle de Estoque da Bicicletaria do Alisson de Souza Rodrigues')

estoque = [] # lista que armazena cada peça


def cadastrarPeca(codigo):
	peca = {'codigo': '000', 'nome':' ', 'fabricante': ' ', 'valor': 0} # formato padrão de cadastro de peça
	 
	peca['codigo'] = '%03d' % codigo # preenche com zeros a esquerda do número para manter o padrão de três dígitos
	peca['nome'] = input('Digite o nome da peça: ')
	peca['fabricante'] = input('Digite o fabricante da peça: ')
	peca['valor'] = input('Digite o valor (R$) da peça: ')
	estoque.append(peca) # adiciona o dicionário 'peca' sempre ao final da lista 'estoque''
	print('Peça cadastrada')
	print('O código desta peça é: ' + peca['codigo'])
	
def consultarPeca():
	while True:
		try:
			print('Escolha o tipo de consulta: ')
			print('1 - Todas as peças')
			print('2 - Código da peça')
			print('3 - Peça por frabricante')
			print('4 - Retornar')
			
			opcaoEscolhida = int(input())
			
			if opcaoEscolhida == 1:
				for i in estoque:
					# 'i' recebe cada dicionário presente em 'estoque'
					print('-' * 15)
					for j, k in i.items():
						# j e k recebe respectivamente chave e valor presente em cada dicionário
						print(j + ' : ' + k)
			elif opcaoEscolhida == 2:
				codigo = int(input('Insira o código da peça para consulta: '))
				pecaEncontrada = 0 # recebe o valor 1 se a peça for encontrada
				for i in estoque:
					if int(i['codigo']) == codigo:
						# consulta todos os dicionários presentes no estoque e faz o print da peça com o código indicado
						pecaEncontrada = 1
						for j, k in i.items():
							print(j + ' : ' + k)
				if pecaEncontrada == 0:
					print('Peça não encontrada')
					
			elif opcaoEscolhida == 3:
				fabricante = input('Insira o fabricante da peça para consulta: ')
				for i in estoque:
					# converte a string em letras minúsculas para facilitar a busca pelo fabricante
					if (i['fabricante']).lower() == (fabricante).lower():
						print('-' * 15)
						for j, k in i.items():
							print(j + ' : ' + k)
					else:
						print('Peça não encontrada')
			elif opcaoEscolhida == 4:
				break
		except:
			continue

def removerPeca():
	pecaRemover = int(input('Digite o código da peça que deseja remover: '))
	for i in estoque:
		if int(i['codigo']) == pecaRemover:
			estoque.remove(i) # deleta o dicionário da lista

while True:
	try:
		print('Escolha a opção desejada: ')
		print('1 - Cadastrar peças')
		print('2 - Consultar peças')
		print('3 - Remover peças')
		print('4 - Sair')
	
		opcaoEscolhida = int(input())
	
	
		if opcaoEscolhida == 1:
			codigo = len(estoque)
			# determina o código da peça com base na quantidade itens no estoque
			cadastrarPeca(codigo + 1) # '+ 1' impede o cadastro com o código 000
			continue
		elif opcaoEscolhida == 2:
			consultarPeca()
			continue
		elif opcaoEscolhida == 3:
			removerPeca()
			continue
		elif opcaoEscolhida == 4:
			break
		else:
			# caso um valor numérico não válido for digitado
			print('Escolha uma opção válida')
			continue
	except:
		# caso  um valor não numérico for digitado
		print('Escolha um valor numérico válido')
		continue
	
	break



