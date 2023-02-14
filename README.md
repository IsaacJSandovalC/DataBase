# Talleres.
Reposito exclusivo para talleres y casos de la materia Programación 4

## Índice:
* [Taller N° 1 usando SQLite](#id1)
* [Taller N° 2 usando ORM(SQLAlchemy)](#id2)



## Taller #1<a name="id1"></a>
Este trabajo se emplea utilizando Python y SQLite, se creo una tabla llamada "Slangs.db", se le agregan las funciones de:

* Agregar nueva palabra.
* Editar palabra existente.
* Eliminar palabra existente.
* Ver listado de palabras.
* Buscar significado de palabra.
* Salir.

en este enlace puedes acceder al taller: [Click](https://github.com/IsaacJSandovalC/programacion4/blob/main/taller_1.py).


## Taller #2<a name="id2"></a>
Este trabajo se emplea utilizando Python, Pymysql y SQLAlchemy, se crea una tabla llamada "Slangs", se le agregan las funciones de:

* Agregar nueva palabra.
* Editar palabra existente.
* Eliminar palabra existente.
* Ver listado de palabras.
* Buscar significado de palabra.
* Salir.

para su uso correcto, reemplazar las credenciales del archivo [conexion.py](https://github.com/IsaacJSandovalC/programacion4/blob/main/orm/conexion.py) por sus credenciales en MySQL de la siguiente manera:

```
engine = create_engine('mysql+pymysql://user:password@host/database')
Session = sessionmaker(bind=engine)
session = Session()
```

### Enlaces a los documentos del taller: 
* conexion.py: [Click](https://github.com/IsaacJSandovalC/programacion4/blob/main/orm/conexion.py)
* menu.py: [Click](https://github.com/IsaacJSandovalC/programacion4/blob/main/orm/menu.py)
* slangs.py: [Click](https://github.com/IsaacJSandovalC/programacion4/blob/main/orm/slangs.py)

