import argparse
import logging
import sys

from annea_foo import example as foo
from annea_bar import example as bar

log_format = "%(asctime)s - [%(levelname)s] [%(module)s.%(funcName)s:%(lineno)d]: %(message)s"
logging.basicConfig(format=log_format, level=logging.DEBUG)
log = logging.getLogger(__name__)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description='Annea Baz')
    parser.add_argument('--test', help='test argument', default='test', type=str)
    args = vars(parser.parse_args(args))

    log.info(args['test'])

    log.info(bar.joke())
    foo.print_joke()


if __name__ == "__main__":
    sys.exit(main())
