#imprime los datos del autor
print("jimenez gamboa issis alexa")
print("no.1189")
print("3W")
#imprime una linea pára que se vea mas limpio
print("")

archivo = open("ALUMNOS.txt", "r") #abro archivo de texto para solo lectura 
#r es para lectura
#a anexar
#w para escribir
print(archivo.readable())
#read imprime el archivo
#readline solo sale un nombre 
#readable para ver si es soo lectura 
archivo.close()
