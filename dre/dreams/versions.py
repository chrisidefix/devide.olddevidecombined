import os
import platform
import sys

output = """
-= DeVIDE Runtime Environment (DRE) v%(devide_ver)s =-

Platform: %(machine_id)s
Software:
    Python %(python_ver)s
    wxPython %(wx_ver)s
"""

def get_devide_version():
    """Return DeVIDE version string.
    """

    import devide
    return devide.DEVIDE_VERSION


def get_machine_id():
    """Return string of the form:
    OS VERSION on MACHINE (ARCH) e.g. Linux 2.6.xxx on x86_64 (64bit)
    """

    u = platform.uname()
    a = platform.architecture()
    return '%s %s on %s (%s)' % (u[0], u[2], u[4], a[0]) 

def get_python_version():
    ver, comp = sys.version.split('\n')
    return '%s compiler %s' % (ver.strip(), comp)

def get_wx_version():
    import wx
    return wx.VERSION_STRING

def main():
    vd = {'devide_ver' : get_devide_version(),
          'machine_id' : get_machine_id(),
          'python_ver' : get_python_version(),
          'wx_ver' : get_wx_version(),
        }

    print output % vd

if __name__ == '__main__':
    main()

