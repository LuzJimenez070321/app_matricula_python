lista_alumnos=[]
def mensaje_manu():
     menu_opciones="""
                         bienvenido al sistema
                         registra tu alumno
     1. escribe (s) si desas agregar un nuevo alumno
     2. escribe (n) si deseas salir del sistema
     escribe la accion que deseas realizar:""" 
     return(menu_opciones)

def ingresar_datos_alumnos():
     id=len(lista_alumnos)+1
     cui=int(input("ingresa el numero de su dni: "))
     nombre=input("ingrese nombre del alumno: ")
     apellido=input("ingrese el apellido del alumno: ")
     numero_celular=input("ingrese el numero de celular del alumno: ")
     programa_estudio=input("8ingrese el programa de estudio: ")
     ciclo_academico=input("ingrese su ciclo academico: ")
     email=input("ingrese su correo electronico: ")
     guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)

def guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
     alumnos={
          "id":id,
          "cui":cui,
          "nombre":nombre,
          "apellido":apellido,
          "numero_celular":numero_celular,
          "programa_estudio":programa_estudio,
          "ciclo_academico":ciclo_academico,
          "email":email
     }     
while True:
     mensaje_menu=input(mensaje_menu())

     if menu_opciones.lower()== "n":
          print("saliendo del sistema")
          break
     elif menu_opciones.lower() == "s":
          ingresar_datos_alumno()
     else:
          print("opcion erronea")     
