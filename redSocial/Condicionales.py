### Condicionales ###

from pickle import TRUE


llueve = False
if llueve == True:
    print("Caen perros y gatos papayon")

else:
    print("Ya valio madre y padre, este pedo no jala")

llueve = True
temperatura = 12

if llueve == True and temperatura < 12:
    print ("Ya valió ma... , covid seguro")

if temperatura < 18:
    if llueve == True:
        print("algo chingón")
    else:
        print("Nada poca madre")
else:
    print(" A Huevo!! ") 

numero = int(input("Ingrese calidad del aire "))
if numero >= 0 and numero <= 99:
  print("Bueno")
elif numero >= 100 and numero <= 199:
  print("Regular")
elif numero >= 200 and numero <= 299:
  print("Alerta")
elif numero >= 300 and numero <= 499:
  print("Preemergencia")
else:
  print("Emergencia")