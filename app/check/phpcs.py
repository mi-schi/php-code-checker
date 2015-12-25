import os
from app.configuration import get_value
from app.helper import php


def execute():
    print '--- phpcs ---'
    phpcs_standard = get_value('project-dir')+get_value('phpcs-standard')
    check_dir = get_value('check-dir')
    scan_dir = get_value('project-dir')+get_value('scan-dir')

    exclude_dirs = []
    for exclude_dir in get_value('exclude-dirs'):
        exclude_dirs.append(exclude_dir+'/*')
    excludes = ','.join(exclude_dirs)

    if not os.path.isfile(phpcs_standard):
        print '>>> No phpcs-standard found. Fallback is the default move-elevator/symfony-coding-standard:'
        phpcs_standard = os.getcwd()+'/vendor/move-elevator/symfony-coding-standard/Standards/Symfony2'

    print '>>> phpcs standard: '+phpcs_standard
    print '>>> Scan dir: '+scan_dir
    print '>>> Excludes: '+excludes

    code = php('bin/phpcs --standard='+phpcs_standard+' --extensions=php --report-checkstyle='+check_dir+'checkstyle.xml --ignore='+excludes+' '+scan_dir)

    if code == 512:
        raise SystemExit('There was a error/exception while executing phpcs.')
