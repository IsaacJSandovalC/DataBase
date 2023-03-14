## Taller #2 ORM(SQLAlchemy)<a name="id2"></a>
Este trabajo se emplea utilizando Python, Pymysql y SQLAlchemy, se crea una tabla llamada "Slangs", se le agregan las funciones de:

* Agregar nueva palabra.
* Editar palabra existente.
* Eliminar palabra existente.
* Ver listado de palabras.
* Buscar significado de palabra.
* Salir.

para su uso correcto, reemplazar las credenciales del archivo [conexion.py](https://github.com/IsaacJSandovalC/Talleres_DB_Prog4/blob/main/orm/conexion.py) por sus credenciales en MySQL de la siguiente manera:

```
engine = create_engine('mysql+pymysql://user:password@host/database')
Session = sessionmaker(bind=engine)
session = Session()
```

### Enlaces a los documentos del taller: 
* conexion.py: [Click](https://github.com/IsaacJSandovalC/Talleres_DB_Prog4/blob/main/orm/conexion.py)
* menu.py: [Click](https://github.com/IsaacJSandovalC/Talleres_DB_Prog4/blob/main/orm/menu.py)
* slangs.py: [Click](https://github.com/IsaacJSandovalC/Talleres_DB_Prog4/blob/main/orm/slangs.py)
