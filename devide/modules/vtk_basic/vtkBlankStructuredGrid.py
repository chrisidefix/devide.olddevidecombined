# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkBlankStructuredGrid(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkBlankStructuredGrid(), 'Processing.',
            ('vtkStructuredGrid',), ('vtkStructuredGrid',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
