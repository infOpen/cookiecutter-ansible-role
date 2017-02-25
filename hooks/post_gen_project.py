import os
import sys

try:
    os.symlink('tests/playbook.yml', 'playbook.yml')
except:
    print 'Symlinks create errors !'
    sys.exit(1)
