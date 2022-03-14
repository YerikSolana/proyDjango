if __name__ == '__main__':
	rept = float()
	parejaconejo1 = float()
	parejaconejo2 = float()
	parejaconejo3 = float()
	cont = float()
	print("Ingrese la cantidad de números que se imprimirán ")
	rept = float(input())
	parejaconejo1 = 0
	parejaconejo2 = 1
	for cont in range(1,rept+1):
		print("El número ",cont," de la secuencia es: ",parejaconejo1)
		parejaconejo3 = parejaconejo1+parejaconejo2
		parejaconejo1 = parejaconejo2
		parejaconejo2 = parejaconejo3

