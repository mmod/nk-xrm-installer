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
import shutil
import errno

# Prepare paths & variables
source = os.path.abspath(sys.argv[1])
destination = os.path.abspath(sys.argv[2])
ignorables = sys.argv[3]

# Get a list of all source files and directires to copy
files = os.listdir( source )

# Copy source files to the package destination
for copyable in files:
    if copyable in ignorables:
        print('Ignorable not copied: %s' % copyable)
    else:
        copied = destination + "/" + copyable
        copyable = source + "/" + copyable
        if os.path.exists(copied):
            print('Skipping directories/files which already exist: %s' % copied)
        else:
            try:
                shutil.move(copyable, destination)
            except OSError as e:
                # The only error we should get is that destination already exists
                print('Move error: %s' % e.strerror)

print('')
print('If attempting to update source, please backup and remove the current source at:')
print('%s (exclude the node_modules directory)' % destination)
print('')

# Exit
sys.exit(0)

