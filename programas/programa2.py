# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
	match = re.findall(r'"user": "((.)*)",', texto)
	vistos = dict();
	ret = "";
	for i in match:
		x = f"{i[0]}" 
		if vistos.get(x) == None:
			vistos[x] = 1;
		else:
			vistos[x] = vistos[x] + 1
	for x in vistos:
		ret = ret + x + ": " + str(vistos[x]) + "\n"
	ret = ret.removesuffix('\n')
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
