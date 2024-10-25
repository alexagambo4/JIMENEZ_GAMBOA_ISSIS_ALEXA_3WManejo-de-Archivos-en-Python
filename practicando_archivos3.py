#imprime los datos del autor
print("jimenez gamboa issis alexa")
print("no.1189")
print("3W")
#imprime una linea pára que se vea mas limpio
print("")

#Leer solo partes del archivo
#De forma predeterminada, el read()método devuelve el texto completo, pero también puedes especificar cuántos caracteres quieres devolver:
#Ejemplo
#Devuelve los 5 primeros caracteres del archivo:
f = open("ALUMNOS.txt", "r")
print(f.read())
