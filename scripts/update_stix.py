#!/usr/bin/env python

import sys
import argparse
from ramrod import (__version__, update, UpdateError)

def _write_xml(tree, outfn):
    if not outfn:
        tree.write(sys.stdout, pretty_print=True)
    else:
        tree.write(outfn, pretty_print=True)


def _validate_args():
    pass


def _get_arg_parser():
    parser = argparse.ArgumentParser(description="STIX Document Updater v%s"
                                    % __version__)

    parser.add_argument("--infile", default=None, required=True,
                        help="Input XML document filename.")

    parser.add_argument("--outfile", default=None,
                        help="Output XML document filename. Prints to stdout "
                             "if no filename is provided.")

    parser.add_argument("--to", default='1.1.1',
                        help="Update STIX content to this version.")

    parser.add_argument("-f", "--force", action="store_true", default=False,
                        help="Removes untranslatable fields and attempts to "
                             "force the update process.")

    return parser

def main():
    parser = _get_arg_parser()
    args = parser.parse_args()

    try:
        _validate_args()
        updated = update(args.infile, to_=args.to, )
        _write_xml(updated, args.outfile)
    except UpdateError as ex:
        print str(ex)

if __name__ == "__main__":
    main()