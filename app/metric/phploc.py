from app.configuration import get_value
from app.helper import php


def execute():
    print '--- phploc ---'
    metric_dir = get_value('metric-dir')
    scan_dir = get_value('project-dir')+get_value('scan-dir')
    excludes = ' '.join(get_value('exclude-dirs'))

    print '>>> Metric dir: '+metric_dir
    print '>>> Excludes: '+excludes

    code = php('bin/phploc '+scan_dir+' --count-tests --log-csv '+metric_dir+'phploc.csv --log-xml '+metric_dir+'phploc.xml --exclude '+excludes)

    if code != 0:
        raise SystemExit('There was a error/exception while executing phploc.')
