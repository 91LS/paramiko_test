from __future__ import print_function
import sys
from time import sleep


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


for i in range(10):
    print(f'out: {i}')
    eprint(f'err: {i}')
    sleep(1)
