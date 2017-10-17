""" Generate new files from templates. """
import argparse
import sys
from typing import Optional
from contextlib import contextmanager
import os
from itertools import chain
from cjrh_template import Template
import biodome


__version__ = '2017.10.1'


@contextmanager
def file_or_stdout(args):
    if args.stdout:
        f = sys.stdout
    else:
        f = open(args.template.rpartition('.')[0], 'w+')
    try:
        yield f
    finally:
        if f is not sys.stdout:
            f.close()


def subs(args):
    paths = biodome.environ.get('TEMPLITZ_PATH', '').split(os.pathsep)
    # Current dir first, and dir of templitz.py as last resort
    paths = chain([os.getcwd()], paths, [os.path.dirname(__file__)])
    possibles = (os.path.join(p, args.template) for p in paths)
    for hit in possibles:
        if os.path.exists(hit):
            break
    else:
        print(f'Error: template "{args.template}" not found in any of '
              f'the following locations:')
        for p in paths:
            print(f'    {p}')
        return

    with open(hit) as f:
        data = f.read()

    tmpl = Template(data)
    print('The template has the following vars: ')
    for ph in tmpl.placeholders():
        print(ph)
        print('   ${%s}' % ph)

    output = tmpl.safe_substitute({})

    with file_or_stdout(args) as f:
        f.write(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template', required=True)
    parser.add_argument('-s', '--stdout', action='store_true')
    args = parser.parse_args()
    subs(args)


if __name__ == '__main__':
    main()
