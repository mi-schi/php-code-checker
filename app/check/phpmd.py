import os
from app.configuration import get_value
from app.helper import php, get_dirs


def execute():
    print('--- phpmd ---')

    dirs = get_dirs()
    phpmd_xml = dirs['project']+get_value('phpmd-xml')
    check_dir = get_value('check-dir')
    excludes = ','.join(get_value('exclude-dirs'))

    if not os.path.isfile(phpmd_xml):
        print('>>> No phpmd-xml found. Fallback is the default phpmd.xml:')
        phpmd_xml = os.getcwd()+'/data/phpmd.xml.dist'

    print('>>> phpmd.xml: '+phpmd_xml)
    print('>>> Excludes: '+excludes)

    code = php('bin/phpmd '+dirs['scan']+' xml '+phpmd_xml+' --reportfile '+check_dir+'pmd.xml  --exclude '+excludes)

    if code == 1:
        raise SystemExit('There was a error/exception while executing phpmd.')
