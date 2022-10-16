### Iniciamos el ejercicio de red social ### 


print('Hola, Bienvenido a Red de Negocios KMX')
print(""" 
RED DE NEGOCIOS KMX
""")

nombre = input('Por favor escribe tu nombre y apellido ')
print(f"Hola" + ' ' + nombre + ' ' + "Bienvenid@ a esta RED DE NEGOCIOS")
print(nombre + ", Gracias por tu interés, para preparar tu perfil vamos a necesitar algo de información")

año_nacimiento = int(input('Para iniciar, por favor ingresa tu año de nacimiento '))
edad = 2022 - año_nacimiento
talla = float(input("¿Cuál es tu estatura en centímetros? "))
tallaM = int(talla)
tallaCM = int((talla - tallaM)* 100)
num_amigos = int(input("Con un poco de memoria, ¿Cuantos amigos crees tener? "))

print("***   ***")
print("Muy bien,", nombre, "Iniciamos a crear tu perfil")
print("***   ***")
print("Nombre: ", nombre)
print("Edad: ", edad, "años")
print("Altura: ", tallaCM, "cm")
print("Amigos: ", num_amigos)
print("***   ***")
print("Gracias por la información. Esperamos disfrutes hacer negocios aquí")

mensaje = input("Presentate a los demás, y/o escribe tu primer mensaje ")
print()
print("***   ***")
print(nombre, "acaba de escribir, ", mensaje)

