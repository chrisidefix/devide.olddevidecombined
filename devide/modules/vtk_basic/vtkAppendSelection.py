# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkAppendSelection(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkAppendSelection(), 'Processing.',
            ('vtkSelection',), ('vtkSelection',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)