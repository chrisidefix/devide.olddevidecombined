# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkWeightedTransformFilter(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkWeightedTransformFilter(), 'Processing.',
            ('vtkPointSet',), ('vtkPointSet',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
