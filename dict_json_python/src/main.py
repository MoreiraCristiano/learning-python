import json


# Carregar arquivo json para o python
with open("../data/input_data.json") as my_json:
	data = json.load(my_json)

print("\n============================= Print linha 9, 10, 11 =============================")
print(type(data))					# Apos ser carregado o json vira um dict
print(data)							# Impressao simples do dict
print(json.dumps(data, indent=4))	# Imprime o dict formatado
print("==================================================================================\n")


print("\n================================= Print linha 16 =================================")
print(data["Nome"])					# Imprime o valor da key "Nome"
data["Nome"] = "Josualdo Crovis"	# Associa um novo valor a key "Nome"


del data["Nome"]					# Remove a key e seu valor do dict
data["Nome"] = "Josualdo Crovis"	# Adiciona novamente o valor ao final do dict
print("==================================================================================\n")


print("\n================================= Print linha 26, 29 =============================")
if ("Nome" in data):				# Verificando a existencia de uma key
	print(data["Nome"])
else:
	print("Não existe")
print("==================================================================================\n")


"""
	Metodos para dicionarios
"""
# Iteracao pelas chaves do dict
for key_name in data.keys():
	print("\n================================= Print linha 39 =================================")
	print(key_name)
	print("==================================================================================\n")

# Iteracao pelos valores do dict
for value in data.values():
	print("\n================================= Print linha 45 =================================")
	print(value)
	print("==================================================================================\n")

# Convertendo dicts para listas
list(data.keys())			# ['Estudando', 'Reside em', 'Nome']
list(data.values())			# ['Json em python', 'Atebaea', 'Josualdo Crovis']
list(data.items())			# [('Estudando', 'Json em python'), ('Reside em', 'Atebaea'), ('Nome', 'Josualdo Crovis')]

# Print em sorted ordem
for key in sorted(data.keys()):
	print("\n================================= Print linha 56 =================================")
	print(key)
	print("==================================================================================\n")
