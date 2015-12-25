import os
from app.configuration import get_value


def php(command):
    php_bin = get_value('php')
    print '>>> Execute with php: '+php_bin
    return os.system(php_bin+' '+command)
