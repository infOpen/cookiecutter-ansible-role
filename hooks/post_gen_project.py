"""
Tasks must be done after project generate
"""

import os
import sys


SOURCE_PATH = 'tests/playbook.yml'
TARGET_PATH = 'playbook.yml'

try:
    if os.path.exists(TARGET_PATH):
        os.unlink(TARGET_PATH)

    os.symlink(SOURCE_PATH, TARGET_PATH)
except OSError:
    print('Symlink create error: {}'.format(TARGET_PATH))
    sys.exit(1)
