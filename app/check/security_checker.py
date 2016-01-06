from app.configuration import get_value
from app.helper import php


def execute():
    print('--- security-checker ---')

    composer_lock = get_value('project-dir')+'composer.lock'
    print('>>> composer.lock: '+composer_lock)

    code = php('security-checker.phar', 'security:check '+composer_lock)

    if code != 0:
        raise SystemExit('You have a security issue with your composer.lock')
