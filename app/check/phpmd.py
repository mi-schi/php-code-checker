import os
from app.configuration import get_value
from app.helper import php


def execute():
    print '--- phpmd ---'
    phpmd_xml = get_value('project-dir')+get_value('phpmd-xml')
    check_dir = get_value('check-dir')
    scan_dir = get_value('project-dir')+get_value('scan-dir')
    excludes = ','.join(get_value('exclude-dirs'))

    if not os.path.isfile(phpmd_xml):
        print '>>> No phpmd-xml found. Fallback is the default phpmd.xml:'
        phpmd_xml = os.getcwd()+'/data/phpmd.xml.dist'

    print '>>> phpmd.xml: '+phpmd_xml
    print '>>> Scan dir: '+scan_dir
    print '>>> Excludes: '+excludes

    code = php('bin/phpmd '+scan_dir+' xml '+phpmd_xml+' --reportfile '+check_dir+'pmd.xml  --exclude '+excludes)

    if code == 1:
        raise SystemExit('There was a error/exception while executing phpmd.')
