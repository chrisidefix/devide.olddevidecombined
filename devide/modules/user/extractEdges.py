# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class extractEdges(simpleVTKClassModuleBase):
    def __init__(self, module_manager):
        simpleVTKClassModuleBase.__init__(
            self, module_manager,
            vtk.vtkExtractEdges(), 'Extracting edges.',
            ('vtkDataSet',), ('vtkPolyData',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
