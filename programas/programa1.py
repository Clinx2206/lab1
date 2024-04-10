# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
	match = re.findall(r'@(([a-z]|[0-9]|[A-Z])*)', texto)
	matchUnicos = []
	for i in match:
		if i not in matchUnicos:
			matchUnicos.append(i)
	
	ret = ""
	counter = 1
	for i in matchUnicos:
		counter += 1
		ret = ret + f"{i[0]}"
		if counter <= len(matchUnicos):
			ret = ret + "\n"

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
