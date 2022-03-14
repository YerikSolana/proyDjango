if __name__ == '__main__':
	numa = int()
	numb = int()
	pares = int()
	print("Escriba el primer número")
	numa = int(input())
	print("Escriba el segundo número")
	numb = int(input())
	for pares in range(numa,numb+1):
		if pares%2==0:
			print("Los números pares son: ",pares)

