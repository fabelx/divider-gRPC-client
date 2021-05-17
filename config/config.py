from configparser import ConfigParser
from pathlib import Path


def config(filepath: str = None):
    if not filepath:
        filepath = Path('..', 'config.ini')

    parser = ConfigParser(default_section='client', defaults={'host': 'localhost', 'port': '8191'})
    parser.read(filepath)

    return parser
