#!/usr/bin/env python3
import os
import subprocess

if __name__ == '__main__':
    molecule = input('enter the name of the molecule >')
    print('The molecule name has the following number of characters')
    # This is bad:
    # cmd_str = 'echo "%s" | wc -c ' % molecule
    # os.system(cmd_str)
    #
    # Instead:
    echo = subprocess.run(['/bin/echo', molecule], stdout=subprocess.PIPE)
    wordcount = subprocess.run(['/usr/bin/wc', '-c'], input=echo.stdout)


