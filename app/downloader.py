import os

download_dict = {
    'bin/security-checker.phar': 'http://get.sensiolabs.org/security-checker.phar',
    'bin/phpmetrics.phar': 'https://github.com/Halleck45/PhpMetrics/raw/master/build/phpmetrics.phar'
}


def initialization():
    for file_bin, url in download_dict.items():
        if not os.path.isfile(file_bin):
            download(file_bin, url)


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
