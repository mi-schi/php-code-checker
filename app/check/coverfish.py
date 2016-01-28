import os
import xml.etree.ElementTree
from app.configuration import get_value
from app.helper import output_start, php, output_error


def execute():
    output_start('coverfish')

    phpunit_xml = get_value('project-dir')+get_value('phpunit-xml')
    phpunit_xml_folder = os.path.dirname(phpunit_xml)

    root = xml.etree.ElementTree.parse(phpunit_xml).getroot()
    output_level = get_value('coverfish-output-level')
    bootstrap = root.get('bootstrap', False)

    if bootstrap is False:
        output_error('You have to define the bootstrap attribute in you phpunit.yml in the root node.')

    autoload = phpunit_xml_folder+'/'+bootstrap

    for testsuites in root.findall('testsuites'):
        for testsuite in testsuites:
            for directory in testsuite:
                scan_path = phpunit_xml_folder+'/'+directory.text
                if not os.path.isdir(scan_path):
                    output_error('Only directories are supported in the phpunit.xml in the testsuites.')

                print('>>> coverfish scan path: '+scan_path)
                print('>>> coverfish autoload file: '+autoload)

                code = php('coverfish', 'scan --raw-scan-path='+scan_path+' --raw-autoload-file='+autoload+' --output-level='+output_level+' --no-ansi')

                if code != 0:
                    output_error('The coverfish command failed with the code '+str(code))




