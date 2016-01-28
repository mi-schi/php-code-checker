from app.configuration import get_value
from app.helper import output_start, php, output_error


def execute():
    output_start('phpmetrics')

    metric_dir = get_value('metric-dir')
    scan_dir = get_value('project-dir')+get_value('scan-dir')
    excludes = '|'.join(get_value('exclude-dirs'))

    if excludes != '':
        excludes = '--excluded-dirs="'+excludes+'"'

    print('>>> Metric dir: '+metric_dir)
    print('>>> Excludes: '+excludes)

    code = php('phpmetrics.phar', '--extensions=php --report-xml='+metric_dir+'phpmetrics.xml --report-html='+metric_dir+'phpmetrics.html '+excludes+' '+scan_dir)

    if code != 0:
        output_error('There was a error/exception while executing phpmetrics.')
