# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkPLYWriter(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkPLYWriter(), 'Writing vtkPLY.',
            ('vtkPLY',), (),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
