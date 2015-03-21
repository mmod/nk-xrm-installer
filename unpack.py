#!/usr/bin/env python
# -*- coding: utf8 -*-
# __author__ = "Richard B Winters"
# __copyright__ = "Copyright 2011-2015, Massively Modified, Inc."
# __credits__ = ["Richard B Winters"]
# __license__ = "Apache-2.0"
# __maintainer__ = "Richard B Winters"
# __email__ = "support@mmogp.com"
# __status__ = "Production"

import sys
import os
import urllib
import tarfile

# Define remote url and local destination of source archive
remote = sys.argv[1] + sys.argv[2] + sys.argv[4]
archive = os.path.abspath(sys.argv[5] + sys.argv[3] + sys.argv[4])

# Fetch source archive
urllib.urlretrieve (remote, archive)

# Define output directory for decompressed source archive
destination = os.path.abspath(sys.argv[6])

# Extract
source = tarfile.open(archive,'r:gz');
source.extractall(destination)

# Relocate the source to the application rood (i.e to the directory above containing node_modules directory)


# Exit
sys.exit(0)
