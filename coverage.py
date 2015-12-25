from app import initialization
from app.configuration import add
from app.check import *

initialization.run()
add('phpunit-coverage', 'true')

phpunit.execute()
