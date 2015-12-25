import os
from app.configuration import get_value


def execute():
    print '--- lint ---'
    php = get_value('php')
    project_dir = get_value('project-dir')
    exclude_dirs = get_value('exclude-dirs')
    forbidden_methods = get_value('forbidden-methods')

    print '>>> Excludes dirs: ',exclude_dirs
    print '>>> Forbidden methods: ',forbidden_methods

    for root, dirs, files in os.walk(project_dir):
        for exclude in exclude_dirs:
            if exclude in dirs:
                dirs.remove(exclude)
        for file in files:
            if file.endswith(".php"):
                php_file = os.path.join(root, file)
                os.system(php+' -l '+php_file)
                check_forbidden_methods(forbidden_methods, php_file)


def check_forbidden_methods(methods, file):
    for method in methods:
        if method in open(file).read():
            raise SystemExit('There is a forbidden method "'+method+'" in the file '+file)
