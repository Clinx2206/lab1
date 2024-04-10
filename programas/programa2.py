# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
	match = re.findall(r'"user": "(.*)",', texto)
	vistos = [];
	ret = "";
	counter = 1
	print(len(match))
	for i in match:
		counter += 1
		if i not in vistos:
			vistos.append(i)
			ret = ret + f"{i}" + ": 1" 
			if (counter - 1) < len(match):
				ret = ret + "\n"
		else:
			edit = re.search(r'@(.*)!\n', texto)
	
	return ret

if __name__ == '__main__':
	entrada = sys.argv[1]  # archivo entrada (param)
	salida = sys.argv[2]   # archivo salida (param)

	f = open(entrada, 'r') # abrir archivo entrada
	datos = f.read()       # leer archivo entrada
	f.close()              # cerrar archivo entrada
    
	ret = prog(datos)      # ejecutar er
    
	f = open(salida, 'w')  # abrir archivo salida
	f.write(ret)           # escribir archivo salida
	f.close()              # cerrar archivo salida
