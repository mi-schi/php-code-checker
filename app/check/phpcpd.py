from app.configuration import get_value
from app.helper import php


def execute():
    print '--- phpcpd ---'
    check_dir = get_value('check-dir')
    scan_dir = get_value('project-dir')+get_value('scan-dir')
    exclude_dirs = get_value('exclude-dirs')
    excludes = ''

    for exclude in exclude_dirs:
        excludes = excludes+' --exclude '+exclude

    print '>>> Scan dir: '+scan_dir
    print '>>> Excludes: '+excludes

    php('bin/phpcpd '+excludes+' --log-pmd '+check_dir+'pmd-cpd.xml '+scan_dir)
