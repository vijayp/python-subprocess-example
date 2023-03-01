#!/usr/bin/env python3

import subprocess
import glob
if __name__ == '__main__':

    path = './*'
    # instead of os.system('ls %s' % path), do the following:
    matching_files = glob.glob(path)
    command_parts = ['/bin/ls'] + matching_files
    subprocess.run(command_parts)
