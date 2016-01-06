import os
from app.configuration import get_value
from app.helper import php


def initialization():
    checker_dir = get_value('checker-dir')

    if not os.path.isfile(checker_dir+'bin/composer'):
        download(checker_dir)
    if not os.path.isfile(checker_dir+'bin/phpcs'):
        php('bin/composer install')


def download(checker_dir):
    php_bin = get_value('php')
    if not os.path.exists(checker_dir+'bin'):
        os.makedirs(checker_dir+'bin')
    print('>>> Download composer')
    os.system('curl -sS https://getcomposer.org/installer | '+php_bin+' -- --install-dir='+checker_dir+'bin --filename=composer')


def update():
    php('bin/composer self-update')
    php('bin/composer update')


def project_installation():
    code = php('bin/composer install --optimize-autoloader')
    if code != 0:
        raise SystemExit('The composer install command for the project failed with the code '+str(code))
