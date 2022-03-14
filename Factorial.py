if __name__ == '__main__':
	# input
	fact = float()
	num = float()
	cont = int()
	print("Ingrese un número")
	num = float(input())
	fact = 1
	# process
	if num>=0:
		for cont in range(1,num+1):
			fact = fact*cont
		# output
		print("El factorial es: ",fact)
	else:
		print("No existe factorial")

