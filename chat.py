import redis
import json


REDIS_HOST = 'de.futoke.ru'
REDIS_PORT = 6379
PIPE_NAME = 'itmo'

def init_chat():
    connector = redis.StrictRedis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=0,
        username='default',
        password='itmoredis',
        charset='utf-8',
        decode_responses=True
    )

    reader = connector.pubsub()
    reader.subscribe(PIPE_NAME)
    return connector, reader

def send_msg(msg):
    connector.publish(PIPE_NAME, 
                      json.dumps(msg))

def read_msgs(callback):
    for msg in reader.listen():
        if type(msg['data']) is int:
            continue
        msg = json.loads(msg['data'])
        callback(f"{msg['user']}:\n{msg['text']}")

connector, reader = init_chat()