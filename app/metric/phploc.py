from app.configuration import get_value
from app.helper import output_start, php, output_error


def execute():
    output_start('phploc')

    metric_dir = get_value('metric-dir')
    scan_dir = get_value('project-dir')+get_value('scan-dir')
    exclude_dirs = get_value('exclude-dirs')
    excludes = ''

    for exclude in exclude_dirs:
        excludes = excludes+' --exclude '+exclude

    print('>>> Metric dir: '+metric_dir)
    print('>>> Excludes: '+excludes)

    code = php('phploc', '--count-tests --log-csv '+metric_dir+'phploc.csv --log-xml '+metric_dir+'phploc.xml '+excludes+' '+scan_dir)

    if code != 0:
        output_error('There was a error/exception while executing phploc.')
