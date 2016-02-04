import os
import shutil
from app import composer, configuration, downloader, helper
import sys


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)


def run(project_dir):
    os.chdir(project_dir)

    add_project_dir(project_dir)
    add_checker_dir()

    configuration.add('build-dir', project_dir+'build/')
    configuration.load()

    composer.initialization()
    downloader.initialization()


def update(php_bin):
    print('>>> PHP version is: '+php_bin)

    add_project_dir(helper.get_project_dir())
    add_checker_dir()

    configuration.add('php', php_bin)
    configuration.load_default()

    composer.initialization()
    composer.update()
    downloader.update()


def add_project_dir(project_dir):
    print('>>> Project dir: '+project_dir)
    configuration.add('project-dir', project_dir)


def add_checker_dir():
    checker_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]+'/'
    print('>>> Checker dir: '+checker_dir)
    configuration.add('checker-dir', checker_dir)


def prepare_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.makedirs(path)
