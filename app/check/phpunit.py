import os
from app.configuration import get_value


def execute():
    print '--- phpunit ---'
    check_dir = get_value('check-dir')

    if get_value('phpunit-coverage') == 'true':
        os.system(test(check_dir)+coverage(check_dir))
    else:
        os.system(test(check_dir))


def test(check_dir):
    php = get_value('php')
    phpunit_xml = get_value('project-dir')+get_value('phpunit-xml')
    phpunit_junit_xml = check_dir+'phpunit.xml'

    print '>>> Execute phpunit with php: '+php
    print '>>> phpunit.xml configuration: '+phpunit_xml
    print '>>> JUnit phpunit.xml log: '+phpunit_xml

    return php+' bin/phpunit --configuration '+phpunit_xml+' --debug --log-junit '+phpunit_junit_xml


def coverage(check_dir):
    base_dir = get_value('build-dir')
    print '>>> With coverage and crap index'

    return ' --coverage-html '+base_dir+'coverage --coverage-clover '+check_dir+'coverage.xml --coverage-crap4j '+check_dir+'crap4j.xml'
