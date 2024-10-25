#imprime los datos del autor
print("jimenez gamboa issis alexa")
print("no.1189")
print("3W")
#imprime una linea pára que se vea mas limpio
print("")

#Ejemplo:
#Abra el archivo "ALUMNOS.txt" y agregue contenido al archivo:
f = open("ALUMNOS.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("ALUMNOS.txt", "r")
print(f.read())
