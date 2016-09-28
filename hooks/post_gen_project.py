import os
import sys

try:
    os.symlink('tests/testing_deployment.yml', 'testing_deployment.yml')
except:
    print 'Symlinks create errors !'
    sys.exit(1)
