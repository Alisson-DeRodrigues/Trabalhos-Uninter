print('Bem Vindo ao Centro Logístico Alisson de Souza Rodrigues Ltda')


def dimensoesObjeto():
	while True:
		try:
			# variávies para o cálculo do volume do objeto
			altura = float(input('Insira a altura do objeto (em cm): '))
			comprimento = float(input('Insira o comprimento do objeto (em cm): '))
			largura = float(input('Insira a largura do objeto (em cm): '))
			
			volume = altura * comprimento * largura # volume do objeto
			if volume >= 100000:
				# volta para o início do laço caso o volume do objeto seja maior que 100000 cm³
				print('O volume do objeto é {} cm³, não aceitamos objetos com volume tão grande.'.format(volume))
				continue
			print('O volume do objeto é {} cm³'.format(volume))
			
			# retorna o preço conforme o volume
			if volume < 1000:
				return 10
			elif volume < 10000:
				# volume de 1000 a 9999 cm³
				return 20
			elif volume < 30000:
				# volume de 10000 a 29999 cm³
				return 30
			elif volume < 100000:
				# volume de 30000 a 99999 cm³
				return 50
			
			break # encerra o looping infinito
		except:
			print('Insira um valor válido')
			continue # retorna para o início do laço em caso de valor inválido
		
def pesoObjeto():
 	while True:
 		try:
 			peso = float(input('Insira o peso do objeto (em kg): '))
 		
 			print('O objeto tem {} kg '.format(peso))
 		
 			if peso >= 30:
 			# volta para o início do laço caso o objeto tenha 30 kg ou mais
 				print('Ele é muito pesado, tente outro objeto')
 				continue
 		
 		# retorna o multiplicador conforme o peso
 			if peso < 0.1:
 				return 1
 			elif peso < 1:
 			# peso de 0.1 a 0.999 kg
 				return 1.5
 			elif peso < 10:
 			# peso de 1 a 9.999 kg
 				return 2
 			elif peso < 30:
 			# peso de 10 a 29.999 kg
 				return 3
 			break
 		except:
 			print('Insira um valor válido')
 			continue # volta para o início do laço em caso de valor inválido
 		
def rotaObjeto():
	while True:
		print('Escolha a rota do objeto:')
		print('RS - De Rio de Janeiro até São Paulo')
		print('SR - De São Paulo até Rio de Janeiro')
		print('BS - De Brasília até São Paulo')
		print('SB - De São Paulo até Brasília')
		print('BR - De Brasília até Rio de Janeiro')
		print('RB - De Rio de Janeiro até Brasília')
			
		rota = input()
		
		# retorna o multiplicador de cada rota
		if rota == 'RS':
			return 1
		elif rota == 'SR':
			return 1
		elif rota== 'BS':
			return 1.2
		elif rota== 'SB':
			return 1.2
		elif rota== 'BR':
			return 1.5
		elif rota== 'RB':
			return 1.5
		else:
			print('Insira uma rota válida')
			continue
			
		break
		
total = dimensoesObjeto() * pesoObjeto() *rotaObjeto()
print('O total a ser pago é R${}'.format(total))

