from app import initialization
from app import composer
from app.check import *

initialization.run()
composer.project_installation()

lint.execute()

coverfish.execute()
phpunit.execute()

phpcs.execute()
phpcpd.execute()
phpmd.execute()

security_checker.execute()
