# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkEnSight6BinaryReader(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkEnSight6BinaryReader(), 'Reading vtkEnSight6Binary.',
            (), ('vtkEnSight6Binary',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
