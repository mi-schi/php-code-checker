import os
from app.configuration import get_value
from app.helper import php


def initialization():
    if not os.path.isfile('bin/composer'):
        download()
    if not os.path.isfile('bin/phpunit'):
        php('bin/composer install')


def download():
    php_bin = get_value('php')
    if not os.path.exists('bin'):
        os.makedirs('bin')
    print '>>> Download composer'
    os.system('curl -sS https://getcomposer.org/installer | '+php_bin+' -- --install-dir=bin --filename=composer')


def update():
    php('bin/composer self-update')
    php('bin/composer update')


def project_installation():
    base_dir = os.getcwd()
    os.chdir(get_value('project-dir'))
    code = php(base_dir+'/bin/composer install --optimize-autoloader')
    os.chdir(base_dir)
    if code != 0:
        raise SystemExit('The composer install command for the project failed with the code '+str(code))
