#!/usr/bin/env python
# generated by wxGlade 0.2.1cvs on Fri Jan 17 17:25:19 2003

from wxPython.wx import *
from wxPython.grid import *
# with the very ugly two lines below, make sure x capture is not used
# this should rather be an ivar of the wxVTKRenderWindowInteractor!
import vtk.wx.wxVTKRenderWindowInteractor
vtk.wx.wxVTKRenderWindowInteractor.WX_USE_X_CAPTURE = 0
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor

class MainFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wxDEFAULT_FRAME_STYLE
        wxFrame.__init__(self, *args, **kwds)
        self.panel_1 = wxPanel(self, -1)
        self.notebook_1_copy = wxNotebook(self.panel_1, -1, style=0)
        self.notebook_1_copy_pane_7 = wxPanel(self.notebook_1_copy, -1)
        self.notebook_1_copy_pane_6 = wxPanel(self.notebook_1_copy, -1)
        self.notebook_1_pane_3_copy = wxPanel(self.notebook_1_copy, -1)
        self.voiPanel = wxPanel(self.notebook_1_copy, -1)
        self.notebook_1_pane_1_copy = wxPanel(self.notebook_1_copy, -1)
        self.panel_3 = wxPanel(self.panel_1, -1)
        self.threedRWI = wxVTKRenderWindowInteractor(self.panel_3, -1)
        self.label_1_copy_copy_copy_2_copy = wxStaticText(self.notebook_1_pane_1_copy, -1, "Cursor at")
        self.sliceCursorText = wxTextCtrl(self.notebook_1_pane_1_copy, -1, "")
        self.label_4_copy_copy_copy_2_copy = wxStaticText(self.notebook_1_pane_1_copy, -1, "Name")
        self.sliceCursorNameCombo = wxComboBox(self.notebook_1_pane_1_copy, -1, choices=["Point 1", "Point 2", "Point 3", "Point 4"], style=wxCB_DROPDOWN)
        self.sliceStoreButtonId  =  wxNewId()
        self.button_6_copy_copy_copy_2_copy = wxButton(self.notebook_1_pane_1_copy, self.sliceStoreButtonId , "Store this point")
        self.spointsGrid = wxGrid(self.notebook_1_pane_1_copy, -1)
        self.pointsSelectAllButtonId  =  wxNewId()
        self.pointsSelectAllButton = wxButton(self.notebook_1_pane_1_copy, self.pointsSelectAllButtonId , "Select all")
        self.pointsDeselectAllButtonId  =  wxNewId()
        self.pointsDeselectAllButton = wxButton(self.notebook_1_pane_1_copy, self.pointsDeselectAllButtonId , "Deselect all")
        self.pointsRemoveButtonId  =  wxNewId()
        self.pointsRemoveButton = wxButton(self.notebook_1_pane_1_copy, self.pointsRemoveButtonId , "Remove")
        self.saveListButtonId  =  wxNewId()
        self.button_5 = wxButton(self.notebook_1_pane_1_copy, self.saveListButtonId , "Save list")
        self.loadListButtonId  =  wxNewId()
        self.button_6 = wxButton(self.notebook_1_pane_1_copy, self.loadListButtonId , "Load list")
        self.pointInteractionCheckBoxId  =  wxNewId()
        self.pointInteractionCheckBox = wxCheckBox(self.notebook_1_pane_1_copy, self.pointInteractionCheckBoxId , "3D Point Interaction")
        self.voiPanel.widgetEnabledCboxId  =  wxNewId()
        self.voiPanel.widgetEnabledCbox = wxCheckBox(self.voiPanel, self.voiPanel.widgetEnabledCboxId , "Widget enabled")
        self.label_7_copy_copy = wxStaticText(self.voiPanel, -1, "Absolute bounds")
        self.voiPanel.boundsText = wxTextCtrl(self.voiPanel, -1, "", style=wxTE_READONLY)
        self.label_7_copy_1 = wxStaticText(self.voiPanel, -1, "Discrete extent")
        self.voiPanel.extentText = wxTextCtrl(self.voiPanel, -1, "")
        self.pipelineButtonId  =  wxNewId()
        self.pipelineButton = wxButton(self.notebook_1_pane_3_copy, self.pipelineButtonId , "Pipeline")
        self.resetButtonId  =  wxNewId()
        self.resetButton = wxButton(self.notebook_1_pane_3_copy, self.resetButtonId , "Reset")
        self.label_1 = wxStaticText(self.notebook_1_copy_pane_6, -1, "Current slice name:")
        self.sliceNameChoiceId  =  wxNewId()
        self.sliceNameChoice = wxChoice(self.notebook_1_copy_pane_6, self.sliceNameChoiceId , choices=["choice 1"])
        self.createSliceText = wxTextCtrl(self.notebook_1_copy_pane_6, -1, "")
        self.createSliceButtonId  =  wxNewId()
        self.button_2_copy_2 = wxButton(self.notebook_1_copy_pane_6, self.createSliceButtonId , "Create Slice")
        self.sliceEnabledCheckBoxId  =  wxNewId()
        self.sliceEnabledCheckBox = wxCheckBox(self.notebook_1_copy_pane_6, self.sliceEnabledCheckBoxId , "Enabled")
        self.sliceInteractionCheckBoxId  =  wxNewId()
        self.sliceInteractionCheckBox = wxCheckBox(self.notebook_1_copy_pane_6, self.sliceInteractionCheckBoxId , "Interaction")
        self.orthoViewCheckBoxId  =  wxNewId()
        self.orthoViewCheckBox = wxCheckBox(self.notebook_1_copy_pane_6, self.orthoViewCheckBoxId , "Ortho View")
        self.acsChoiceId  =  wxNewId()
        self.acsChoice = wxChoice(self.notebook_1_copy_pane_6, self.acsChoiceId , choices=["Reset to Axial", "Reset to Coronal", "Reset to Sagittal"])
        self.destroySliceButtonId  =  wxNewId()
        self.button_3_copy_2 = wxButton(self.notebook_1_copy_pane_6, self.destroySliceButtonId , "Destroy Slice")
        self.pushSliceLabel = wxStaticText(self.notebook_1_copy_pane_6, -1, "Push slice")
        self.pushSliceSpinCtrlId  =  wxNewId()
        self.pushSliceSpinCtrl = wxSpinCtrl(self.notebook_1_copy_pane_6, self.pushSliceSpinCtrlId , "0", min=-100, max=100, style=wxSP_ARROW_KEYS)
        self.surfacePickActionRB = wxRadioBox(self.notebook_1_copy_pane_7, -1, "When I click on an object in the scene", choices=["Do nothing", "Place a point on its surface", "Configure the object", "Show a scalar bar for its input"], majorDimension=1, style=wxRA_SPECIFY_ROWS)
        self.objectsListGrid = wxGrid(self.notebook_1_copy_pane_7, -1)
        self.objectSetColourButtonId  =  wxNewId()
        self.button_2 = wxButton(self.notebook_1_copy_pane_7, self.objectSetColourButtonId , "Set Colour")
        self.objectShowHideButtonId  =  wxNewId()
        self.button_3 = wxButton(self.notebook_1_copy_pane_7, self.objectShowHideButtonId , "Show/Hide")
        self.objectContourButtonId  =  wxNewId()
        self.button_4 = wxButton(self.notebook_1_copy_pane_7, self.objectContourButtonId , "Contour")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("Slice3D Viewer")
        self.panel_3.SetSize((729, 496))
        self.sliceCursorNameCombo.SetSelection(0)
        self.spointsGrid.CreateGrid(0, 3)
        self.spointsGrid.SetRowLabelSize(30)
        self.spointsGrid.EnableEditing(0)
        self.spointsGrid.SetSelectionMode(wxGrid.wxGridSelectRows)
        self.spointsGrid.SetColLabelValue(0, "World")
        self.spointsGrid.SetColSize(0, 200)
        self.spointsGrid.SetColLabelValue(1, "Discrete")
        self.spointsGrid.SetColLabelValue(2, "Value")
        self.spointsGrid.SetSize((720, 111))
        self.sliceNameChoice.SetSelection(0)
        self.sliceEnabledCheckBox.SetValue(1)
        self.sliceInteractionCheckBox.SetValue(1)
        self.acsChoice.SetSelection(0)
        self.surfacePickActionRB.SetSelection(0)
        self.objectsListGrid.CreateGrid(2, 4)
        self.objectsListGrid.EnableEditing(0)
        self.objectsListGrid.EnableDragRowSize(0)
        self.objectsListGrid.SetSelectionMode(wxGrid.wxGridSelectRows)
        self.objectsListGrid.SetColLabelValue(0, "Object Name")
        self.objectsListGrid.SetColLabelValue(1, "Colour")
        self.objectsListGrid.SetColLabelValue(2, "Visible")
        self.objectsListGrid.SetColLabelValue(3, "Contour")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wxBoxSizer(wxVERTICAL)
        sizer_8 = wxBoxSizer(wxVERTICAL)
        sizer_9 = wxBoxSizer(wxHORIZONTAL)
        sizer_10 = wxBoxSizer(wxVERTICAL)
        sizer_3 = wxBoxSizer(wxVERTICAL)
        sizer_11 = wxBoxSizer(wxHORIZONTAL)
        sizer_6 = wxBoxSizer(wxVERTICAL)
        sizer_20_copy_1_copy = wxBoxSizer(wxHORIZONTAL)
        sizer_7 = wxBoxSizer(wxHORIZONTAL)
        sizer_18_copy = wxBoxSizer(wxHORIZONTAL)
        sizer_19_copy = wxBoxSizer(wxVERTICAL)
        sizer_3_copy = wxBoxSizer(wxVERTICAL)
        grid_sizer_4_copy = wxFlexGridSizer(2, 2, 0, 0)
        sizer_10_copy = wxBoxSizer(wxVERTICAL)
        sizer_11_copy = wxBoxSizer(wxHORIZONTAL)
        sizer_13_copy_copy = wxBoxSizer(wxHORIZONTAL)
        sizer_2 = wxBoxSizer(wxVERTICAL)
        sizer_2.Add(self.threedRWI, 1, wxEXPAND, 0)
        self.panel_3.SetAutoLayout(1)
        self.panel_3.SetSizer(sizer_2)
        sizer_8.Add(self.panel_3, 1, wxLEFT|wxRIGHT|wxTOP|wxEXPAND, 7)
        sizer_13_copy_copy.Add(self.label_1_copy_copy_copy_2_copy, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_13_copy_copy.Add(self.sliceCursorText, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_13_copy_copy.Add(self.label_4_copy_copy_copy_2_copy, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_13_copy_copy.Add(self.sliceCursorNameCombo, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_13_copy_copy.Add(self.button_6_copy_copy_copy_2_copy, 0, wxEXPAND, 0)
        sizer_10_copy.Add(sizer_13_copy_copy, 0, wxALL|wxEXPAND, 4)
        sizer_10_copy.Add(self.spointsGrid, 1, wxEXPAND, 4)
        sizer_11_copy.Add(self.pointsSelectAllButton, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_11_copy.Add(self.pointsDeselectAllButton, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_11_copy.Add(self.pointsRemoveButton, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_11_copy.Add(self.button_5, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_11_copy.Add(self.button_6, 0, wxALIGN_CENTER_VERTICAL, 0)
        sizer_10_copy.Add(sizer_11_copy, 0, wxLEFT|wxRIGHT|wxBOTTOM|wxEXPAND, 4)
        sizer_10_copy.Add(self.pointInteractionCheckBox, 0, wxLEFT|wxRIGHT|wxBOTTOM|wxALIGN_CENTER_VERTICAL, 4)
        self.notebook_1_pane_1_copy.SetAutoLayout(1)
        self.notebook_1_pane_1_copy.SetSizer(sizer_10_copy)
        sizer_10_copy.Fit(self.notebook_1_pane_1_copy)
        sizer_10_copy.SetSizeHints(self.notebook_1_pane_1_copy)
        sizer_3_copy.Add(self.voiPanel.widgetEnabledCbox, 0, 0, 0)
        grid_sizer_4_copy.Add(self.label_7_copy_copy, 0, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        grid_sizer_4_copy.Add(self.voiPanel.boundsText, 1, wxLEFT|wxRIGHT|wxEXPAND, 2)
        grid_sizer_4_copy.Add(self.label_7_copy_1, 0, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        grid_sizer_4_copy.Add(self.voiPanel.extentText, 1, wxLEFT|wxRIGHT|wxEXPAND, 2)
        grid_sizer_4_copy.AddGrowableCol(1)
        sizer_3_copy.Add(grid_sizer_4_copy, 1, wxEXPAND, 0)
        self.voiPanel.SetAutoLayout(1)
        self.voiPanel.SetSizer(sizer_3_copy)
        sizer_3_copy.Fit(self.voiPanel)
        sizer_3_copy.SetSizeHints(self.voiPanel)
        sizer_19_copy.Add(self.pipelineButton, 0, wxALL, 2)
        sizer_19_copy.Add(self.resetButton, 0, wxALL, 2)
        sizer_18_copy.Add(sizer_19_copy, 0, wxEXPAND, 0)
        self.notebook_1_pane_3_copy.SetAutoLayout(1)
        self.notebook_1_pane_3_copy.SetSizer(sizer_18_copy)
        sizer_18_copy.Fit(self.notebook_1_pane_3_copy)
        sizer_18_copy.SetSizeHints(self.notebook_1_pane_3_copy)
        sizer_7.Add(self.label_1, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_7.Add(self.sliceNameChoice, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        label_2 = wxStaticText(self.notebook_1_copy_pane_6, -1, "New slice name:")
        sizer_7.Add(label_2, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_7.Add(self.createSliceText, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_7.Add(self.button_2_copy_2, 0, wxALIGN_CENTER_VERTICAL, 7)
        sizer_6.Add(sizer_7, 0, wxALL|wxEXPAND, 4)
        sizer_20_copy_1_copy.Add(self.sliceEnabledCheckBox, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_20_copy_1_copy.Add(self.sliceInteractionCheckBox, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_20_copy_1_copy.Add(self.orthoViewCheckBox, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_20_copy_1_copy.Add(self.acsChoice, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_20_copy_1_copy.Add(self.button_3_copy_2, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_20_copy_1_copy.Add(self.pushSliceLabel, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_20_copy_1_copy.Add(self.pushSliceSpinCtrl, 0, wxALIGN_CENTER_VERTICAL, 7)
        sizer_6.Add(sizer_20_copy_1_copy, 0, wxLEFT|wxRIGHT|wxBOTTOM, 4)
        self.notebook_1_copy_pane_6.SetAutoLayout(1)
        self.notebook_1_copy_pane_6.SetSizer(sizer_6)
        sizer_6.Fit(self.notebook_1_copy_pane_6)
        sizer_6.SetSizeHints(self.notebook_1_copy_pane_6)
        sizer_10.Add(self.surfacePickActionRB, 0, wxALL|wxEXPAND, 4)
        sizer_3.Add(self.objectsListGrid, 1, wxEXPAND, 0)
        sizer_11.Add(self.button_2, 0, wxRIGHT, 4)
        sizer_11.Add(self.button_3, 0, wxRIGHT, 4)
        sizer_11.Add(self.button_4, 0, wxRIGHT, 4)
        sizer_3.Add(sizer_11, 0, wxTOP|wxBOTTOM|wxEXPAND, 4)
        sizer_10.Add(sizer_3, 1, wxALL|wxEXPAND, 4)
        self.notebook_1_copy_pane_7.SetAutoLayout(1)
        self.notebook_1_copy_pane_7.SetSizer(sizer_10)
        sizer_10.Fit(self.notebook_1_copy_pane_7)
        sizer_10.SetSizeHints(self.notebook_1_copy_pane_7)
        self.notebook_1_copy.AddPage(self.notebook_1_pane_1_copy, "Selected points")
        self.notebook_1_copy.AddPage(self.voiPanel, "Volume of Interest")
        self.notebook_1_copy.AddPage(self.notebook_1_pane_3_copy, "Global Operations")
        self.notebook_1_copy.AddPage(self.notebook_1_copy_pane_6, "Slices")
        self.notebook_1_copy.AddPage(self.notebook_1_copy_pane_7, "Objects")
        sizer_9.Add(wxNotebookSizer(self.notebook_1_copy), 1, wxEXPAND, 0)
        sizer_8.Add(sizer_9, 0, wxALL|wxEXPAND, 7)
        self.panel_1.SetAutoLayout(1)
        self.panel_1.SetSizer(sizer_8)
        sizer_8.Fit(self.panel_1)
        sizer_8.SetSizeHints(self.panel_1)
        sizer_1.Add(self.panel_1, 1, wxEXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class MainFrame


class orthoViewFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: orthoViewFrame.__init__
        kwds["style"] = wxDEFAULT_FRAME_STYLE
        wxFrame.__init__(self, *args, **kwds)
        self.panel_2 = wxPanel(self, -1)
        self.RWI = wxVTKRenderWindowInteractor(self.panel_2, -1)
        self.closeButtonId  =  wxNewId()
        self.button_1 = wxButton(self.panel_2, self.closeButtonId , "Close")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: orthoViewFrame.__set_properties
        self.SetTitle("Ortho View")
        self.SetSize((480, 433))
        self.RWI.SetSize((-1, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: orthoViewFrame.__do_layout
        sizer_4 = wxBoxSizer(wxVERTICAL)
        sizer_5 = wxBoxSizer(wxVERTICAL)
        sizer_5.Add(self.RWI, 1, wxEXPAND, 0)
        sizer_5.Add(self.button_1, 0, wxALIGN_CENTER_HORIZONTAL, 0)
        self.panel_2.SetAutoLayout(1)
        self.panel_2.SetSizer(sizer_5)
        sizer_5.Fit(self.panel_2)
        sizer_5.SetSizeHints(self.panel_2)
        sizer_4.Add(self.panel_2, 1, wxEXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_4)
        self.Layout()
        # end wxGlade

# end of class orthoViewFrame

