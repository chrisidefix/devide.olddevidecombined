# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkEnSight6Reader(SimpleVTKClassModuleBase):
    def __init__(self, module_manager):
        SimpleVTKClassModuleBase.__init__(
            self, module_manager,
            vtk.vtkEnSight6Reader(), 'Reading vtkEnSight6.',
            (), ('vtkEnSight6',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
