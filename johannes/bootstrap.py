# python script for bootstrapping the johannes DeVIDE build system
#
# NB:
# 1. on unix systems that don't have Python installed, you should rather
# use bootstrap_stage1.sh and bootstrap_stage2.sh, these are
# shell-based alternatives to bootstrap.py
# 2. on windows systems, you have no choice: you need to have a system
# python installed to run this bootstrap.py script.
# 3. johannes.py will be run by the python that is locally built by
# EITHER bootstrap.py OR bootstrap_stage{1,2}.sh

PYVER_STR = '2.6.2'

import config
import getopt
import os
import shutil
import stat
import sys
import utils

nt_python = """
@echo off
@rem script to run locally installed johannes python
@rem should be located in johannes wd\jpython.cmd
@rem as it assumes the local install of python is in
@rem wd\inst\python and it's in wd
%~dp0\inst\python\python.exe %1 %2 %3 %4 %5 %6 %7 %8 %9 
"""

# I tried with a jython.sh script that sets up the environment and
# then runs the correct python, but even with exports, if that python
# process then restarted another python (with os.system) it would not
# get the modified environment (LD_LIBRARY_PATH), and would hence not
# be able to find its own libraries.
posix_python = """
#!/bin/sh
# script to setup environment for running local python
# this should be sourced before running python
# double-check with 'which python' that the locally installed
# version is running...
MYDIR=%s
export LD_LIBRARY_PATH=$MYDIR/python/lib
export PATH=$MYDIR/python/bin/:$PATH
"""


# script to test for presence of required libs on posix
posix_deps_test_c_file = """
#include <bzlib.h>
#include <sqlite3.h>
#include <ncurses.h>
#include <readline/readline.h>
#include <gtk/gtkversion.h>
#include <ft2build.h>
#include <png.h>
#include <zlib.h>
#include <X11/Intrinsic.h>
#include <GL/glu.h>
int main(void) {}
"""

def download_python():
    urlbase = 'http://python.org/ftp/python/%s' % (PYVER_STR,)
    if os.name == 'posix':
        fname = 'Python-%s.tar.bz2' % (PYVER_STR,)
        url = '%s/%s' % (urlbase, fname)
    elif os.name == 'nt':
        import platform
        a = platform.architecture()[0]
        if a == '32bit':
            fname = 'python-%s.msi' % (PYVER_STR,)
            url = '%s/%s' % (urlbase, fname) 
        else:
            fname = 'python-%s.amd64.msi' % (PYVER_STR,)
            url = '%s/%s' % (urlbase, fname)

	print "##### Bootstrapping with %s Python. #####" % (a,)

    utils.goto_archive()
    utils.urlget(url)

    return fname

def usage():
    message = """
Invoke with:
    python bootstrap.py -w working_directory
    """

    print message

def main():
    try:
        optlist, args = getopt.getopt(
                sys.argv[1:], 'w:',
                ['working-dir='])

    except getopt.GetoptError,e:
        usage()
        return

    working_dir = None

    print optlist
    for o, a in optlist:
        if o in ('-w', '--working-dir'):
            working_dir = a

    if not working_dir:
        usage()
        return

    # this will setup the necessary dirs for later calls into utils
    config.init(working_dir, None)

    # first create directory structure
    prepare_dirs(working_dir)

    # now download the python (source for linux, binaries for windows)
    python_fname = download_python()

    if os.name == 'nt':
        # this means we just have to unpack python
        py_msi_dir = os.path.join(config.archive_dir, python_fname)
        py_inst_dir = os.path.join(config.inst_dir, 'python')

        if os.path.exists(py_inst_dir):
            utils.output(
            'Python installation dir present.  Skipping install.')

        else:
            utils.output('Doing local installation of Python.')

            # run with basic interface
            # ret is 0 if successful
            ret = os.system(
                    'msiexec /a %s TARGETDIR=%s /qb' % 
                    (py_msi_dir, py_inst_dir))

            if ret != 0:
                utils.error(
                        'Failed locally installing Python.  EFS / msiexec problems?')


        sxs_manifest_dest = os.path.join(
                py_inst_dir, 'Microsoft.VC90.CRT.manifest')
        if not os.path.exists(sxs_manifest_dest):
            utils.output(
                    'Copying Python MSVCRT 9.0 runtime libs.')

            # now copy the frikking VS2008 RTM (i.e. NOT SP1) from the system
            sr = os.environ.get('SYSTEMROOT')
            sxsd = os.path.join(sr, 'WinSxS')
            if config.WINARCH == '64bit':
                astr = 'amd64'
            else:
                astr = 'x86'

            mbase = '%s_Microsoft.VC90.CRT_1fc8b3b9a1e18e3b_'+ \
                    '9.0.21022.8_x-ww_d08d0375'
            mbase = mbase % (astr,)

            mfn = os.path.join(
                    sxsd, 'Manifests',
                    '%s.manifest' % (mbase,))

            # copy the manifest  file
            shutil.copy(
                    mfn, sxs_manifest_dest)

            # now copy the DLLs
            dllsd = os.path.join(sxsd, mbase)
            for dllfn in ['msvcm90.dll', 'msvcp90.dll', 
                    'msvcr90.dll']:
                shutil.copy(os.path.join(
                    dllsd, dllfn), os.path.join(
                        py_inst_dir, dllfn))
            

        jpcmd = 'jpython.cmd'
        jpc_fn = os.path.join(config.working_dir, jpcmd)
        f = open(jpc_fn, 'w')
        f.write(nt_python)
        f.close()

        ilines = """
%s johannes.py -w %s
        """ % (jpc_fn, config.working_dir)

    else:
        if not posix_deps_test_c():
            print """
JOHANNES ##### cc (compiler) or necessary headers not found.
See error above.  Please fix and try again.

* See the johannes README.txt for more details on which packages to
  install, and also for correct apt-get invocation to install them all
  on for example Debian / Ubuntu.
            """
            return

        if not posix_test_cc():
            utils.output('c++ compiler not found.')
            return

        utils.goto_build()
        tbfn = os.path.join(config.archive_dir, python_fname)
        pybasename = 'Python-%s' % (PYVER_STR,)
        build_dir = os.path.join(config.build_dir, pybasename)

        if not os.path.exists(build_dir):
            utils.unpack(tbfn)

        os.chdir(build_dir)
        ret = os.system(
            './configure --enable-shared --prefix=%s/python' %
            (config.inst_dir,))

        if ret != 0:
            utils.error('Python configure error.')

        # config.MAKE contains -j setting
        # I've had this break with Python 2.6.2, so I'm using straight make here...
        ret = os.system('%s install' % ('make',))
        if ret != 0:
            utils.error('Python build error.')

        # this means we have to test for dependencies and then build
        # Python.
        sefn = 'jpython_setup_env.sh'

        jpcmd_fn = os.path.join(config.working_dir, sefn)
        f = open(jpcmd_fn, 'w')
        f.write(posix_python % (config.inst_dir,))
        f.close()

        # make it executable
        #os.chmod(jpcmd_fn, stat.S_IEXEC)

        ilines = """
source %s
which python
python johannes.py -w %s
        """ % (sefn, config.working_dir)


    print """
######################################################################
Successfully bootstrapped local johannes Python.  Start the full build
system with:
%s
    """ % (ilines,) 


def posix_deps_test_c():
    utils.goto_build()
    f = open('dtest.c', 'w')
    f.write(posix_deps_test_c_file)
    f.close()

    ret = os.system(
'cc -I/usr/include/gtk-2.0 -I/usr/include/freetype2 -o dtest dtest.c')

    # True if successful
    return bool(ret == 0)

def posix_test_cc():
    utils.goto_build()
    f = open('cpptest.cc', 'w')
    f.write('int main(void) {}')
    f.close()

    ret = os.system('c++ -o cpptest cpptest.cc')

    # True if successful
    return bool(ret == 0)


def prepare_dirs(working_dir):
    a_dir = os.path.join(working_dir, 'archive')
    b_dir = os.path.join(working_dir, 'build')
    i_dir = os.path.join(working_dir, 'inst')

    for d in [working_dir, a_dir, b_dir, i_dir]:
        if not os.path.exists(d):
            os.mkdir(d)


           

if __name__ == '__main__':
    main()

