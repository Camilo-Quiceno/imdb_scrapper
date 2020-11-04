import yaml

__config = None

def config():
    global __config
    if not __config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.safe_load(f) #carga el archivo yaml como un diccionario

    return __config