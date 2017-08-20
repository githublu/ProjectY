import sys

debug = 0


def log_info(message):
    print(message)


def log_error(error):
    sys.exit("Exit with exception: %s" % error)

def log_warning(warning):
    print("WARNING: %s" % warning)

def log_debug(message):
    if debug == 1:
        print(message)
