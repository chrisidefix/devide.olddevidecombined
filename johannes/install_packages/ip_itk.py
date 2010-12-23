# Copyright (c) Charl P. Botha, TU Delft.
# All rights reserved.
# See COPYRIGHT for details.

import config
from install_package import InstallPackage
import os
import shutil
import utils
import sys

BASENAME = "Insight"
# password part of REPO spec
CVS_REPO = ":pserver:anonymous:insight@www.itk.org:/cvsroot/" + BASENAME
CVS_VERSION = "-r ITK-3-20" # 

CS_BASENAME = "CableSwig"
# password part of REPO spec
CS_CVS_REPO = ":pserver:anonymous@www.itk.org:/cvsroot/" + CS_BASENAME
CABLESWIG_CVS_VERSION = "-r ITK-3-20"

dependencies = ['CMake']


class ITK(InstallPackage):
    
    def __init__(self):
        self.source_dir = os.path.join(config.archive_dir, BASENAME)
        self.build_dir = os.path.join(config.build_dir, '%s-build' %
                                      (BASENAME,))
        self.inst_dir = os.path.join(config.inst_dir, BASENAME)
        
        # ITK external packages will need this
        config.ITK_INSTALL_PREFIX = os.path.join(self.inst_dir)
        # on Windows, contains the main ITK dlls
        config.ITK_BIN = os.path.join(self.inst_dir, 'bin')
        # this is the dir with the cmake config and on *ix the main
        # SOs (on Win these are in ITK_BIN)
        config.ITK_DIR = os.path.join(self.inst_dir, 'lib/InsightToolkit')
        if os.name == 'posix':
            itd = 'itkTestDriver'
        elif os.name == 'nt':
            itd = 'itkTestDriver.exe'

        config.ITK_TEST_DRIVER = os.path.join(
                config.ITK_BIN, itd)
    
    def get(self):
        if os.path.exists(self.source_dir):
            utils.output("ITK already checked out, skipping step.")

        else:
            os.chdir(config.archive_dir)
            ret = os.system("%s -d %s co %s %s" %
                            (config.CVS, CVS_REPO, CVS_VERSION, BASENAME))
            
            if ret != 0:
                utils.error("Could not CVS checkout ITK.  Fix and try again.")

        # also the source dir for other installpackages that wish to build
        # WrapITK external projects
        # itkvtkglue needs this during its get() stage!
        config.WRAPITK_SOURCE_DIR = os.path.join(self.source_dir,
                                             'Wrapping/WrapITK')

    def unpack(self):
        pass

    def configure(self):
        if os.path.exists(
            os.path.join(self.build_dir, 'CMakeFiles/cmake.check_cache')):
            utils.output("ITK build already configured.")
            return
        
        if not os.path.exists(self.build_dir):
            os.mkdir(self.build_dir)

        # ITK_USE_REVIEW *must* be on for ItkVtkGlue to work!
        # following types are wrapped:
        # complex_float, float, signed_short, unsigned long,
        # vector_float 
        cmake_params = "-DBUILD_EXAMPLES=OFF " \
                       "-DBUILD_SHARED_LIBS=ON " \
                       "-DBUILD_TESTING=OFF " \
                       "-DCMAKE_BUILD_TYPE=RelWithDebInfo " \
                       "-DCMAKE_INSTALL_PREFIX=%s " \
                       "-DITK_USE_REVIEW=ON " \
                       "-DITK_USE_REVIEW_STATISTICS=ON " \
                       "-DITK_USE_ORIENTED_IMAGE_DIRECTION=ON " \
                       "-DITK_IMAGE_BEHAVES_AS_ORIENTED_IMAGE=ON " \
                       "_DITK_USE_CENTERED_PIXEL_COORDINATES_CONSISTENTLY=ON " \
                                              % (self.inst_dir,)
        
        ret = utils.cmake_command(self.build_dir, self.source_dir,
                cmake_params)

        if ret != 0:
            utils.error("Could not configure ITK.  Fix and try again.")

    def build(self):
        
        posix_file = os.path.join(self.build_dir,
                'bin/libITKCommon.so')

        nt_file = os.path.join(self.build_dir, 'bin',
                config.BUILD_TARGET, 
                'ITKCommon.dll')

        if utils.file_exists(posix_file, nt_file):
            utils.output("ITK already built.  Skipping build step.")

        else:
            os.chdir(self.build_dir)
            ret = utils.make_command('ITK.sln')
            if ret != 0:
                utils.error("Error building ITK.  Fix and try again.")

    def install(self):
        nt_file = os.path.join(config.ITK_BIN, 'ITKCommon.dll')
        posix_file = os.path.join(
                config.ITK_DIR, 'libITKCommon.so')
       
        if utils.file_exists(posix_file, nt_file):
            utils.output("ITK already installed.  Skipping step.")

        else:
            os.chdir(self.build_dir)
            # really sad, ITK 3.4 on Windows rebuilds the whole ITK
            # when I request an INSTALL
            ret = utils.make_command('ITK.sln', install=True) 

            if ret != 0:
                utils.error("Could not install ITK.  Fix and try again.")


    def clean_build(self):
        utils.output("Removing build and installation directories.")
        if os.path.exists(self.inst_dir):
            shutil.rmtree(self.inst_dir)

        if os.path.exists(self.build_dir):
            shutil.rmtree(self.build_dir)

    def clean_install(self):
        utils.output("Removing installation directory.")
        if os.path.exists(self.inst_dir):
            shutil.rmtree(self.inst_dir)

    def get_installed_version(self):
        import itk
        return itk.Version.GetITKVersion()
       

        

        
