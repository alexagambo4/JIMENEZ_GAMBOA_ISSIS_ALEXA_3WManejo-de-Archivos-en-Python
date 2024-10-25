#imprime los datos del autor
print("jimenez gamboa issis alexa")
print("no.1189")
print("3W")
#imprime una linea pára que se vea mas limpio
print("")

#Ejemplo
#Comprueba si el archivo existe  elimínalo:
import os
if os.path.exists("ALUMNOS.txt"):
    os.remove("ALUMNOS.txt")
else:
    print("The file does not exist")
