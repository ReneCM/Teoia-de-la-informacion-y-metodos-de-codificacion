#!/usr/bin/python

# Importando modulos
import time
from heapq import heappush, heappop, heapify

tiempoi = time.time()

# Funcion de codigo de huffman
def huff(f):
  tiempoi = time.time()
	pila = [[pal, [simbolo, ""]] for simbolo, pal in f.items()]
	heapify(pila)
	while len(pila) > 1:
		largo = heappop(pila)
		ancho = heappop(pila)
		for pares in largo[1:]:
			pares[1] = "0" + pares[1]
		for pares in ancho[1:]:
			pares[1] = "1" + pares[1]
		heappush(pila, [largo[0] + ancho[0]] + largo[1:] + ancho[1:])
	return sorted(heappop(pila)[1:], key=lambda p: (len(p[-1]), p))

# Imprimiendo Tabla
def imprimir(huff):
	print "\nLetra\tBinario"
	for p in huff:
		simbolo, codigo = p[0], p[1]
		print "%s\t%s" % (simbolo, codigo)
	return

# Frencuencias
def frecuencia(txt):
	f = {}
	for caracter in txt:
		if caracter in f:
			f[caracter] += 1
		else:
			f[caracter] = 1
	return f
	
# Codificando 
def codificar(txt, huff):
	tiempoi = time.time()
	cadena = ""
	for char in txt:
		for row in huff:
			if char in row:
				cadena += row[1]
				break
	print "\nTexto Codificado: %s"%cadena
	tiempof = time.time()
	print "\nCodificar, se tardo: ",tiempof-tiempoi,"segundos"
	return cadena

# Decodificando texto
def decodificar(pal_bin, huff):
	tiempoi = time.time()
	tmp = ""
	match = {}
	cadena = ""
	for bit in pal_bin:
		tmp += bit
		if len(tmp) == 1:
			for p in huff:
				if p[1][len(tmp)-1] == tmp[len(tmp)-1]:
					match[p[1]] = p[0]
		else:
			for key in match:
				if tmp in key:
					if tmp == key:
						tmp = ""
						cadena += match[key]
	print "\nTexto Decodificado: %s" %cadena
	tiempof = time.time()
	print "\nDecodificar, se tardo: ",tiempof-tiempoi,"segundos"
	return cadena

txt = raw_input("Texto: ")
f = frecuencia(txt)
huff = huff(f)
imprimir(huff)
pal_bin = codificar(txt, huff)  
txt = decodificar(pal_bin, huff)  
