# FIXME: check that everything is located in the DRE_TOP directory.

import os
import platform
import re
import sys

output1 = """
-= DeVIDE Runtime Environment (DRE) v%(devide_ver)s =-

Platform: %(machine_id)s
"""

output2 = """Basic software:
    cmake %(cmake_ver)s

Python software:
    Python %(python_ver)s
    numpy %(numpy_ver)s
    matplotlib %(mpl_ver)s
    wxPython %(wx_ver)s
    VTK %(vtk_ver)s
    ITK %(itk_ver)s
    gdcm %(gdcm_ver)s
"""

def helper_get_status_output(command):
    """Run command, return output of command and exit code in status.
    In general, status is None for success and 1 for command not
    found.
    """

    ph = os.popen(command)
    output = ph.read()
    status = ph.close()
    return (status, output)


def get_cmake_version():
    dre_top = os.environ.get('DRE_TOP')
    cmake_binpath = os.path.join(
            dre_top, 'cmake', 'bin', 'cmake')

    status, output = helper_get_status_output(
            cmake_binpath + ' -version')

    if status is None:
        mo = re.search('^cmake version (.*)$', output)
        if mo:
            return mo.groups()[0]
        else:
            return '[error extracting version]'
        
    else:
        return '[not found]'



def get_devide_version():
    """Return DeVIDE version string.
    """

    import devide
    return devide.DEVIDE_VERSION

def get_gdcm_version():
    import gdcm
    return gdcm.Version.GetVersion()  

def get_itk_version():
    import itk
    return itk.Version.GetITKVersion()

def get_machine_id():
    """Return string of the form:
    OS VERSION on MACHINE (ARCH) e.g. Linux 2.6.xxx on x86_64 (64bit)
    """

    u = platform.uname()
    a = platform.architecture()
    return '%s %s on %s (%s)' % (u[0], u[2], u[4], a[0]) 

def get_mpl_ver():
    try:
        import matplotlib
    except ImportError:
        return "[not installed]"
    else:
        return matplotlib.__version__

def get_numpy_ver():
    try:
        import numpy
    except ImportError:
        return "[not installed]"
    else:
        return numpy.version.version

def get_python_version():
    return '%s.%s.%s %s-%s' % sys.version_info

def get_vtk_version():
    import vtk
    return vtk.vtkVersion.GetVTKVersion()

def get_wx_version():
    import wx
    return wx.VERSION_STRING

def main():
    # print output in two sections, because the second section can
    # take its time.  This way, the user knows that we're here.
    vd1 = {'devide_ver' : get_devide_version(),
          'machine_id' : get_machine_id()
          }
    print output1 % vd1

    vd2 = {
          'python_ver' : get_python_version(),
          'wx_ver' : get_wx_version(),
          'numpy_ver' : get_numpy_ver(),
          'mpl_ver' : get_mpl_ver(),
          'vtk_ver' : get_vtk_version(),
          'itk_ver' : get_itk_version(),
          'gdcm_ver' : get_gdcm_version(),
          'cmake_ver' : get_cmake_version()
        }
    print output2 % vd2

if __name__ == '__main__':
    main()

