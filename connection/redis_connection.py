import redis
from connection.connect_config import config
import json

redis_host = config['redis']['host']
redis_port = config['redis']['port']

r = redis.Redis(host=redis_host, port=int(redis_port), decode_responses=True)

def add(redis_key:str, redis_data):
    r.set(redis_key, redis_data)

def search(key):
    
    value = r.get(key)
    
    if value is not None:
        cached_data = json.loads(value)
        return cached_data
    else:
        return None