from sys import argv
from random import randrange, randint, random

debug = False # activar para poder ver todos los "print"

MIN = 3
MAX = 5

def generaDatos(argv):
  try: 
		largo = int(argv[1])
	except:
		largo = int(raw_input("Largo de palabra: "))
	try: 
		densidad = float(argv[2])
	except:
		densidad = float(raw_input("Densidad(generar ceros): "))
	try:
		probabilidadCero = float(argv[3])
	except:
		probabilidadCero = float(raw_input("Probalidad de recibir ceros: "))
	try: 
		probabilidadUno = float(argv[4])
	except:
		probabilidadUno = float(raw_input("Probalidad de recibir unos: "))
	try:
		repeticiones = int(argv[5])
	except:
		repeticiones = int(raw_input("Repeticiones por palabra: "))
	
	return (largo, densidad, probabilidadCero, probabilidadUno, repeticiones)

def generarPalabras(largoPalabra, densidad):
	palabras = list()
	caracter = ""
	for numero in xrange(largoPalabra): 
		caracter += ("1","0")[random() <= densidad] # operador ternario en python
	palabras.append(caracter) # agregamos la letra a las palabras
	return palabras

def transmisor(palabra, probaCeros, probaUnos):
	palabraFinal = list()
	for lista1 in palabra:
		for elemento in lista1:
			letra = ""
			for caracter in elemento:
				if caracter == "1":
					if random() >= probaUnos: # significa que recibe un cero
						letra += "0" # mal
					else:
						letra += "1" # bien
				else: # recibe un cero
					if random() >= probaCeros:
						letra += "1" # mal
					else:
						letra += "0" # bien
		palabraFinal.append(letra)

	# comparacion de cadenas
	for caracter in palabra:
		if palabraFinal == caracter:
			if debug: print "-", palabraFinal
			return True
		else:
			if debug: print "-", palabraFinal
			return False

def main():
	(largoPalabras, densidad, probaCeros, probaUnos, repeticiones) = generaDatos(argv) # genereamos los datos de necesarios para el prog  
	palabras = generarPalabras(largoPalabras, densidad) # generemos palabras aleatoriamente
	if debug: print "original: ", contenido[0]		
	exito = 0 
	for i in xrange(repeticiones): # repeticiones por palabra
		resultado = transmisor(palabras, probaCeros, probaUnos)
		if resultado:
			exito += 1 # sacamos las veces que fueron correcta
	probabilidad = float(exito) / float(repeticiones)
	print probabilidad # probabilidad de confianza del canal
	return	

main()
