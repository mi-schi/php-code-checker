import sys
import os
import shutil
import composer
import configuration
import downloader


def run():
    if len(sys.argv) != 2:
        raise SystemExit('Set the path to the composer.json as argument.')

    project_dir = sys.argv[1]
    build_dir = project_dir+'build/'

    configuration.load(project_dir)
    configuration.add('project-dir', project_dir)
    configuration.add('build-dir', build_dir)

    composer.initialization()
    downloader.initialization()


def update():
    if len(sys.argv) != 2:
        raise SystemExit('Set the path to php as argument.')

    configuration.add('php', sys.argv[1])
    composer.initialization()
    composer.update()
    downloader.update()


def prepare_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.makedirs(path)
