import os
from app.configuration import get_value
from app.helper import php, get_dirs


def execute():
    print('--- phpcs ---')

    dirs = get_dirs()
    phpcs_standard = dirs['project']+get_value('phpcs-standard')
    check_dir = get_value('check-dir')

    exclude_dirs = []
    for exclude_dir in get_value('exclude-dirs'):
        exclude_dirs.append(exclude_dir+'/*')
    excludes = ','.join(exclude_dirs)

    if not os.path.isfile(phpcs_standard):
        print('>>> No phpcs-standard found. Fallback is the default move-elevator/symfony-coding-standard:')
        phpcs_standard = os.getcwd()+'/vendor/move-elevator/symfony-coding-standard/Standards/Symfony2'

    print('>>> phpcs standard: '+phpcs_standard)
    print('>>> Excludes: '+excludes)

    code = php('bin/phpcs --standard='+phpcs_standard+' --extensions=php --report-checkstyle='+check_dir+'checkstyle.xml --ignore='+excludes+' '+dirs['scan'])

    if code == 512:
        raise SystemExit('There was a error/exception while executing phpcs.')
