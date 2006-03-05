# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkXMLPPolyDataWriter(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkXMLPPolyDataWriter(), 'Writing vtkXMLPPolyData.',
            ('vtkXMLPPolyData',), (),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
