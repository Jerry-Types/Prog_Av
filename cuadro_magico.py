def imprimir_cuadro(cuadro_magico):
	for renglon in cuadro_magico:
		print renglon


def verificar_renglones():
	for renglon in cuadro_magico:
		constante_acumulada=0
		sin_llenar= False
		for columna in renglon:
			constante_acumulada+=columna
			if columna==0:
				sin_llenar=True
		if (sin_llenar==False and constante_acumulada!=constante_magica):
			return False
	return True


def verificar_columnas():
	for columna in range(len(cuadro_magico[0])):
		constante_acumulada=0
		sin_llenar=False
		for renglon in cuadro_magico:
			constante_acumulada+=renglon[columna]
			if  renglon[columna]==0:
				sin_llenar=True
		if (sin_llenar==False and constante_acumulada!=constante_magica):
			return False
	return True


#Crear una matriz que represente el cuadro magico
tamanio=int(raw_input("Dame el tamanio de tu cuadro magico: "))
#cuadro_magico=[[0 for x in range (tamanio)] for y in range(tamanio)]
cuadro_magico=[[1,2,3],[4,5,6],[7,8,9]]

#Cuadro magico parcial
#cuadro_magico=[[4,9,0],[0,0,0],[0,0,0]]

#Cuadro magico valido
#cuadro_magico=[[4,9,2],[3,5,7],[8,1,6]]

ncuadrados_totales=tamanio**2
ncuadrados_posibles=[True for x in range (ncuadrados_totales)]

#Referencia a este valor en: http://mathworld.wolfram.com/MagicSquare.html
constante_magica=((tamanio**3)+(tamanio))/2


def verificar_diagonales():
	sin_llenar=False
	constante_acumulada=0
	for pos in range(0,3):
		constante_acumulada+=cuadro_magico[pos][pos]
		if cuadro_magico[pos][pos]==0:
			sin_llenar=True
	if (sin_llenar==False and constante_acumulada!=constante_magica):
		return False
	constante_acumulada=0
	
	for pos in range(tamanio-1,-1,-1):
		constante_acumulada+=cuadro_magico[tamanio-1-pos][pos]
		if cuadro_magico[tamanio-1-pos][pos]==0
imprimir_cuadro(cuadro_magico)
verificar_diagonales()
