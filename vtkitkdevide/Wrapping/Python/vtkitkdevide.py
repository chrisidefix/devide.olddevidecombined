import os

try:
    if os.name == 'posix':
        from libvtkitkdvCommonPython import *
        from libvtkitkdvBasicFiltersPython import *
        from libvtkitkdvAlgorithmsPython import *
    else:
        from vtkitkdvCommonPython import *
        from vtkitkdvBasicFiltersPython import *
        from vtkitkdvAlgorithmsPython import *
except ImportError,e:
    print e
    pass
