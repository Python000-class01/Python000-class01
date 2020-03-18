import yaml


def getConfig():
    with open("config.yaml", 'r') as f:
        config = f.read()
    return yaml.safe_load(config)