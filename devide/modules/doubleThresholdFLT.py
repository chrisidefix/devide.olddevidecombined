from module_base import module_base
import module_utils
from wxPython.wx import *
import vtk

class doubleThresholdFLT(module_base):

    def __init__(self, module_manager):

        # call parent constructor
        module_base.__init__(self, module_manager)

        self._config = None

        self._imageThreshold = vtk.vtkImageThreshold()

        self._outputTypes = {'Double': 'VTK_DOUBLE',
                             'Float' : 'VTK_FLOAT',
                             'Long'  : 'VTK_LONG',
                             'Unsigned Long' : 'VTK_UNSIGNED_LONG',
                             'Integer' : 'VTK_INT',
                             'Unsigned Integer' : 'VTK_UNSIGNED_INT',
                             'Short' : 'VTK_SHORT',
                             'Unsigned Short' : 'VTK_UNSIGNED_SHORT',
                             'Char' : 'VTK_CHAR',
                             'Unsigned Char' : 'VTK_UNSIGNED_CHAR',
                             'Same as input' : -1}

        self._viewFrame = None
        self._createViewFrame()
        self._viewFrame.Show(1)
        
    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        self.set_input(0, None)
        # take out our view interface
        self._viewFrame.Destroy()
        # get rid of our reference
        del self._imageThreshold

    def get_input_descriptions(self):
	return ('vtkImageData',)
    
    def set_input(self, idx, input_stream):
        self._imageThreshold.SetInput(input_stream)
    
    def get_output_descriptions(self):
	return ('vtkImageData',)
    
    def get_output(self, idx):
        return self._imageThreshold.GetOutput()
    
    def sync_config(self):
        
        self._config.lt = self._imageThreshold.GetLowerThreshold()
        self._config.up = self._imageThreshold.GetUpperThreshold()
        self._config.ri = self._imageThreshold.GetReplaceIn()
        self._config.iv = self._imageThreshold.GetInValue()
        self._config.ro = self._imageThreshold.GetReplaceOut()
        self._config.ov = self._imageThreshold.GetOutValue()
        self._config.os = self._imageThreshold.GetOutputScalarType()
        
        filename = self._writer.GetFileName()
        if filename == None:
            filename = ''

        self._setViewFrameFilename(filename)
	
    def apply_config(self):
        self._writer.SetFileName(self._getViewFrameFilename())

    def execute_module(self):
        # following is the standard way of connecting up the dscas3 progress
        # callback to a VTK object; you should do this for all objects in
        # your module - you could do this in __init__ as well, it seems
        # neater here though
        self._writer.SetProgressText('Writing vtk Structured Points data')
        mm = self._module_manager
        self._writer.SetProgressMethod(lambda s=self, mm=mm:
                                       mm.vtk_progress_cb(s._writer))
        
        if len(self._writer.GetFileName()):
            self._writer.Write()

        # tell the vtk log file window to poll the file; if the file has
        # changed, i.e. vtk has written some errors, the log window will
        # pop up.  you should do this in all your modules right after you
        # caused some VTK processing which might have resulted in VTK
        # outputting to the error log
        self._module_manager.vtk_poll_error()

        mm.setProgress(100, 'DONE writing vtk Structured Points data')

    def view(self, parent_window=None):
	# first make sure that our variables agree with the stuff that
        # we're configuring
	self.sync_config()
        self._viewFrame.Show(true)

    def _createViewFrame(self):

        # import the viewFrame (created with wxGlade)
        import modules.resources.python.doubleThresholdFLTFrame
        reload(modules.resources.python.doubleThresholdFLTFrame)

        # find our parent window and instantiate the frame
        pw = self._module_manager.get_module_view_parent_window()
        self._viewFrame = modules.resources.python.doubleThresholdFLTFrame.\
                          doubleThresholdFLTFrame(pw, -1, 'dummy')

        # make sure that a close of that window does the right thing
        EVT_CLOSE(self._viewFrame,
                  lambda e, s=self: s._viewFrame.Show(false))

        # default binding for the buttons at the bottom
        module_utils.bind_CSAEO2(self, self._viewFrame)        

        # finish setting up the output datatype choice
        self._viewFrame.outputDataTypeChoice.Clear()
        for aType in self._outputTypes.keys():
            self._viewFrame.outputDataTypeChoice.Append(aType)


