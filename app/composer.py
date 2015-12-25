import os
from app.configuration import get_value


def initialization():
    php = get_value('php')
    if not os.path.isfile('bin/composer'):
        download(php)
    if not os.path.isfile('bin/phpunit'):
        os.system(php+' bin/composer install')


def download(php):
    if not os.path.exists('bin'):
        os.makedirs('bin')
    os.system('curl -sS https://getcomposer.org/installer | '+php+' -- --install-dir=bin --filename=composer')


def update():
    php = get_value('php')
    os.system(php+' bin/composer self-update')
    os.system(php+' bin/composer update')
