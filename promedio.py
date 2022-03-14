if __name__ == '__main__':

	numalumno = int()
	cal1 = int()
	cal2 = int()
	cal3 = int()
	promedioalumno = float()
	promediogrupo = float()
	aprobados = int()
	reprobados = int()
	contadoralumnos = int()

	print("¿A cuántos alumnos calculará su promedio?")
	numalumno = int(input())
	contadoralumnos = 0
	aprobados = 0
	reprobados = 0
	while True:
		print("califacion 1")
		cal1 = int(input())
		print("califacion 2")
		cal2 = int(input())
		print("califacion 3")
		cal3 = int(input())
		promedioalumno = (cal1+cal2+cal3)/3
		promediogrupo = promediogrupo+(promedioalumno)/numalumno
		print("promedio alumno",promedioalumno)
		if promedioalumno>=7:
			print("Aprobado")
			aprobados = aprobados+1
		else:
			print("Reprobado")
			reprobados = reprobados+1
		contadoralumnos = contadoralumnos+1

		if contadoralumnos==numalumno: break
	print("Alumnos aprobados: ",aprobados)
	print("Alumnos reprobados: ",reprobados)

