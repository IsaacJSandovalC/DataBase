# Descripcion
Proyecto realizado utilizando MySql, se implementa un CRUD (registro, búsqueda, edición y eliminación) como parcial para la materia de programacion 4

# Libreria
Para el uso correcto de este taller se debe utilizar primero el siguiente comando:

```
pip install pymysql
```

# MotorDB a utilizar
Antes de realizar la conexion, se debe crear la base de datos, dejo un ejemplo de como hacerlo con Querys desde consola:
```
CREATE DATABASE nombre_de_tu_db;
USE nombre_de_tu_db;

CREATE TABLE nombre_de_tu_tabla (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    edad INT,
    email VARCHAR(255)
);
```

# Conexion

Ya que se esta utilizando pymsql como libreria de conexion a la base de datos. Seguido a eso, se debe hacer la conexion desde el documento **conexion.py** con la siguiente configuracion: 

```
conexion = pymysql.connect(
    host='localhost',
    user='tu_usuario',
    password='tu_contraseña',
    db='nombre_de_tu_db',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
```
