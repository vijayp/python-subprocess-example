#!/usr/bin/env python3

import os
import shlex

if __name__ == '__main__':
    molecule = input('enter the name of the molecule >')
    print('The molecule name has the following number of characters')
    cmd_str = './counter.sh %s' % shlex.quote(molecule)
    print(cmd_str)
    os.system(cmd_str)
