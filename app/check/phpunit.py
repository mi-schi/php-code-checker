from app.configuration import get_value
from app.helper import php


def execute():
    print '--- phpunit ---'

    check_dir = get_value('check-dir')

    if get_value('phpunit-coverage') == 'true':
        code = php(test(check_dir)+coverage(check_dir))
    else:
        code = php(test(check_dir))

    if code != 0:
        raise SystemExit('Some tests failed.')


def test(check_dir):
    phpunit_xml = get_value('project-dir')+get_value('phpunit-xml')
    phpunit_junit_xml = check_dir+'phpunit.xml'

    print '>>> phpunit.xml configuration: '+phpunit_xml
    print '>>> JUnit phpunit.xml log: '+phpunit_xml

    return 'bin/phpunit --configuration '+phpunit_xml+' --debug --log-junit '+phpunit_junit_xml


def coverage(check_dir):
    base_dir = get_value('build-dir')
    print '>>> With coverage and crap index'

    return ' --coverage-html '+base_dir+'coverage --coverage-clover '+check_dir+'coverage.xml --coverage-crap4j '+check_dir+'crap4j.xml'
