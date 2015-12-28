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
    project_dir = os.getcwd()

    if len(sys.argv) == 3:
        project_dir = sys.argv[2]

    if not project_dir.endswith('/'):
        project_dir = project_dir+'/'

    return project_dir


def get_dirs():
    project_dir = get_value('project-dir')
    scan_dir = project_dir+get_value('scan-dir')

    print('>>> Project dir: '+project_dir)
    print('>>> Scan dir: '+scan_dir)

    return {'project': project_dir, 'scan': scan_dir}
