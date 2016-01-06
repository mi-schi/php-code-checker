import json
import os

config = {}
default_config = {}
extra_config = {}


def load():
    global config
    load_default()
    composer = get_value('project-dir')+'composer.json'

    if not os.path.isfile(composer):
        raise SystemExit('You have to define a composer.json in your project.')

    data = load_json(composer)

    if 'extra' in data:
        if 'php-code-checker' in data['extra']:
            config = data['extra']['php-code-checker']


def load_default():
    global default_config
    data = load_json(get_value('checker-dir')+'data/default_configuration.json')
    default_config = data['extra']['php-code-checker']


def load_json(path):
    if not os.path.isfile(path):
        raise SystemExit('The json '+path+' was not found.')
    with open(path) as data_file:
        return json.load(data_file)


def add(key, value):
    global extra_config
    extra_config.update({key: value})


def get_value(key):
    if key in extra_config:
        return extra_config[key]
    elif key in config:
        return config[key]
    elif key in default_config:
        return default_config[key]
    else:
        raise SystemExit('The key '+key+' does not exists in the configs (composer.json and default config).')
