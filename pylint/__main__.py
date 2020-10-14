# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

#!/usr/bin/env python
import os
import sys

sys.path.append('/'.join(sys.argv[0].split('/')[:-2]))
import pylint


if __name__ == "__main__":

    if sys.path[0] == "" or sys.path[0] == os.getcwd():
        sys.path.pop(0)

    pylint.run_pylint()
