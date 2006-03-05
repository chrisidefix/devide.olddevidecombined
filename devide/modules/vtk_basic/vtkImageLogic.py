# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkImageLogic(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkImageLogic(), 'Processing.',
            ('vtkImageData', 'vtkImageData'), ('vtkImageData',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
