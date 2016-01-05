from app.configuration import get_value
from app.helper import php


def execute():
    print('--- pdepend ---')

    metric_dir = get_value('metric-dir')
    scan_dir = get_value('project-dir')+get_value('scan-dir')
    excludes = ','.join(get_value('exclude-dirs'))

    if excludes != '':
        excludes = '--ignore='+excludes

    print('>>> Metric dir: '+metric_dir)
    print('>>> Excludes: '+excludes)

    code = php('bin/pdepend --summary-xml='+metric_dir+'pdepend.xml --overview-pyramid='+metric_dir+'pdepend.svg --jdepend-chart='+metric_dir+'dependencies.svg '+excludes+' '+scan_dir)

    if code != 0:
        raise SystemExit('There was a error/exception while executing pdepend.')
