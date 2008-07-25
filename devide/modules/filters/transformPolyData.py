import genUtils
from module_base import ModuleBase
from moduleMixins import noConfigModuleMixin
import moduleUtils
import vtk

class transformPolyData(noConfigModuleMixin, ModuleBase):
    def __init__(self, module_manager):
        # initialise our base class
        ModuleBase.__init__(self, module_manager)

        self._transformPolyData = vtk.vtkTransformPolyDataFilter()
        
        noConfigModuleMixin.__init__(
            self, {'vtkTransformPolyDataFilter' : self._transformPolyData})

        moduleUtils.setupVTKObjectProgress(self, self._transformPolyData,
                                           'Transforming geometry')

        self.sync_module_logic_with_config()

    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        for inputIdx in range(len(self.get_input_descriptions())):
            self.set_input(inputIdx, None)

        # this will take care of all display thingies
        noConfigModuleMixin.close(self)
        
        # get rid of our reference
        del self._transformPolyData

    def get_input_descriptions(self):
        return ('vtkPolyData', 'vtkTransform')

    def set_input(self, idx, inputStream):
        if idx == 0:
            self._transformPolyData.SetInput(inputStream)
        else:
            self._transformPolyData.SetTransform(inputStream)

    def get_output_descriptions(self):
        return (self._transformPolyData.GetOutput().GetClassName(), )

    def get_output(self, idx):
        return self._transformPolyData.GetOutput()

    def logic_to_config(self):
        pass
    
    def config_to_logic(self):
        pass
    
    def view_to_config(self):
        pass

    def config_to_view(self):
        pass
    
    def execute_module(self):
        self._transformPolyData.Update()
