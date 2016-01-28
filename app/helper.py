import os
import sys
from app.configuration import get_value


def output_start(message):
    print('')
    print('-------------')
    print(message)
    print('-------------')


def php(command, arguments):
    project_dir = get_value('project-dir')
    bin_dir = get_value('bin-dir')
    execution_command = get_full_dir(project_dir+bin_dir)+command

    if not os.path.isfile(execution_command):
        execution_command = get_value('checker-dir')+'bin/'+command

    command = get_value('php')+' '+execution_command+' '+arguments
    print('>>> Execute command: '+command)

    return os.system(command)


def output_error(message):
    print('')
    print('!!!!!!!! - ERROR - !!!!!!!!')
    print('')
    print(message)
    print('')
    print('!!!!!!!! - ERROR - !!!!!!!!')
    print('')
    raise SystemExit()


def get_mode():
    if len(sys.argv) < 2:
        output_error('You have to set a mode as first argument. Possible modes are all, check, metric or coverage.')

    return sys.argv[1]


def get_project_dir():
    project_dir = os.getcwd()+'/'

    if len(sys.argv) < 3:
        return project_dir

    argument_dir = sys.argv[2]

    if not argument_dir.startswith('/'):
        argument_dir = project_dir+argument_dir

    return get_full_dir(argument_dir)


def get_full_dir(dir):
    if not dir.endswith('/'):
        dir = dir+'/'

    return dir


def get_dirs():
    project_dir = get_value('project-dir')
    scan_dir = project_dir+get_value('scan-dir')

    print('>>> Project dir: '+project_dir)
    print('>>> Scan dir: '+scan_dir)

    return {'project': project_dir, 'scan': scan_dir}
