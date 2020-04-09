import yaml
import os


def getConfig():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(ROOT_DIR, 'config.yaml')
    with open(CONFIG_PATH, 'r') as f:
        config = f.read()
    return yaml.safe_load(config)