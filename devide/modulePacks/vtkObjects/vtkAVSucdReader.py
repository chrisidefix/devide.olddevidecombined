# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkAVSucdReader(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkAVSucdReader(), 'Reading vtkAVSucd.',
            (), ('vtkAVSucd',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
