# Copyright (c) Charl P. Botha, TU Delft.
# All rights reserved.
# See COPYRIGHT for details.

import config
from install_package import InstallPackage
import os
import utils
import shutil
import sys

BASENAME = "devide"
SVN_REPO = "http://devide.googlecode.com/svn/trunk/" + BASENAME
# this should be the same release as johannes and the rest of devide
SVN_REL = config.DEVIDE_REL

dependencies = []

class DeVIDE(InstallPackage):
    
    def __init__(self):
        self.source_dir = os.path.join(config.archive_dir, BASENAME)
        self.build_dir = os.path.join(config.build_dir, BASENAME)
        self.full_version = '%s.%s.0' % (SVN_REL, config.JOHANNES_REL)
        #self.inst_dir = os.path.join(config.inst_dir,
        #                             '%s-%s' % (BASENAME,
        #                                        self.full_version))
        self.inst_dir = os.path.join(config.inst_dir, BASENAME)

        # setup some devide config variables (we need to do this in anycase,
        # because they're config vars and other modules might want them)
        config.DEVIDE_PY = os.path.join(self.inst_dir, 'devide.py')

    def get(self):
        if os.path.exists(self.source_dir):
            utils.output("DeVIDE already checked out, skipping step.")

        else:
            os.chdir(config.archive_dir)
            ret = os.system("%s co %s -r%s" % (config.SVN, SVN_REPO, SVN_REL))
            if ret != 0:
                utils.error("Could not SVN checkout DeVIDE.  "
                            "Fix and try again.")

    def unpack(self):
        """No unpack step.
        """
        pass

    def copy_devide_to_inst(self):
        # we unpack by copying the checked out tree to the build dir
        if os.path.isdir(self.inst_dir):
            utils.output(
                'DeVIDE already present in inst dir.  Skipping step.')
            return

        shutil.copytree(self.source_dir, self.inst_dir)

        # now modify the version unpacked devide.py
        utils.output("Modifying DeVIDE version")
        devide_py = os.path.join(self.inst_dir, 'devide.py')
        # we want to change DEVIDE_VERSION = '%s.%s' % (VERSION,
        # SVN_REVISION) to DEVIDE_VERSION = '%s.%s' % (VERSION,
        # "$JOHANNES_REL") 
        utils.re_sub_filter_file(
            [('(DEVIDE_VERSION\s*=.*)SVN_REVISION(.*)', '\\1"%s"\\2' %
              (config.JOHANNES_REL,))],
            devide_py)

    def build(self):
        pass

    def install(self):
        config.DEVIDE_INST_DIR = self.inst_dir
        self.copy_devide_to_inst()

    def clean_build(self):
        utils.output("Removing build and installation directories.")

        if os.path.isdir(self.inst_dir):
            shutil.rmtree(self.inst_dir)

    def get_installed_version(self):
        import sys
        sys.path.insert(0, self.inst_dir)
        import devide
        del sys.path[0]
        return devide.DEVIDE_VERSION


            
