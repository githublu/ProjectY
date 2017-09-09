import sys

debug = False


def log_info(message):
    print(message)


def log_error(error):
    sys.exit("Exit with exception: %s" % error)

def log_warning(warning):
    print("WARNING: %s" % warning)

def log_debug(message):
    if debug:
        print(message)

def is_debug():
    return debug
