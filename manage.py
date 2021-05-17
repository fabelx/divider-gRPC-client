import sys

from client.client import run
from config import config

if __name__ == '__main__':
    config = config()
    host = config.get('client', 'host')
    port = config.get('client', 'port')
    run(target=f'{host}:{port}', x=int(sys.argv[1]), y=int(sys.argv[2]))
