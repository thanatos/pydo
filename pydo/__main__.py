import argparse
import sys


def _get_locals():
    # TODO: Import a "~/.pydo" file, and run get_locals() in it to get
    # additional, user-defined locals.
    import pprint, re, sys
    import os
    from os import path
    return {
        'os': os,
        'path': path,
        'pprint': pprint.pprint,
        're': re,
    }


def main():
    parser = argparse.ArgumentParser()
    # TODO: change to -e, allow files.
    parser.add_argument('command')
    parser.add_argument('-n', action='store_true', default=False)
    parser.add_argument('-p', action='store_true', default=False)

    pargs = parser.parse_args()

    if pargs.p and pargs.n:
        print('-n and -p are mutually exclusive.', file=sys.stderr)
        sys.exit(1)

    code_obj = compile(pargs.command, '<string>', 'exec')

    locals_ = _get_locals()

    if pargs.n:
        for line in sys.stdin:
            locals_['line'] = line
            exec(code_obj, {}, locals_)
    if pargs.p:
        for line in sys.stdin:
            locals_['line'] = line
            exec(code_obj, {}, locals_)
            sys.stderr.write(locals_['line'])
    else:
        exec(code_obj, {}, locals_)


if __name__ == '__main__':
    main()


# TODO: allow looping over null-separated strings. (--null output.)
