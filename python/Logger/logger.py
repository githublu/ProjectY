import sys

debug = 1


def log_info(message):
    print(message)


def log_error(error):
    sys.exit("Exit with exception: %s" % error)


def log_debug(message):
    if debug == 1:
        print(message)
