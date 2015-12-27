from app.configuration import get_value
from app.helper import php


def execute():
    print '--- phpmetrics ---'

    metric_dir = get_value('metric-dir')
    scan_dir = get_value('project-dir')+get_value('scan-dir')
    excludes = '|'.join(get_value('exclude-dirs'))

    print '>>> Metric dir: '+metric_dir
    print '>>> Excludes: '+excludes

    code = php('bin/phpmetrics.phar --extensions=php --report-xml='+metric_dir+'phpmetrics.xml --report-html='+metric_dir+'phpmetrics.html --excluded-dirs="'+excludes+'" '+scan_dir)

    if code != 0:
        raise SystemExit('There was a error/exception while executing phpmetrics.')
