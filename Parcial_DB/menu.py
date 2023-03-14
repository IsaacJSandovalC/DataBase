from acciones import *


while True:
        print('--------------------------------------------------------------')
        print('Este es el menu de nuestrA base de datos, ingresa tu accion:\n'
              '1. Agregar valor\n'
              '2. Actualizar valor\n'
              '3. Eliminar valor\n'
              '4. Imprimir todos los valores\n'
              '5. Salir'
              )

        desicion = input("Que deseas hacer?: ")

        if desicion == '1':
            print('**** Agregar registro ****')
            nombre = input("Ingresa el nombre: ")
            edad = input("Ingresa la edad: ")
            correo = input("Ingresa el correo: ")
            
            if crear_registro(nombre, edad, correo) == True:
                print("Registro agregado exitosamente")
            else:
                print("Error al agregar registro")

        elif desicion == '2':
            print('**** Actualizar registro ****')
            id = input("Ingresa el id del registro a actualizar: ")
            nombre = input("Ingresa el nombre: ")
            edad = input("Ingresa la edad: ")
            correo = input("Ingresa el correo: ")
            
            if actualizar_registro(id, nombre, edad, correo) == True:
                print("Registro actualizado exitosamente")
            else:
                print("Error al actualizar registro") 

        elif desicion == '3':
            print('**** Eliminar registro ****')
            id = int(input("Ingresa el id del registro a eliminar: "))
            if eliminar_registro(id) == True:
                print("Registro eliminado exitosamente")
            else:
                print("Error al eliminar registro") 

        elif desicion == '4':
            print('**** Leer registro ****')
            id = int(input("Ingresa el id del registro a leer: "))
            registro = leer_registro(id)
            
            if registro != None:
                print(', '.join([f'{key}: {value}' for key, value in registro.items()]))
            else:
                print("Registro no encontrado")


        elif desicion == '5':
            print('**********************************')
            print("Saliendo del programa")
            conexion.close()
            break


# Ejemplo de uso



# Cerrar la conexión
