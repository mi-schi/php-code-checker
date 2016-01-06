import os
from app.configuration import get_value

download_dict = {
    'bin/security-checker.phar': 'http://get.sensiolabs.org/security-checker.phar',
    'bin/phpmetrics.phar': 'https://github.com/Halleck45/PhpMetrics/raw/master/build/phpmetrics.phar'
}


def initialization():
    checker_dir = get_value('checker-dir')

    for file_bin, url in download_dict.items():
        absolute_file_bin = checker_dir+file_bin
        if not os.path.isfile(absolute_file_bin):
            download(absolute_file_bin, url)


def download(file_bin, url):
    print('>>> Download '+file_bin)

    try:
        import urllib.request
        urllib.request.urlretrieve(url, file_bin)
    except ImportError:
        import urllib
        urllib.urlretrieve(url, file_bin)


def update():
    for file_bin, url in download_dict.items():
        os.remove(file_bin)
        download(file_bin, url)
