import os
import urllib

security_checker = 'bin/security-checker.phar'


def initialization():
    if not os.path.isfile(security_checker):
        download()


def download():
    print '>>> Download '+security_checker
    urllib.urlretrieve('http://get.sensiolabs.org/security-checker.phar', security_checker)


def update():
    os.remove(security_checker)
    download()
