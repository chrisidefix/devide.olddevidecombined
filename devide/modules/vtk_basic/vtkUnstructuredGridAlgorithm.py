# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkUnstructuredGridAlgorithm(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkUnstructuredGridAlgorithm(), 'Processing.',
            ('vtkUnstructuredGrid',), ('vtkUnstructuredGrid',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
