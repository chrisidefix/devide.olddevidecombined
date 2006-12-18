from moduleBase import moduleBase
from moduleMixins import scriptedConfigModuleMixin
import moduleUtils
import vtk



class warpPoints(scriptedConfigModuleMixin, moduleBase):
    _defaultVectorsSelectionString = 'Default Active Vectors'
    _userDefinedString = 'User Defined'

    def __init__(self, moduleManager):
        moduleBase.__init__(self, moduleManager)

        self._config.scaleFactor = 1
        self._config.vectorsSelection = self._defaultVectorsSelectionString


        configList = [
            ('Scale factor:', 'scaleFactor', 'base:float', 'text',
             'The warping will be scaled by this factor'),
            ('Vectors selection:', 'vectorsSelection', 'base:str', 'choice',
             'The attribute that will be used as vectors for the warping.',
             (self._defaultVectorsSelectionString, self._userDefinedString))]

        scriptedConfigModuleMixin.__init__(self, configList)

        self._warpVector = vtk.vtkWarpVector()
        
        moduleUtils.setupVTKObjectProgress(self, self._warpVector,
                                           'Warping points.')
        

        self._createWindow(
            {'Module (self)' : self,
             'vtkWarpVector' : self._warpVector})

        # pass the data down to the underlying logic
        self.config_to_logic()
        # and all the way up from logic -> config -> view to make sure
        self.logic_to_config()
        self.config_to_view()

    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        for inputIdx in range(len(self.get_input_descriptions())):
            self.set_input(inputIdx, None)

        # this will take care of all display thingies
        scriptedConfigModuleMixin.close(self)
        
        # get rid of our reference
        del self._warpVector

    def execute_module(self):
        self._warpVector.Update()
        

    def get_input_descriptions(self):
        return ('VTK points/polydata with vector attribute',)

    def set_input(self, idx, inputStream):
        self._warpVector.SetInput(inputStream)

    def get_output_descriptions(self):
        return ('Warped data',)

    def get_output(self, idx):
        # we only return something if we have something
        if self._warpVector.GetNumberOfInputConnections(0):
            return self._warpVector.GetOutput()
        else:
            return None

    def logic_to_config(self):
        self._config.scaleFactor = self._warpVector.GetScaleFactor()

        # the vector choice is the second configTuple
        choice = self._getWidget(1)

        # this is the new way of checking input connections
        if self._warpVector.GetNumberOfInputConnections(0):
        #if self._warpVector.GetInput():
            pd = self._warpVector.GetInput().GetPointData()
            if pd:
                # get a list of attribute names
                names = []
                for i in range(pd.GetNumberOfArrays()):
                    names.append(pd.GetArray(i).GetName())
                
                # find out what the choices CURRENTLY are (except for the
                # default and the "user defined")
                choiceNames = []
                ccnt = choice.GetCount()
                for i in range(2,ccnt):
                    choiceNames.append(choice.GetString(i))

                if choiceNames != names:
                    # this means things have changed, we have to rebuild
                    # the choice
                    choice.Clear()
                    choice.Append(self._defaultVectorsSelectionString)
                    choice.Append(self._userDefinedString)
                    for name in names:
                        choice.Append(name)

        #vs = self._warpVector.GetInputVectorsSelection()
        inf = self._warpVector.GetInputArrayInformation(0)
        vs = inf.Get(vtk.vtkDataObject.FIELD_NAME())

        if vs:
            si = choice.FindString(vs)
            if si == -1:
                # string not found, that means the user has been playing
                # behind our backs, (or he's loading a valid selection
                # from DVN) so we add it to the choice as well
                choice.Append(vs)
                choice.SetStringSelection(vs)

            else:
                choice.SetSelection(si)

        else:
            # no vector selection, so default
            choice.SetSelection(0)
        
                
    
    def config_to_logic(self):
        self._warpVector.SetScaleFactor(self._config.scaleFactor)

        if self._config.vectorsSelection == \
               self._defaultVectorsSelectionString:
            # default: idx, port, connection, fieldassociation (points), name
            self._warpVector.SetInputArrayToProcess(0, 0, 0, 0, None)
            
        else:
            self._warpVector.SetInputArrayToProcess(
                0, 0, 0, 0, self._config.vectorsSelection)

