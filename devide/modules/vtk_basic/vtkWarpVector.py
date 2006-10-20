# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkWarpVector(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkWarpVector(), 'Processing.',
            ('vtkPointSet',), ('vtkPointSet',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
