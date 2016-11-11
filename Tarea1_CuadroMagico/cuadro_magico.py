def imprimir_cuadro():
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
		if cuadro_magico[tamanio-1-pos][pos]==0:
			sin_llenar==True
	if (sin_llenar==False and constante_acumulada!=constante_magica):
		return False
	return True	

def back_magic(renglon,columna):
	if (not verificar_renglones() or not verificar_columnas() or not verificar_diagonales()):
		return
	if (renglon==tamanio):
		imprimir_cuadro()
		print "*******************"
		return
	for i in range(0,ncuadrados_totales):
		if ncuadrados_posibles[i]==True:
			cuadro_magico[renglon][columna]=i+1
			ncuadrados_posibles[i]=False

			sig_columna=columna+1
			sig_renglon=renglon
			if sig_columna==tamanio:
				sig_renglon+=1
				sig_columna=0

			back_magic(sig_renglon,sig_columna)

			cuadro_magico[renglon][columna]=0
			ncuadrados_posibles[i]=True




#Referencia a este valor en: http://mathworld.wolfram.com/MagicSquare.htm

tamanio=int(raw_input("Dame el tamanio de tu cuadro magico: "))
cuadro_magico=[[0 for x in range (tamanio)] for y in range(tamanio)]
ncuadrados_totales=tamanio**2
ncuadrados_posibles=[True for x in range (ncuadrados_totales)]
constante_magica=((tamanio**3)+(tamanio))/2
back_magic(0,0)
