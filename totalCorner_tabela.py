from selenium import webdriver
import json

class TotalCorner:
	
	def __init__(self):

		url = 'https://www.totalcorner.com/league/view/1363'

		self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')

		self.driver.get(url)


	def obter_tabela(self):

		base_tabela = '#content_container > div.main_content > div:nth-child(3) > div.col-sm-10 > table:nth-child(2) >'
		#Pegando os títulos das colunas da tabela e armazenando em uma lista

		headers_names = []

		headers = self.driver.find_elements_by_tag_name(f'{base_tabela}thead > tr > th')

		#Na tabela tem um símbolo de um relógio que retorna uma string vazia, então substitui por 'Tempo de jogo'

		for name in headers:

			if name.text != '':
				headers_names.append(name.text)
			else:
				headers_names.append('Tempo de jogo')

		# Obtendo a quantidade de linhas e a quantidade de colunas( quantidade de elementos em cada linha)

		lista_linhas = self.driver.find_elements_by_tag_name(f'{base_tabela}tbody > tr')

		quantidade_linhas = len(lista_linhas)

		lista_elemento_linha = self.driver.find_elements_by_tag_name(f'{base_tabela}tbody > tr:nth-child(2) > td')

		quantidade_elem_linha = len(lista_elemento_linha)

		#Lista que em que será salvo os dados da tabela

		tabela_json = []

		print(f'Tems um total de {quantidade_linhas} linhas...')

		for linha in range(quantidade_linhas):

			lista_auxiliar = []

			dicionario_auxiliar ={}

			lista_elemento_linha = self.driver.find_elements_by_tag_name(f'{base_tabela}tbody > tr:nth-child({linha + 1}) > td')
            
            # Verificando se a linha possui, no caso , 15 elementos para fazer a iteração

			if len(lista_elemento_linha) == quantidade_elem_linha:

				for elemento in range(quantidade_elem_linha):

					item = self.driver.find_element_by_tag_name(f'{base_tabela}tbody > tr:nth-child({linha + 1}) > td:nth-child({elemento + 1})')

					# Cada elemento da linha é adicionado na lista auxiliar

					lista_auxiliar.append(item.text)
				
				for dado in range(len(lista_auxiliar)):

					#Adicionando cada elemento da lista ao dicionário auxiliar, cuja chave será cada elemento da
					#lista headers_name

					dicionario_auxiliar[headers_names[dado]] = lista_auxiliar[dado]

					#Adicionando o dicionário, que representa cada linha da coluna, na tabela_json, criando uma extrutora JSON

				tabela_json.append(dicionario_auxiliar)

				print(f'Obtendo {linha}° linha ...')
		
		print('Finalizado.')

		#Salvando a lista como JSON

		with open('tabela.json', 'w') as json_file:

			json.dump(tabela_json, json_file)

		self.driver.quit()

		return(tabela_json)

		

x = TotalCorner()

print(x.obter_tabela())





