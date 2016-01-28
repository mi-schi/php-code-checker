import os
from app.configuration import get_value
from app.helper import output_start, php, get_dirs, output_error


def execute():
    output_start('phpmd')

    dirs = get_dirs()
    phpmd_xml = dirs['project']+get_value('phpmd-xml')
    check_dir = get_value('check-dir')
    excludes = ','.join(get_value('exclude-dirs'))

    if excludes != '':
        excludes = '--exclude '+excludes

    if not os.path.isfile(phpmd_xml):
        print('>>> No phpmd-xml found. Fallback is the default phpmd.xml:')
        phpmd_xml = get_value('checker-dir')+'data/phpmd.xml.dist'

    print('>>> phpmd.xml: '+phpmd_xml)
    print('>>> Excludes: '+excludes)

    code = php('phpmd', dirs['scan']+' xml '+phpmd_xml+' --reportfile '+check_dir+'pmd.xml '+excludes)

    if code == 1:
        output_error('There was a error/exception while executing phpmd.')
