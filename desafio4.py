temperatura = float(input("Ingrese su temperatura: "))
frecuencia_cardiaca = int(input("ingrese su frecuencia cardíaca: "))

if temperatura < 35 or temperatura > 40 :
    print("temperatura critica")
elif temperatura >= 38 and frecuencia_cardiaca >=100 :
    print("posible cuadro febril")
else:
    print("sin criterios de gravedad")
