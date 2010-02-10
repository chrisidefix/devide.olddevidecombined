# Copyright (c) Charl P. Botha, TU Delft.
# All rights reserved.
# See COPYRIGHT for details.

import ConfigParser
import config
import getopt
import os
import sys
import utils

def usage():
    message = """
Welcome to johannes, the ugliest
downloading/unpacking/configuring/building and installation system of
them all.  It could save you a lot of time though.  This instance of
johannes will get, build and install the following: python, numpy,
wxpython, matplotlib, cmake, dcmtk, vtk, vtktudoss, vtkdevide, itk,
itktudoss, itkvtkglue, devide

Please read the included README.txt file NOW.

Build method A (the default) is as follows: Before starting
johannes.py, first run bootstrap_stage1.sh and bootstrap_stage2.sh to
download and install python.  After that, run johannes as follows:

/you/new/python johannes.py -w working_directory

Options are as follows:
-w, --working-dir      : specify working directory [REQUIRED]
-h, --help             : show this help
-m, --mode             : working mode, 'everything' (default),
                         'clean_build', 'get_only' or 'configure_only'
-p, --install-packages : specify comma-separated list of packages to work on,
                         default all.  Example: -p "CMake,CableSwig"
                         Correct capitalisation IS important!
--no-win-prereq        : do NOT do Windows prerequisites check.
-v, --versions         : display installed versions of all packages.

All of this ugliness is copyright 2006-2010 Charl P. Botha http://cpbotha.net/
and is hereby put under a BSD license.
"""

    print message

def posix_prereq_check(working_dir):
    """Perform posix system check for prerequisite software.

    Largest part of this checking is done in the second bootstrap
    shell script (executed before this file).  Here we check for basic
    stuff like cvs, svn and patch.
    """

    v = utils.find_command_with_ver(
            'CVS', '%s -v' % (config.CVS,),
            '\(CVS\)\s+(.*)\s+')

    v = v and utils.find_command_with_ver(
            'Subversion (SVN)', '%s --version' % (config.SVN,),
            'version\s+(.*)$')

    v = v and utils.find_command_with_ver(
            'patch', '%s -v' % (config.PATCH,),
            '^patch\s+(.*)$')

    # now check that working_dir contains the required subdirs
    dv = True
    for wsub in ['archive', 'build', 'inst']:
        cdir = os.path.join(working_dir, wsub)
        if os.path.isdir(cdir):
            msg = '%s exists.' % (cdir,)
        else:
            msg = '%s does not exist.' % (cdir,)
            dv = False

        utils.output(msg)

    return v and dv


def windows_prereq_check(working_dir):
    """Perform Windows system check for prerequisite software and
    directory structure.
    """

    utils.output("Windows prerequisites check", 70, '#')

    v = utils.find_command_with_ver(
            'MS Visual Studio', '%s /?' % (config.DEVENV,), 
            'Visual Studio Version (.*)\.$')

    #v = v and utils.find_command_with_ver(
    #        'CMake', '%s --version' % (config.CMAKE_BINPATH,),
    #        '^cmake version\s+(.*)$')

    v = v and utils.find_command_with_ver(
            'CVS', '%s -v' % (config.CVS,),
            '\((CVS|CVSNT)\)\s+(.*)\s+')

    v = v and utils.find_command_with_ver(
            'Subversion (SVN)', '%s --version' % (config.SVN,),
            'version\s+(.*)$')

    v = v and utils.find_command_with_ver(
            'patch', '%s -v' % (config.PATCH,),
            '^patch\s+(.*)$')

    # now check that setuptools is NOT installed (it screws up
    # everything on Windows)
    try:
        import setuptools
    except ImportError:
        # this is what we want
        utils.output(
                'setuptools not found. Good!')
        sut_v = True
    else:
        utils.output(
                """setuptools is installed.  
                This will break the complete DeVIDE build.  
                Please uninstall by doing:
                \Python25\Scripts\easy_install -m setuptools
                del \Python25\Lib\site-packages\setuptools*.*
                You can reinstall later by using ez_setup.py again.
                """)
        sut_v = False


    # now check that working_dir contains the required subdirs
    dv = True
    for wsub in ['archive', 'build', 'inst']:
        cdir = os.path.join(working_dir, wsub)
        if os.path.isdir(cdir):
            msg = '%s exists.' % (cdir,)
        else:
            msg = '%s does not exist.' % (cdir,)
            dv = False

        utils.output(msg)

    return v and sut_v and dv


def main():

    if len(sys.argv) < 2:
        usage()

    else:
        rpad = 60
        rpad_char = '+'

        # this is the default list of install packages
        #
        # you can override this by:
        # - specifying packages on the johannes command line
        # - specifying packages in the working dir johannes.py
        # (command line has preference over config file)
        #
        # capitalisation has to match the capitalisation of your
        # install package class, name of install package module is
        # exactly that, but all lower case, so e.g. MyModule will
        # become: install_packages.ip_mymodule.MyModule()
        #
        # johannes will:
        # - attempt to import the ip_name from install_packages
        # - instantiate ip_name.Name
        #
        ip_names = [
                'NumPy', 
                'WXPython',
                'matplotlib', 
                'CMake', 
                'DCMTK',
                'VTK', 
                'IPython', 
                'VTKTUDOSS', 
                'VTKDEVIDE', 
                'ITK', 
                'SWIG',
                'CableSwig',
                'WrapITK',
                'ItkVtkGlue', 
                'itkPyBuffer', 
                'ITKTUDOSS',
                'GDCM',  
                'DeVIDE',
                'SetupEnvironment', 
                ]




        try:
            optlist, args = getopt.getopt(
                sys.argv[1:], 'hm:p:w:v',
                ['help', 'mode=', 'install-packages=', 
                    'working-dir=',
                    'no-prereq-check', 'versions'])

        except getopt.GetoptError,e:
            usage()
            return

        mode = 'everything'
        #ip_names = None
        working_dir = None
        profile = 'default'
        no_prereq_check = False
        ip_names_cli = False
        
        for o, a in optlist:
            if o in ('-h', '--help'):
                usage()
                return

            elif o in ('-m', '--mode'):
                if a in ('clean', 'clean_build'):
                    mode = 'clean_build'
                elif a in ['get_only', 'unpack_only',
                        'configure_only']:
                    mode = a

            elif o in ('--install-packages'):
                # list of package name to perform the action on
                ip_names = [i.strip() for i in a.split(',')]
                # remember that the user has specified ip_names on the command-line
                ip_names_cli = True

            elif o in ('-w', '--working-dir'):
                working_dir = a

            elif o in ('--profile'):
                profile = a

            elif o in ('--no-prereq-check'):
                no_prereq_check = True

            elif o in ('-v', '--versions'):
                mode = 'show_versions'

        # we need at LEAST a working directory
        if not working_dir:
            usage()
            return

        # init config (DURR)
        config.init(working_dir, profile)

        # now try to read johannes config file from the working dir
        cp = ConfigParser.ConfigParser()
        # returns list of filenames successfully parsed
        cfgfns = cp.read(os.path.join(working_dir, 'johannes.cfg'))
        if cfgfns:
            if not ip_names_cli:
                # first packages that need to be installed
                # we only do this if the user has NOT specified install
                # packages on the command line.
                ip_names = [i.strip() 
                        for i in cp.get('default', 'packages').split(',')]

            # also try to read extra install package paths
            # FIXME

        # if user is asking for versions, we don't do the
        # prerequisites check as we're not going to build anything
        if mode == 'show_versions':
            no_prereq_check = True

        if os.name == 'nt' and not no_prereq_check:
            if not windows_prereq_check(working_dir):
                utils.output(
                     'Windows prerequisites do not check out.  '
                     'Fix and try again.', 70, '-')
                return
            else:
                utils.output(
                        'Windows prerequisites all good.', 70, '-')

        elif os.name == 'posix' and not no_prereq_check:
            if not posix_prereq_check(working_dir):
                utils.output(
                     'Posix prerequisites do not check out.  '
                     'Fix and try again.', 70, '-')
                return
            else:
                utils.output(
                        'Posix prerequisites all good.', 70, '-')



        ip_instance_list = []
        for ip_name in ip_names:
            # turn Name into ip_name
            ip_name_l = 'ip_' + ip_name.lower()
            # emulate:
            # from install_packages import ip_name
            ips_m = __import__('install_packages', globals(), locals(),
                    [ip_name_l])
            # this still gives you install_packages, with ip_name ivar
            # so now get out the the ip_name module itself
            ip_m = getattr(ips_m, ip_name_l)
            # instantiate
            ip_instance_list.append(getattr(ip_m, ip_name)())


        #ip_instance_list = [ip_numpy.NumPy(),
        #                    ip_wxpython.WXPython(),
        #                    ip_matplotlib.matplotlib(),
        #                    ip_cmake.CMake(),
        #                    ip_dcmtk.DCMTK(),
        #                    ip_vtk.VTK(),
        #                    ip_ipython.IPython(),
        #                    ip_vtktudoss.VTKTUDOSS(),
        #                    ip_vtkdevide.VTKDEVIDE(),
        #                    ip_itk.ITK(),
        #                    ip_swig.SWIG(),
        #                    ip_cableswig.CableSwig(),
        #                    ip_wrapitk.WrapITK(),
        #                    ip_itkvtkglue.ItkVtkGlue(),
        #                    ip_itkpybuffer.itkPyBuffer(),
        #                    ip_itktudoss.ITKTUDOSS(),
        #                    ip_gdcm.GDCM(),
        #                    ip_devide.DeVIDE(),
        #                    ip_setupenvironment.SetupEnvironment()
        #                    ]

        #if ip_names is None:
            # iow the user didn't touch this
            # this only works because module and class names differ
            # ONLY w.r.t. case
        #    ip_names = [i.__class__.__name__.lower()
        #                for i in ip_instance_list]

        print 'Building install_packages:', str(ip_names)


        def get_stage(ip, n):
            utils.output("%s :: get()" % (n,), rpad, rpad_char)
            ip.get()

        def unpack_stage(ip, n):
            utils.output("%s :: unpack()" % (n,), rpad, rpad_char)
            ip.unpack()

        def configure_stage(ip, n):
            utils.output("%s :: configure()" % (n,), rpad, rpad_char)
            ip.configure()

        def build_stage(ip, n):
            utils.output("%s :: build()" % (n,), rpad, rpad_char)
            ip.build()

        def all_stages(ip, n):
            get_stage(ip, n)

            unpack_stage(ip, n)

            configure_stage(ip, n)            

            build_stage(ip, n)
            
            utils.output("%s :: install()" % (n,), rpad, rpad_char)
            ip.install()

        if mode == 'show_versions':
            utils.output('Extracting all install_package versions.')
            print "python: %d.%d.%d (%s)" % \
                    (sys.version_info[0:3] +
                            (config.PYTHON_EXECUTABLE,))

            
        
        for ip in ip_instance_list:
            n = ip.__class__.__name__

            if mode == 'get_only':
                utils.output("%s GET_ONLY" % (n,), 70, '#')
                utils.output("%s" % (n,), 70, '#')
                get_stage(ip, n)

            elif mode == 'unpack_only':
                utils.output("%s UNPACK_ONLY" % (n,), 70, '#')
                utils.output("%s" % (n,), 70, '#')
                unpack_stage(ip, n)

            elif mode == 'configure_only':
                utils.output("%s CONFIGURE_ONLY" % (n,), 70, '#')
                utils.output("%s" % (n,), 70, '#')
                configure_stage(ip, n)

            elif mode == 'everything':
                utils.output("%s" % (n,), 70, '#')
                all_stages(ip, n)

            elif mode == 'clean_build':
                utils.output("%s CLEAN_BUILD" % (n,), 70, '#')
                ip.clean_build()

            elif mode == 'show_versions':
                print '%s: %s' % (n, ip.get_installed_version())

        if mode != 'show_versions':
            utils.output("Now please read the RESULTS section of README.txt!")

if __name__ == '__main__':
    main()
