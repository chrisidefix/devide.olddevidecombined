import os

try:
    if os.name == 'posix':
        from libvtkitkdvCommonPython import *        
        from libvtkitkdvAlgorithmsPython import *
    else:
        from vtkitkdvAlgorithmsPython import *
except ImportError,e:
    print e
    pass
