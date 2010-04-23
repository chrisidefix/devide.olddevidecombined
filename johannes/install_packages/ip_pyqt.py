import config
from install_package import InstallPackage
import os
import shutil
import utils

VERSION = "4.7.2"
BASENAME = "PyQt"

if os.name == "nt":
    ARCHIVE_BASENAME = "%s-win-gpl-%s" % (BASENAME, VERSION)
    ARCHIVE_NAME = "%s.zip" % (ARCHIVE_BASENAME,)
else:
    ARCHIVE_BASENAME = "%s-x11-gpl-%s" % (BASENAME, VERSION)
    ARCHIVE_NAME = "%s.tar.gz" % (ARCHIVE_BASENAME,)

URL = "http://www.riverbankcomputing.com/static/Downloads/PyQt4/%s" % (ARCHIVE_NAME,)

dependencies = ['SIP', 'Qt']

class PyQt(InstallPackage):
    
    def __init__(self):
        self.archive_path = os.path.join(
                config.archive_dir, ARCHIVE_NAME)
        
        self.build_dir = os.path.join(config.build_dir, '%s-%s' %
                                      (BASENAME,VERSION))
        self.site_packages = os.path.join(config.inst_dir, 'python',
                                          'Lib', 'site-packages')

    def get(self):
        if os.path.exists(self.archive_path):
            utils.output("%s already present, skipping step." % BASENAME)
            return
        
        utils.goto_archive()
        utils.urlget(URL)
        
    def unpack(self):
        if os.path.exists(os.path.join(self.build_dir, "configure.py")):
            utils.output("%s already unpacked. Skipping." % BASENAME)
            return
        
        utils.output("Unpacking %s." % BASENAME)
        utils.unpack_build(self.archive_path)
        
        # Rename the folder:
        shutil.move(os.path.join(config.build_dir, ARCHIVE_BASENAME), 
                    self.build_dir)
        
        # Remove the examples, because somehow it crashes the build on win64
        folder = os.path.join(self.build_dir, 'examples')
        if os.path.exists(folder):
            shutil.rmtree(folder)        
        
    def configure(self):
        if os.path.exists(os.path.join(self.build_dir, 'Makefile')): #TODO
            utils.output("%s build already configured." % BASENAME)
            return
        
        os.chdir(self.build_dir)
        pre_commands = 'SET PATH=%s;%%PATH%% &SET QTDIR=%s' % (
                    config.QT_BIN, # Note: for some reason we must 
                                   # modify the PATH before applying
                                   # the Visual Studio environment, 
                                   # or nmake will not be on the PATH 
                    config.QT_DIR)
        post_commands = '%s configure.py -w' % config.PYTHON_EXECUTABLE
        communicate = 'yes\n'
        ret = utils.execute_in_vs_environment(post_commands, pre_commands,
                                              communicate)
        
        if ret != 0:
            utils.error("Could not configure %s.  Fix and try again." % BASENAME)
        
        
    def build(self):
        if os.path.exists(os.path.join(self.build_dir, 'QtCore', 'QtCore.pyd')):
            utils.output("%s already built.  Skipping build step." % BASENAME)
            return

        os.chdir(self.build_dir)
        ret = utils.execute_in_vs_environment('nmake')
        
        if ret != 0:
            utils.error("Could not build %s.  Fix and try again." % BASENAME)
    

    def install(self):
        if os.path.exists(os.path.join(self.site_packages, 'qt.py')):
            utils.output("%s already installed. Skipping step." % BASENAME)
            return

        os.chdir(self.build_dir)
        ret = utils.execute_in_vs_environment('nmake install')
        
        # We're creating a package named 'qt', so that we can import
        # qt stuff using 'from qt import QObject'
        file = open(os.path.join(self.site_packages, 'qt.py'), 'w')
        file.write("from PyQt4.Qt import *")
        file.close()
        
        if ret != 0:
            utils.error(
            "Could not install %s.  Fix and try again." % BASENAME)

 
    def clean_build(self):
        # nuke the build dir, the source dir is pristine
        utils.output("Removing build dir.")
        if os.path.exists(self.build_dir):
            shutil.rmtree(self.build_dir)

    def get_installed_version(self):
        import qt 
        return qt.PYQT_VERSION_STR
