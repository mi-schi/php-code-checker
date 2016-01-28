from app.configuration import get_value
from app.helper import output_start, php, output_error


def execute():
    output_start('security-checker')

    composer_lock = get_value('project-dir')+'composer.lock'
    print('>>> composer.lock: '+composer_lock)

    code = php('security-checker.phar', 'security:check '+composer_lock)

    if code != 0:
        output_error('You have a security issue with your composer.lock')
