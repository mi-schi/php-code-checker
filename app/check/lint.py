import os
from app.configuration import get_value
from app.helper import get_dirs, output_start, output_error


def execute():
    output_start('lint')

    dirs = get_dirs()
    exclude_dirs = get_value('exclude-dirs')
    forbidden_methods = get_value('forbidden-methods')

    print('>>> Excludes dirs: ', exclude_dirs)
    print('>>> Forbidden methods: ', forbidden_methods)

    for root, dirs, files in os.walk(dirs['scan']):
        for exclude in exclude_dirs:
            if exclude in dirs:
                dirs.remove(exclude)
        for file in files:
            if file.endswith(".php"):
                php_file = os.path.join(root, file)
                code = os.system(get_value('php')+' -l '+php_file)
                if code != 0:
                    output_error('PHP lint found an error in the file '+php_file)
                check_forbidden_methods(forbidden_methods, php_file)


def check_forbidden_methods(methods, file):
    for method in methods:
        try:
            content = open(file).read().decode('utf-8')
        except AttributeError:
            content = open(file, 'r', 1, 'utf-8').read()

        if method in content:
            output_error('There is a forbidden method "'+method+'" in the file '+file)
