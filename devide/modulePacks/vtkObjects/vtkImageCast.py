# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkImageCast(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkImageCast(), 'Processing.',
            ('vtkImageData',), ('vtkImageData',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
