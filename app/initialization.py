import sys
import os
import shutil
import composer
import configuration


def run():
    if len(sys.argv) != 2:
        raise SystemExit('Set the path to the composer.json as argument.')

    project_dir = sys.argv[1]
    build_dir = project_dir+'build/'
    check_dir = build_dir+'check/'

    configuration.load(project_dir)
    configuration.add('project-dir', project_dir)
    configuration.add('build-dir', build_dir)
    configuration.add('check-dir', check_dir)

    composer.initialization()
    prepare_dir(check_dir)


def update():
    composer.initialization()
    composer.update()


def prepare_dir(path):
    shutil.rmtree(path)
    os.makedirs(path)
