# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkImageAppendComponents(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkImageAppendComponents(), 'Processing.',
            ('Input 1 (vtkImageData)', 'Input 2 (vtkImageData)', 'Input 3 (vtkImageData)', 'Input 4 (vtkImageData)', 'Input 5 (vtkImageData)'), ('vtkImageData',),
            replaceDoc=True,
            inputFunctions=('SetInput(0, inputStream)', 'SetInput(1, inputStream)', 'SetInput(2, inputStream)', 'SetInput(3, inputStream)', 'SetInput(4, inputStream)'), outputFunctions=None)
