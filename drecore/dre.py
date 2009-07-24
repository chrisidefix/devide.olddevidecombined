# main DRE driver script

import ConfigParser
import copy
import os
import subprocess
import sys



class DRE:

    def disp_usage(self):
        print "Perbeer nog een keer."

    def run_drepython(self):
        """Run the DRE Python with the environment correctly setup so that
        all DRE libraries can be imported.

        """

        # if any MORE arguments were passed after "python", pass that on
        # to the python interpreter
        if len(sys.argv) > 2:
            args = sys.argv[2:]
        else:
            args = []

        p = subprocess.Popen([self.python_bin] + args, env=self.env)
        p.communicate()

    def main(self):
        # first check for builtin
        # then check for file / dir

        # simple argument checking no getopt: only sys.argv[1] is checked,
        # all subsequent arguments are passed to the called script.
        if len(sys.argv) < 2:
            self.disp_usage()
            return

        # now setup some variables we'll need ############################
        self.builtin_dreams = {'python' : self.run_drepython}
        # first determine the directory containing dre.py
        self.dre_top = os.path.abspath(os.path.dirname(sys.argv[0]))

        if os.name == 'nt':
            self.python_bin = os.path.join(self.dre_top, 'python', 'python.exe')
        elif os.name == 'posix':
            self.python_bin = os.path.join(self.dre_top, 'python', 'bin', 'python')
        else:
            # if nothing else works, we use the python that's executing this script
            # should be the right one in most cases
            self.python_bin = sys.executable 

        # read the DRE configuration file
        cp = ConfigParser.ConfigParser({'dre_top' : self.dre_top})
        cf = open(os.path.join(self.dre_top, 'dre.cfg'),'r')
        cp.readfp(cf)
        # get the specified environment from dre.cfg and merge it with the existing environment.
        self.env = copy.deepcopy(os.environ)
        for sec in cp.sections():
            if sec.startswith('env:'):
                env_var = sec[4:].upper()
                # love the python:
                # get all values from this section of the config file
                # append them altogether with either ; or : in between, 
                # depending on OS
                elems = os.pathsep.join([i[1] for i in cp.items(sec)])
                self.env[env_var] = elems


        dream_name = sys.argv[1]

        # check for builtin
        m = self.builtin_dreams.get(dream_name)
        if m is not None:
            m()




if __name__ == "__main__":
    DRE().main()


