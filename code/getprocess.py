def filter_non_printable(str):
    ret=""
    for c in str:
        if ord(c) > 31 or ord(c) == 9:
            ret += c
        else:
            ret += " "
    return ret

#
# Get /proc/<cpu>/cmdline information
#
def pid_name(self, pid):
    try:
        with open(os.path.join('/proc/', pid, 'cmdline'), 'r') as pidfile:
            return filter_non_printable(pidfile.readline())

    except Exception:
        pass
        return