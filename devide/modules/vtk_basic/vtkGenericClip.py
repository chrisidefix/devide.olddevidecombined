# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkGenericClip(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkGenericClip(), 'Processing.',
            ('vtkGenericDataSet',), ('vtkUnstructuredGrid', 'vtkUnstructuredGrid'),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
