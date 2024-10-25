#imprime los datos del autor
print("jimenez gamboa issis alexa")
print("no.1189")
print("3W")
#imprime una linea pára que se vea mas limpio
print("")

#Ejemplo
#Abra el archivo "demofile3.txt" y sobrescriba el contenido:
f = open("ALUMNOS.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("ALUMNOS.txt", "r")
print(f.read())