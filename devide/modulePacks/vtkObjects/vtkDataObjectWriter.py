# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkDataObjectWriter(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkDataObjectWriter(), 'Writing vtkDataObject.',
            ('vtkDataObject',), (),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
