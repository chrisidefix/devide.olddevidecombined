# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkDelimitedTextReader(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkDelimitedTextReader(), 'Reading vtkDelimitedText.',
            (), ('vtkDelimitedText',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
