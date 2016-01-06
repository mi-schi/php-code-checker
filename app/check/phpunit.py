from app.configuration import get_value
from app.helper import php


def execute():
    print('--- phpunit ---')

    check_dir = get_value('check-dir')
    argument = get_test_argument(check_dir)

    if get_value('phpunit-coverage') == 'true':
        argument = argument+get_coverage_argument(check_dir)

    code = php('phpunit', argument)

    if code != 0:
        raise SystemExit('Some tests failed.')


def get_test_argument(check_dir):
    phpunit_xml = get_value('project-dir')+get_value('phpunit-xml')
    phpunit_junit_xml = check_dir+'phpunit.xml'

    print('>>> phpunit.xml configuration: '+phpunit_xml)
    print('>>> JUnit phpunit.xml log: '+phpunit_xml)

    return '--configuration '+phpunit_xml+' --debug --log-junit '+phpunit_junit_xml


def get_coverage_argument(check_dir):
    base_dir = get_value('build-dir')
    print('>>> With coverage and crap index')

    return ' --coverage-html '+base_dir+'coverage --coverage-clover '+check_dir+'coverage.xml --coverage-crap4j '+check_dir+'crap4j.xml'
