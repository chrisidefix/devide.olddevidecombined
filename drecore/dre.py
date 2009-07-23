# main DRE driver script

import sys

def disp_usage():
    print "Perbeer nog een keer."

def run_drepython():
    """Run the DRE Python with the environment correctly setup so that
    all DRE libraries can be imported.

    We load the dre.cfg file to get the environment settings.
    """
    pass

builtin_dreams = {'python' : run_drepython}

def main():
    # first check for builtin
    # then check for file / dir

    # simple argument checking no getopt: only sys.argv[1] is checked,
    # all subsequent arguments are passed to the called script.

    if len(sys.argv) < 2:
        disp_usage()

    dream_name = sys.argv[1]

    # check for builtin
    m = builtin_dreams.get(dream_name)
    if m is not None:
        m()




if __name__ == "__main__":
    main()


