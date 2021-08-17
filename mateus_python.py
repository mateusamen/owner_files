from pathlib import Path
import os
import sys

input_program = sys.argv

print(input_program)
if (len(input_program)>1):
	path_desired = input_program[1]
else:
	path_desired =(".")

print(path_desired)
lista_arquivos = os.listdir(path_desired)
print(str(lista_arquivos))
for arquivo in lista_arquivos:
	file_path = path_desired + ('/') + arquivo 	
	path = Path(file_path)
	owner = path.owner()
	nome = [owner]	
	print(f"{path.name} is owned by {owner}")

print(nome)



