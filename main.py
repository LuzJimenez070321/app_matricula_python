"""
- Registrar alumnos
- Generar fichas de matricula
- Mostrar la lista de todos los matriculados 
- Filtrar matriculados por programa de estudio 
"""
# inicio de problema
# nesecito poder agregar mas alumnos sin la nesecidad d crear tantas variable 
# posible solucionar crear o encerrar el codigo en un suglo while
lista_alumnos=[]

nombre=input("ingrese nombre del alumno: ")
apellido=input("ingrese el apellido alumno: ")

nombre2=input("ingrese nombre del alumno: ")
apellido2=input("ingrese el apellido alumno: ")
alumno={
    "nombre":nombre,
    "apellido":apellido
}
{
    "nombre2":nombre2,
    "apellido2":apellido2
}
lista_alumnos.append(nombre)
lista_alumnos.append(nombre2)
# fin de problema 

# deseo mostrar un menu con las opciones de agregar un nuevo alumno y salir del progrma 
print(lista_alumnos)