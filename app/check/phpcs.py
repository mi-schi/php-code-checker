import os
from app.configuration import get_value
from app.helper import output_start, php, get_dirs, output_error


def execute():
    output_start('phpcs')

    dirs = get_dirs()
    phpcs_standard = dirs['project']+get_value('phpcs-standard')
    check_dir = get_value('check-dir')

    exclude_dirs = []
    for exclude_dir in get_value('exclude-dirs'):
        exclude_dirs.append(exclude_dir+'/*')
    excludes = ','.join(exclude_dirs)

    if excludes != '':
        excludes = '--ignore='+excludes

    if not os.path.isfile(phpcs_standard):
        print('>>> No phpcs-standard found. Fallback is the default move-elevator/symfony-coding-standard:')
        phpcs_standard = get_value('checker-dir')+'vendor/move-elevator/symfony-coding-standard/Standards/Symfony2'

    print('>>> phpcs standard: '+phpcs_standard)
    print('>>> Excludes: '+excludes)

    code = php('phpcs', '--standard='+phpcs_standard+' --extensions=php --report-checkstyle='+check_dir+'checkstyle.xml '+excludes+' '+dirs['scan'])

    if code == 512:
        output_error('There was a error/exception while executing phpcs.')
