## Taller #4 Redis<a name="id4"></a>
Este trabajo se emplea utilizando Python y la libreria de redis, se le agregan las funciones de:

* Agregar nueva clave.
* Editar clave existente.
* Eliminar clave existente.
* Buscar significado de clave.
* Salir.

para su uso correcto, reemplazar las credenciales del archivo [conexion.py](https://github.com/IsaacJSandovalC/Talleres_DB_Prog4/blob/main/redis/conexion.py) por sus credenciales en MySQL de la siguiente manera:

```
r = redis.Redis(host='tu_host', port=tu_pruerto, db=tu_db)
```

### Enlaces a los documentos del taller: 
* conexion.py: [Click](https://github.com/IsaacJSandovalC/Talleres_DB_Prog4/blob/main/redis/conexion.py)
* menu.py: [Click](https://github.com/IsaacJSandovalC/Talleres_DB_Prog4/blob/main/redis/menu.py)
* acciones.py: [Click](https://github.com/IsaacJSandovalC/Talleres_DB_Prog4/blob/main/redis/acciones.py)