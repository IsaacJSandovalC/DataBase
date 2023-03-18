import redis

# Función para conectarse a Redis
def conectar_redis():
    r = redis.Redis(host='localhost', port=6379, db=0)
    return r

