import logging

from annea_foo import example as foo
from annea_bar import example as bar

log_format = "%(asctime)s - [%(levelname)s] [%(module)s.%(funcName)s:%(lineno)d]: %(message)s"
logging.basicConfig(format=log_format, level=logging.DEBUG)
log = logging.getLogger(__name__)

if __name__ == '__main__':
    log.info(bar.joke())
    foo.print_joke()
