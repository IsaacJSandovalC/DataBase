from conexion import conexion

# Crear un registro
def crear_registro(nombre, edad, email):
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO personas (nombre, edad, email) VALUES (%s, %s, %s)"
        valores = (nombre, edad, email)
        resultado = cursor.execute(consulta, valores)
    conexion.commit()
    return resultado != 0

# Leer un registro
def leer_registro(id):
    with conexion.cursor() as cursor:
        consulta = "SELECT * FROM personas WHERE id = %s"
        valor = (id,)
        cursor.execute(consulta, valor)
        resultado = cursor.fetchone()
    return resultado
        

# Actualizar un registro
def actualizar_registro(id, nombre, edad, email):
    with conexion.cursor() as cursor:
        consulta = "UPDATE personas SET nombre = %s, edad = %s, email = %s WHERE id = %s"
        valores = (nombre, edad, email, id)
        resultado = cursor.execute(consulta, valores)
    conexion.commit()
    return resultado != 0

# Eliminar un registro
def eliminar_registro(id):
    with conexion.cursor() as cursor:
        consulta = "DELETE FROM personas WHERE id = %s"
        valor = (id,)
        resultado =cursor.execute(consulta, valor)
    conexion.commit()
    return resultado != 0