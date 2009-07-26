# Copyright (c) Charl P. Botha, TU Delft.
# All rights reserved.
# See COPYRIGHT for details.

# main DRE driver script

import ConfigParser
import copy
import os
import subprocess
import sys

help_msg = """
Welcome to the DRE (DeVIDE Runtime Environment) runner.

With this programme, you can invoke DREAMs, or DRE Application
Modules, for example the DeVIDE application, a Python interpreter
enhanced with VTK, ITK and wxPython or your own applications.

Invoke as follows:
    dre dream_name [param1 param2 param3]

Where dream_name can be: 
1. One of the built-in dreams:
    devide   - Graphical medical visualisation application application builder.
    help     - Show this message.
    python   - Python interpreter with VTK, ITK, wxPython available.
    versions - Output versions of included libraries.

2. The full path to an arbitrary Python script.

3. A Python package or script located in dre-toplevel/dreams/

"""

class DRE:

    def disp_usage(self):
        print help_msg

    def helper_run_python(self, args):
        """Helper function used by built-in dreams to execute the DRE-enabled python on stuff.

        @param args: Will be passed to python as command line argumenst.
        """

        p = subprocess.Popen([self.python_bin] + args, env=self.env)
        # wait for the process to return
        p.communicate()

    def helper_args_preprocess(self):
        if len(sys.argv) > 2:
            args = sys.argv[2:]
        else:
            args = []

        return args


    def run_devide(self):
        """Built-in dream to run the DeVIDE that is packaged with the DRE.
        """
        devide_fn = os.path.join(self.dre_top, 'devide', 'devide.py')

        # if any MORE arguments were passed after "devide", pass that on
        args = self.helper_args_preprocess()

        self.helper_run_python([devide_fn] + args)

    def run_drepython(self):
        """Run the DRE Python with the environment correctly setup so that
        all DRE libraries can be imported.

        """

        # if any MORE arguments were passed after "python", pass that on
        # to the python interpreter
        args = self.helper_args_preprocess()

        self.helper_run_python(args)

    def run_versions(self):
        print "TBD."

    def run_help(self):
        print help_msg

    def run_pyfile(self, pyfilename):
        args = self.helper_args_preprocess()
        self.helper_run_python([pyfilename] + args)

    def main(self):
        # first check for builtin
        # then check for dream in dre_top/dreams/
        # then check for file / dir

        # simple argument checking no getopt: only sys.argv[1] is checked,
        # all subsequent arguments are passed to the called script.
        if len(sys.argv) < 2:
            self.disp_usage()
            return

        # now setup some variables we'll need ############################
        self.builtin_dreams = {
                'python' : self.run_drepython,
                'devide' : self.run_devide,
                'help'   : self.run_help,
                'versions' : self.run_versions}
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


        # start command-line processing ###############################
        dream_name = sys.argv[1]

        # check for builtin
        m = self.builtin_dreams.get(dream_name)
        if m is not None:
            m()

        elif os.path.exists(dream_name):
            self.run_pyfile(dream_name)

        else:
            print "Could not find specified DREAM."


if __name__ == "__main__":
    DRE().main()


