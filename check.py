from app import *
from app.check import *

initialization.run()

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
