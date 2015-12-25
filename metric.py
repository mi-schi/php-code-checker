from app import *
from app.metric import *

initialization.run()

metric_dir = configuration.get_value('build-dir')+'metric/'
configuration.add('metric-dir', metric_dir)
initialization.prepare_dir(metric_dir)

phploc.execute()
phpmetrics.execute()
pdepend.execute()
