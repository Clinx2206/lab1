# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
	match = re.search(r'@(.*)!\n', texto)
	ret = "";
	for i in match:
		ret = ret + ":1" + f"{i}" + "\n"
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
