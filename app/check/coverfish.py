import os
import xml.etree.ElementTree
from app.configuration import get_value
from app.helper import php


def execute():
    print '--- coverfish ---'

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

                print '>>> coverfish scan path: '+scan_path
                print '>>> coverfish autoload file: '+autoload

                code = php('bin/coverfish scan --raw-scan-path='+scan_path+' --raw-autoload-file='+autoload+' --output-level='+output_level+' --no-ansi')

                if code != 0:
                    raise SystemExit('The coverfish command failed with the code '+str(code))




