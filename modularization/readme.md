# Imports
	1. Imports de somente modulos pode ser feito utilizando import.pasta.arquivo
	2. Se o import for ser uma pasta toda a pasta deve conter o arquivo __init__.py e então o python esta reconhecendo o import do arquivo __init__.py(SÓ ele) sendo assim os imports devem estar constando no __init__.py para que seja enxergado por arquivos externos. (Não é a melhor pratica, pois não pratica o import relativo).
	3. Se o arquivo possuir __name__ == '__main__' o passo 2 já não funciona 

# Imports relativos

	1. 	Imports relativos funcionam utilizando seguinte codigo 
	
		import sys
		from pathlib import Path
		file = Path(__file__).resolve()
		parent, root = file.parent, file.parents[1]
		sys.path.append(str(root))

