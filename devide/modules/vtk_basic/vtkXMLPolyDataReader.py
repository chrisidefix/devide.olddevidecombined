# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkXMLPolyDataReader(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkXMLPolyDataReader(), 'Reading vtkXMLPolyData.',
            (), ('vtkXMLPolyData',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
