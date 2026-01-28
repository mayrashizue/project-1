nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
#edad es el nombre de la variable. 
#int quiere decir que el tipo de dato es un numero entero 
#input quiere decir que el programa va a pedir que ingrese un texto con el teclado
if edad >= 18:
    print(f"{nombre} es mayor de edad")
else:
    print(f"{nombre} es menor de edad")
