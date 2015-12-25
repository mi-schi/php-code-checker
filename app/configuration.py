import json
import os

config = {}
default_config = {}


def load(path):
    global config
    load_default()
    composer = path+'composer.json'
    data = load_json(composer)
    config = data['extra']['php-code-checker']


def load_default():
    global default_config
    data = load_json('data/default_configuration.json')
    default_config = data['extra']['php-code-checker']


def load_json(path):
    if not os.path.isfile(path):
        raise SystemExit('The json '+path+' was not found.')
    with open(path) as data_file:
        return json.load(data_file)


def add(key, value):
    global default_config
    default_config.update({key: value})


def get_value(key):
    if key in config:
        return config[key]
    elif key in default_config:
        return default_config[key]
    else:
        raise SystemExit('The key '+key+' does not exists in the configs (composer.json and default config).')
