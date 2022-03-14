if __name__ == '__main__':
	n = int()
	i = int()
	a = int()
	print("Ingrese el número a multiplicar")
	n = int(input())
	print("Ingrese hasta qué número se multiplicará")
	a = int(input())
	i = 0
	print("Los multiplos de ",n," son: ")
	while True:# no hay 'repetir' en python
		i = i+1
		print(n," x ",i,"= ",n*i)
		if i==a: break

