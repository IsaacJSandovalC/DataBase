## Taller #3 MongoDB(pymongo)<a name="id3"></a>
Este trabajo se emplea utilizando Python y pymongo, se crea una colecion llamada "Slangs_db" y un documento llamado "Slangs". 

Se le agregan las funciones de:

* Agregar nueva palabra.
* Editar palabra existente.
* Eliminar palabra existente.
* Ver listado de palabras.
* Buscar significado de palabra.
* Salir.

para su uso correcto, reemplazar las credenciales del archivo [conexion.py](https://github.com/IsaacJSandovalC/Talleres_DB_Prog4/blob/main/MongoDB/conexion.py) por sus credenciales en MongoDB de la siguiente manera:

```
MONGODB_HOST = 'Host name'
MONGODB_PORT = 'Ussing port'
MONGODB_TIMEOUT = timer (colocar en enteros)
```
Posterior a estos ajustes, ejecutar el archivo llamado [menu.py](https://github.com/IsaacJSandovalC/Talleres_DB_Prog4/blob/main/MongoDB/menu.py), este creará automanticamente todas las colecciones y documentos con sus registros.
