import os
from app.configuration import get_value
import xml.etree.ElementTree


def execute():
    print '--- coverfish ---'
    php = get_value('php')

    project_dir = get_value('project-dir')
    phpunit_xml = project_dir+get_value('phpunit-xml')
    phpunit_xml_folder = os.path.dirname(phpunit_xml)

    root = xml.etree.ElementTree.parse(phpunit_xml).getroot()
    output_level = get_value('coverfish-output-level')
    autoload = phpunit_xml_folder+'/'+root.get('bootstrap', False)

    if autoload is False:
        raise SystemExit('You have to define the bootstrap attribute in you phpunit.yml in the root node.')

    for testsuites in root.findall('testsuites'):
        for testsuite in testsuites:
            for directory in testsuite:
                scan_path = phpunit_xml_folder+'/'+directory.text

                print '>>> Execute coverfish with php: '+php
                print '>>> coverfish scan path: '+scan_path
                print '>>> coverfish autoload file: '+autoload

                os.system(php+' bin/coverfish scan --raw-scan-path='+scan_path+' --raw-autoload-file='+autoload+' --output-level='+output_level+' --no-ansi')




