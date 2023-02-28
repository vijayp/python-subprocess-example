#!/usr/bin/env python3

import os
import subprocess

if __name__ == '__main__':
    molecule = input('enter the name of the molecule >')
    print('The molecule name has the following number of characters')
    command_parts = ['./counter.sh', molecule]
    print(command_parts)
    subprocess.run(command_parts)
