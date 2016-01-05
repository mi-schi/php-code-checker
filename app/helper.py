import os
import sys
from app.configuration import get_value


def php(command):
    php_bin = get_value('php')
    print('>>> Execute with php: '+php_bin)
    return os.system(php_bin+' '+command)


def get_mode():
    if len(sys.argv) < 2:
        raise SystemExit('You have to set a mode as first argument. Possible modes are all, check, metric or coverage.')

    return sys.argv[1]


def get_project_dir():
    project_dir = os.getcwd()+'/'

    if len(sys.argv) < 3:
        return project_dir

    argument_dir = sys.argv[2]

    if not argument_dir.startswith('/'):
        argument_dir = project_dir+argument_dir

    if not argument_dir.endswith('/'):
        argument_dir = argument_dir+'/'

    return argument_dir


def get_dirs():
    project_dir = get_value('project-dir')
    scan_dir = project_dir+get_value('scan-dir')

    print('>>> Project dir: '+project_dir)
    print('>>> Scan dir: '+scan_dir)

    return {'project': project_dir, 'scan': scan_dir}
