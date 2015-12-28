import os
import shutil
from app import composer, configuration, downloader


def run(project_dir):
    execution_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]+'/'
    os.chdir(execution_dir)

    print('>>> Execution dir: '+execution_dir)
    print('>>> Project dir: '+project_dir)

    build_dir = project_dir+'build/'

    configuration.load(project_dir)
    configuration.add('project-dir', project_dir)
    configuration.add('build-dir', build_dir)

    composer.initialization()
    downloader.initialization()


def update(php_bin):
    print('>>> PHP version is: '+php_bin)

    configuration.add('php', php_bin)
    composer.initialization()
    composer.update()
    downloader.update()


def prepare_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.makedirs(path)
