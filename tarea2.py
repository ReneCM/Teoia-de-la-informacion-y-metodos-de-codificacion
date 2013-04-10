import random
import sys

debug = True

# clase que genera texto y patrones
class Generador:
  def __init__(self, *longitud):
		self.texto = longitud[0]
		self.patron = longitud[1]

	def generarTexto(self):
		txt_form = [chr(random.randrange(97, 105)) for i in xrange(self.texto)]
		txt_form = "".join(txt_form)
		return txt_form
		
	def generarPatron(self):
		patronFormado = [chr(random.randrange(97, 105)) for i in xrange(self.patron)]
		patron = "".join(patronFormado)
		return patron


# Clase que se encarga de comparar un patron si esta dentro de un texto(strings)
class Comparador:
	def __init__(self, *parametro):
		self.texto = parametro[0]
		self.patron = parametro[1]
		self.lenTexto = len(parametro[0]) 
		self.lenPatron = len(parametro[1])
		self.tablaSaltos = parametro[2]

	def comparadorBasico(self):
		indiceInicalPalabraEncontrada = list()
		intentosTotales  = 0

		for indice, caracter in enumerate(self.texto):
			intentosTotales += 1
			letraFormada = list()
			cont = 0
			if caracter == self.patron[cont]:
				sigIndice = indice
				while cont < self.lenPatron:
					try:
						letraFormada.append(self.texto[sigIndice])
					except:
						break 
					sigIndice += 1
					cont += 1
				letraFormada = "".join(letraFormada)
				if self.patron == letraFormada:
					indiceInicalPalabraEncontrada.append(indice)
		return(indiceInicalPalabraEncontrada ,intentosTotales)

	def morrisPratt(self):
		indiceInicalPalabraEncontrada = list()
		intentos  = 0

		for indice, caracter in enumerate(self.texto):
			intentos += 1
			letraFormada = list()
			cont = 0
			if caracter == self.patron[cont]:
				sigIndice = indice
				while cont < self.lenPatron:
					try:
						letraFormada.append(self.texto[sigIndice])
					except:
						break
					sigIndice += 1
					cont += 1
				letraFormada = "".join(letraFormada)
				if self.patron == letraFormada:
					indiceInicalPalabraEncontrada.append(indice)

		return(indiceInicalPalabraEncontrada ,intentos)

	def boyerMoore(self):
		indiceInicalPalabraEncontrada = list()
		indice = 0
		intentosTotales = 0
		while indice < self.lenTexto:
			if debug: print "indice Actual", indice, " letra ", self.texto[indice]
			salto = 0
			intentosTotales += 1
			incremeto = False ###############
			try:
				valorTextoFinal = self.texto[indice + (self.lenPatron - 1)]
				valorPatronFinal = self.patron[self.lenPatron - 1]
			except:
				break
			if valorTextoFinal == valorPatronFinal:
				salto += 1
				sig = 0
				indiceRaiz = next = indice 
				incremeto = True
				while self.texto[next] == self.patron[sig]:
					salto += 1 
					next += 1 
					sig += 1 
					incremeto = True
					if sig == self.lenPatron - 1:
						indiceInicalPalabraEncontrada.append(indiceRaiz)
						indice += self.tablaSaltos[self.texto[indiceRaiz]]
						incremeto = False
						break 
			if incremeto:
				salto += 1
				indice += salto
			
			else:
				try:
					indice += self.tablaSaltos[self.texto[indice + (self.lenPatron - 1)]]
				except:
					break
		return(indiceInicalPalabraEncontrada, intentosTotales)

def tabla(patron):
	print "patron", patron
	raw_input()
	tablaSaltos = {}
	for i in patron: 
		if not tablaSaltos.has_key(i):
			# agregamos la letra con su indice en la tabla
			tablaSaltos[i] = patron.index(i) + 1
	print tablaSaltos
	raw_input()

	return tablaSaltos

def reversa(cadena):
	for indice in range(len(cadena) - 2, -1, -1):
		yield cadena[indice]

def diferencias(texto, patron):
	patron = list(patron)
	for i in texto:
		if i not in patron:
			patron.insert(0, i)
	patron = "".join(patron)
	return patron

def main(lenTexto, lenPatron):
	gene = Generador(lenTexto, lenPatron)
	texto = gene.generarTexto()
	patron = copyPatron = gene.generarPatron()
	texto = "facebookfatrcetyobwqoplonaqkfatrcetyobwqoplonaqk"
	patron = copyPatron = "facebok"
	copyPatron = diferencias(texto, copyPatron)
	copyPatron = [letra for letra in reversa(copyPatron)]
	copyPatron = "".join(copyPatron) #convertimos la lista en cadena
	tablaSaltos = tabla(copyPatron)
	print "tabla", tablaSaltos
	print "texto ", texto
	print "patron", patron
	comp = Comparador(texto, patron, tablaSaltos)
	(basico, intentosBasico) = comp.comparadorBasico()
	(morris, intentosMorris) = comp.morrisPratt()
	(boyer, intentosBoyer) = comp.boyerMoore()
	print "indice para basico => ", basico, " intentos ", intentosBasico
	print "indice para morris => ", morris, " intentos ", intentosMorris
	print "indice para boyer => ", boyer, " intentos ", intentosBoyer

#argumento 1 = cantidad de texto rndom
#argumento 2 = cantidad de patron random
main(int(sys.argv[1]), int(sys.argv[2]))
