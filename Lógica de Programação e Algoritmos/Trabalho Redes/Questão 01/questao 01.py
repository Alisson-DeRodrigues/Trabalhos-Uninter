print("Bem Vindo a Loja de Alisson de Souza Rodrigues")

valor_produto = float(input('Insira o valor do produto: '))
qtd_produto = int(input('Insira a quantidade do produto: '))

total = 0 # valor total sem desconto
total_desconto = 0 # valor total com desconto

if qtd_produto <= 9:
	# desconto de 0% para até 9 itens
	total = valor_produto * qtd_produto
	total_desconto = valor_produto * qtd_produto
	
	print('o valor total da venda sem desconto é: R${:.2f}'.format(total))
	print('o valor total da venda com desconto é: R${:.2f}'.format(total_desconto))
	
elif qtd_produto <= 99:
	# desconto de 5% para 10 até 99 itens
	desconto = 0.95
	total = valor_produto * qtd_produto
	total_desconto = valor_produto * desconto * qtd_produto
	
	print('o valor total da venda sem desconto é: R${:.2f}'.format(total))
	print('o valor total da venda com desconto é: R${:.2f} (desconto 5%)'.format(total_desconto))
	
elif qtd_produto <= 999:
	# desconto de 10% para 100 até 999 itens
	desconto = 0.9
	total = valor_produto * qtd_produto
	total_desconto = valor_produto * desconto * qtd_produto
	
	print('o valor total da venda sem desconto é: R${:.2f}'.format(total))
	print('o valor total da venda com desconto é: R${:.2f} (desconto 10%)'.format(total_desconto))
	
else:
	# desconto de 15% para acima de 1000 itens
	desconto = 0.85
	total = valor_produto * qtd_produto
	total_desconto = valor_produto * desconto * qtd_produto
	
	print('o valor total da venda sem desconto é: R${:.2f}'.format(total))
	print('o valor total da venda com desconto é: R${:.2f} (desconto 15%)'.format(total_desconto))

