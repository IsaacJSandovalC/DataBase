import pymysql

# Conexión a la base de datos
conexion = pymysql.connect(
    host='localhost',
    user='root',
    password='49P54ty8.',
    db='parcial',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

