#!/usr/bin/env python
# generated by wxGlade 0.2.1 on Thu Feb 20 18:11:11 2003

from wxPython.wx import *

class seedConnectFLTViewFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: seedConnectFLTViewFrame.__init__
        kwds["style"] = wxCAPTION|wxMINIMIZE_BOX|wxMAXIMIZE_BOX|wxSYSTEM_MENU|wxRESIZE_BORDER
        wxFrame.__init__(self, *args, **kwds)
        self.viewFramePanel = wxPanel(self, -1)
        self.label_1 = wxStaticText(self.viewFramePanel, -1, "Input Connect Value")
        self.inputConnectValueText = wxTextCtrl(self.viewFramePanel, -1, "")
        self.label_2 = wxStaticText(self.viewFramePanel, -1, "Output Connected Value")
        self.outputConnectedValueText = wxTextCtrl(self.viewFramePanel, -1, "")
        self.label_3 = wxStaticText(self.viewFramePanel, -1, "Output Unconnected Value")
        self.outputUnconnectedValueText = wxTextCtrl(self.viewFramePanel, -1, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: seedConnectFLTViewFrame.__set_properties
        self.SetTitle("seedConnect View")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: seedConnectFLTViewFrame.__do_layout
        sizer_1 = wxBoxSizer(wxVERTICAL)
        sizer_5 = wxBoxSizer(wxVERTICAL)
        grid_sizer_1 = wxFlexGridSizer(3, 2, 4, 4)
        grid_sizer_1.Add(self.label_1, 0, wxALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.inputConnectValueText, 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, wxALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.outputConnectedValueText, 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, wxALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.outputUnconnectedValueText, 0, 0, 0)
        grid_sizer_1.AddGrowableCol(1)
        sizer_5.Add(grid_sizer_1, 1, wxALL|wxEXPAND, 7)
        self.viewFramePanel.SetAutoLayout(1)
        self.viewFramePanel.SetSizer(sizer_5)
        sizer_5.Fit(self.viewFramePanel)
        sizer_5.SetSizeHints(self.viewFramePanel)
        sizer_1.Add(self.viewFramePanel, 1, wxEXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class seedConnectFLTViewFrame


