import os
from app.configuration import get_value


def php(command):
    php_bin = get_value('php')
    print '>>> Execute with php: '+php_bin
    return os.system(php_bin+' '+command)


def get_dirs():
    project_dir = get_value('project-dir')
    scan_dir = project_dir+get_value('scan-dir')

    print '>>> Project dir: '+project_dir
    print '>>> Scan dir: '+scan_dir

    return {'project': project_dir, 'scan': scan_dir}
