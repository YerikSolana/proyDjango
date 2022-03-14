if __name__ == '__main__':
	lt_ac = float()
	lt_costo = float()
	precio_og = float()
	iva = float()
	preciofin = float()
	print("¿Cuántos litros de sanitizante desea comprar?")
	lt_ac = float(input())
	lt_costo = 0
	precio_og = lt_ac*70
	iva = 0
	preciofin = 0
	if lt_ac>5 and lt_ac<=10:
		lt_costo = precio_og-(precio_og*0.05)
	else:
		if lt_ac>10 and lt_ac<=20:
			lt_costo = precio_og-(precio_og*0.10)
		else:
			if lt_ac>20:
				lt_costo = precio_og-(precio_og*0.13)
			else:
				lt_costo = precio_og
	iva = lt_costo*0.16
	preciofin = iva+lt_costo
	print("Litros de sanitizante comprados: ",lt_ac)
	print("Precio Original: $",precio_og)
	print("Precio con descuento: $",lt_costo)
	print("IVA: $",iva)
	print("Precio + IVA: $",preciofin)

