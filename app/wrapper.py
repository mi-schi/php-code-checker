from app import configuration, initialization, composer
from app.check import *
from app.metric import *


def check():
    check_dir = configuration.get_value('build-dir')+'check/'
    configuration.add('check-dir', check_dir)
    initialization.prepare_dir(check_dir)

    composer.project_installation()

    lint.execute()

    coverfish.execute()
    phpunit.execute()

    phpcs.execute()
    phpcpd.execute()
    phpmd.execute()

    security_checker.execute()


def metric():
    metric_dir = configuration.get_value('build-dir')+'metric/'
    configuration.add('metric-dir', metric_dir)
    initialization.prepare_dir(metric_dir)

    phploc.execute()
    phpmetrics.execute()
    pdepend.execute()


def coverage():
    configuration.add('phpunit-coverage', 'true')

    phpunit.execute()
