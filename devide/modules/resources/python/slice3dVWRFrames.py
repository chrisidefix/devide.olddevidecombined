#!/usr/bin/env python
# generated by wxGlade 0.2.1cvs on Fri Jan 17 17:25:19 2003

from wxPython.wx import *
from wxPython.grid import *
# with the very ugly two lines below, make sure x capture is not used
# this should rather be an ivar of the wxVTKRenderWindowInteractor!
import vtk.wx.wxVTKRenderWindowInteractor
vtk.wx.wxVTKRenderWindowInteractor.WX_USE_X_CAPTURE = 0
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor

class threedFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: threedFrame.__init__
        kwds["style"] = wxDEFAULT_FRAME_STYLE
        wxFrame.__init__(self, *args, **kwds)
        self.panel_1 = wxPanel(self, -1)
        self.showControlsButtonId  =  wxNewId()
        self.button_2 = wxButton(self.panel_1, self.showControlsButtonId , "Show Controls")
        self.resetCameraButtonId  =  wxNewId()
        self.resetCameraButton = wxButton(self.panel_1, self.resetCameraButtonId , "Reset Camera")
        self.resetAllButtonId  =  wxNewId()
        self.button = wxButton(self.panel_1, self.resetAllButtonId , "Reset All")
        self.introspectPipelineButtonId  =  wxNewId()
        self.button_5 = wxButton(self.panel_1, self.introspectPipelineButtonId , "Introspect")
        self.projectionChoiceId  =  wxNewId()
        self.projectionChoice = wxChoice(self.panel_1, self.projectionChoiceId , choices=["Perspective", "Orthogonal"])
        self.threedRWI = wxVTKRenderWindowInteractor(self.panel_1, -1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: threedFrame.__set_properties
        self.SetTitle("Slice3D Viewer")
        self.SetSize((640, 480))
        self.projectionChoice.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: threedFrame.__do_layout
        sizer_1 = wxBoxSizer(wxVERTICAL)
        sizer_8 = wxBoxSizer(wxVERTICAL)
        sizer_2 = wxBoxSizer(wxHORIZONTAL)
        sizer_15 = wxBoxSizer(wxVERTICAL)
        sizer_15.Add(self.button_2, 0, wxBOTTOM|wxEXPAND, 4)
        sizer_15.Add(self.resetCameraButton, 0, wxBOTTOM|wxEXPAND, 4)
        sizer_15.Add(self.button, 0, wxBOTTOM|wxEXPAND, 4)
        sizer_15.Add(self.button_5, 0, wxBOTTOM|wxEXPAND, 4)
        sizer_15.Add(self.projectionChoice, 0, wxEXPAND, 0)
        sizer_2.Add(sizer_15, 0, wxRIGHT|wxEXPAND, 4)
        sizer_2.Add(self.threedRWI, 1, wxEXPAND, 0)
        sizer_8.Add(sizer_2, 1, wxALL|wxEXPAND, 7)
        self.panel_1.SetAutoLayout(1)
        self.panel_1.SetSizer(sizer_8)
        sizer_8.Fit(self.panel_1)
        sizer_8.SetSizeHints(self.panel_1)
        sizer_1.Add(self.panel_1, 1, wxEXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class threedFrame


class controlFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: controlFrame.__init__
        kwds["style"] = wxCAPTION|wxMINIMIZE_BOX|wxMAXIMIZE_BOX|wxSYSTEM_MENU
        wxFrame.__init__(self, *args, **kwds)
        self.panel_3 = wxPanel(self, -1)
        self.createSliceComboBox = wxComboBox(self.panel_3, -1, choices=["Scapula lateral edge", "Scapula spina", "Axial", "Coronal", "Sagittal"], style=wxCB_DROPDOWN)
        self.createSliceButtonId  =  wxNewId()
        self.button_2_2 = wxButton(self.panel_3, self.createSliceButtonId , "Create Slice")
        self.sliceGrid = wxGrid(self.panel_3, -1)
        self.label_1_2 = wxStaticText(self.panel_3, -1, "Cursor at")
        self.sliceCursorText = wxTextCtrl(self.panel_3, -1, "")
        self.label_4_2 = wxStaticText(self.panel_3, -1, "Name")
        self.sliceCursorNameCombo = wxComboBox(self.panel_3, -1, choices=["Point 1", "Point 2", "Point 3", "Point 4"], style=wxCB_DROPDOWN)
        self.sliceStoreButtonId  =  wxNewId()
        self.button_6_2 = wxButton(self.panel_3, self.sliceStoreButtonId , "Store this point")
        self.pointsGrid = wxGrid(self.panel_3, -1)
        self.pointsSelectAllButtonId  =  wxNewId()
        self.pointsSelectAllButton = wxButton(self.panel_3, self.pointsSelectAllButtonId , "Select all")
        self.pointsDeselectAllButtonId  =  wxNewId()
        self.pointsDeselectAllButton = wxButton(self.panel_3, self.pointsDeselectAllButtonId , "Deselect all")
        self.pointsRemoveButtonId  =  wxNewId()
        self.pointsRemoveButton = wxButton(self.panel_3, self.pointsRemoveButtonId , "Delete")
        self.pointInteractionCheckBoxId  =  wxNewId()
        self.pointInteractionCheckBox = wxCheckBox(self.panel_3, self.pointInteractionCheckBoxId , "3D Point Interaction")
        self.label_5_1 = wxStaticText(self.panel_3, -1, "When I click on an object in the scene,")
        self.surfacePickActionChoice = wxChoice(self.panel_3, -1, choices=["do nothing.", "place a point on its surface.", "configure the object.", "show the scalar bar for its input."])
        self.objectsListGrid = wxGrid(self.panel_3, -1)
        self.objectSelectAllButtonId  =  wxNewId()
        self.button_9_1 = wxButton(self.panel_3, self.objectSelectAllButtonId , "Select All")
        self.objectDeselectAllButtonId  =  wxNewId()
        self.button_10_1 = wxButton(self.panel_3, self.objectDeselectAllButtonId , "Deselect All")
        self.objectShowHideButtonId  =  wxNewId()
        self.button_3_1 = wxButton(self.panel_3, self.objectShowHideButtonId , "Show/Hide")
        self.objectSetColourButtonId  =  wxNewId()
        self.button_2_1 = wxButton(self.panel_3, self.objectSetColourButtonId , "Set Colour")
        self.objectContourButtonId  =  wxNewId()
        self.button_4_1 = wxButton(self.panel_3, self.objectContourButtonId , "Contour")
        self.objectMotionButtonId  =  wxNewId()
        self.button_11_1 = wxButton(self.panel_3, self.objectMotionButtonId , "Motion")
        self.objectAttachAxisButtonId  =  wxNewId()
        self.button_3 = wxButton(self.panel_3, self.objectAttachAxisButtonId , "Attach Axis")
        self.objectAxisToSliceButtonId  =  wxNewId()
        self.button_13_1 = wxButton(self.panel_3, self.objectAxisToSliceButtonId , "Axis to Slice")
        self.objectPlaneLockButtonId  =  wxNewId()
        self.button_4 = wxButton(self.panel_3, self.objectPlaneLockButtonId , "Plane Lock")
        self.voiEnabledCheckBoxId  =  wxNewId()
        self.voiEnabledCheckBox = wxCheckBox(self.panel_3, self.voiEnabledCheckBoxId , "VOI extraction:")
        self.label_7 = wxStaticText(self.panel_3, -1, "Bounds")
        self.voiBoundsText = wxTextCtrl(self.panel_3, -1, "", style=wxTE_READONLY)
        self.label_7_1 = wxStaticText(self.panel_3, -1, "Discrete")
        self.voiExtentText = wxTextCtrl(self.panel_3, -1, "")
        
        # Menu Bar
        self.frame_4_menubar = wxMenuBar()
        self.SetMenuBar(self.frame_4_menubar)
        self.slicesMenu = wxMenu()
        self.frame_4_menubar.Append(self.slicesMenu, "&Slices")
        self.pointsMenu = wxMenu()
        self.frame_4_menubar.Append(self.pointsMenu, "&Points")
        self.objectsMenu = wxMenu()
        self.frame_4_menubar.Append(self.objectsMenu, "&Objects")
        # Menu Bar end
        self.frame_4_statusbar = self.CreateStatusBar(1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: controlFrame.__set_properties
        self.SetTitle("Slice3D Control")
        self.createSliceComboBox.SetSelection(0)
        self.sliceGrid.CreateGrid(2, 3)
        self.sliceGrid.EnableEditing(0)
        self.sliceGrid.EnableDragRowSize(0)
        self.sliceGrid.EnableDragGridSize(0)
        self.sliceGrid.SetSelectionMode(wxGrid.wxGridSelectRows)
        self.sliceGrid.SetColLabelValue(0, "Slice name")
        self.sliceGrid.SetColLabelValue(1, "Enabled")
        self.sliceGrid.SetColLabelValue(2, "Interaction")
        self.sliceGrid.SetSize((500, 125))
        self.sliceCursorNameCombo.SetSelection(0)
        self.pointsGrid.CreateGrid(2, 3)
        self.pointsGrid.SetRowLabelSize(30)
        self.pointsGrid.EnableEditing(0)
        self.pointsGrid.EnableDragRowSize(0)
        self.pointsGrid.EnableDragGridSize(0)
        self.pointsGrid.SetSelectionMode(wxGrid.wxGridSelectRows)
        self.pointsGrid.SetColLabelValue(0, "World")
        self.pointsGrid.SetColSize(0, 200)
        self.pointsGrid.SetColLabelValue(1, "Discrete")
        self.pointsGrid.SetColLabelValue(2, "Value")
        self.pointsGrid.SetSize((500, 100))
        self.surfacePickActionChoice.SetSize((200, 34))
        self.surfacePickActionChoice.SetSelection(0)
        self.objectsListGrid.CreateGrid(2, 5)
        self.objectsListGrid.EnableEditing(0)
        self.objectsListGrid.EnableDragRowSize(0)
        self.objectsListGrid.EnableDragGridSize(0)
        self.objectsListGrid.SetSelectionMode(wxGrid.wxGridSelectRows)
        self.objectsListGrid.SetColLabelValue(0, "Object Name")
        self.objectsListGrid.SetColLabelValue(1, "Colour")
        self.objectsListGrid.SetColLabelValue(2, "Visible")
        self.objectsListGrid.SetColLabelValue(3, "Contour")
        self.objectsListGrid.SetColLabelValue(4, "Motion")
        self.objectsListGrid.SetSize((500, 100))
        self.button_11_1.SetToolTipString("(De)Activate motion for the selected object(s).")
        self.button_3.SetToolTipString("Associate an object axis (defined by two selected points) with the selected object(s).")
        self.button_13_1.SetToolTipString("Move the selected objects so that their axes are on the selected planes.")
        self.button_4.SetToolTipString("Constrain motion of the selected objects to the selected planes.")
        self.frame_4_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_4_statusbar_fields = ["All hail the mighty Slice3D Control!"]
        for i in range(len(frame_4_statusbar_fields)):
            self.frame_4_statusbar.SetStatusText(frame_4_statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: controlFrame.__do_layout
        sizer_16 = wxBoxSizer(wxVERTICAL)
        sizer_3 = wxBoxSizer(wxVERTICAL)
        sizer_20 = wxStaticBoxSizer(wxStaticBox(self.panel_3, -1, "Miscellaneous"), wxVERTICAL)
        sizer_21 = wxBoxSizer(wxHORIZONTAL)
        sizer_19 = wxStaticBoxSizer(wxStaticBox(self.panel_3, -1, "Objects"), wxVERTICAL)
        objectsButtons2Sizer = wxBoxSizer(wxHORIZONTAL)
        objectsButtons1Sizer = wxBoxSizer(wxHORIZONTAL)
        sizer_13 = wxBoxSizer(wxHORIZONTAL)
        sizer_17 = wxStaticBoxSizer(wxStaticBox(self.panel_3, -1, "Selected Points"), wxVERTICAL)
        selectedPointsButtons1Sizer = wxBoxSizer(wxHORIZONTAL)
        selectedPointsCursorSizer = wxBoxSizer(wxHORIZONTAL)
        sizer_18 = wxStaticBoxSizer(wxStaticBox(self.panel_3, -1, "Slices"), wxVERTICAL)
        sizer_7 = wxBoxSizer(wxHORIZONTAL)
        label_2 = wxStaticText(self.panel_3, -1, "New slice name:")
        sizer_7.Add(label_2, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_7.Add(self.createSliceComboBox, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_7.Add(self.button_2_2, 0, wxALIGN_CENTER_VERTICAL, 7)
        sizer_7.Add(100, 20, 0, 0, 0)
        sizer_18.Add(sizer_7, 0, wxALL|wxEXPAND, 4)
        sizer_18.Add(self.sliceGrid, 1, wxEXPAND, 4)
        sizer_3.Add(sizer_18, 0, wxLEFT|wxRIGHT|wxTOP, 7)
        selectedPointsCursorSizer.Add(self.label_1_2, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        selectedPointsCursorSizer.Add(self.sliceCursorText, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        selectedPointsCursorSizer.Add(self.label_4_2, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        selectedPointsCursorSizer.Add(self.sliceCursorNameCombo, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        selectedPointsCursorSizer.Add(self.button_6_2, 0, wxEXPAND, 0)
        sizer_17.Add(selectedPointsCursorSizer, 0, wxALL|wxEXPAND, 4)
        sizer_17.Add(self.pointsGrid, 1, wxEXPAND, 4)
        selectedPointsButtons1Sizer.Add(self.pointsSelectAllButton, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        selectedPointsButtons1Sizer.Add(self.pointsDeselectAllButton, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        selectedPointsButtons1Sizer.Add(self.pointsRemoveButton, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_17.Add(selectedPointsButtons1Sizer, 0, wxLEFT|wxRIGHT|wxTOP|wxEXPAND, 4)
        sizer_17.Add(self.pointInteractionCheckBox, 0, wxALL|wxALIGN_CENTER_VERTICAL, 4)
        sizer_3.Add(sizer_17, 0, wxLEFT|wxRIGHT|wxTOP, 7)
        sizer_13.Add(self.label_5_1, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_13.Add(self.surfacePickActionChoice, 0, wxALIGN_CENTER_VERTICAL, 0)
        sizer_19.Add(sizer_13, 0, wxALL, 4)
        sizer_19.Add(self.objectsListGrid, 0, 0, 4)
        objectsButtons1Sizer.Add(self.button_9_1, 0, wxRIGHT, 4)
        objectsButtons1Sizer.Add(self.button_10_1, 0, wxRIGHT, 4)
        objectsButtons1Sizer.Add(self.button_3_1, 0, wxRIGHT, 4)
        objectsButtons1Sizer.Add(self.button_2_1, 0, wxRIGHT, 4)
        objectsButtons1Sizer.Add(self.button_4_1, 0, wxRIGHT, 4)
        sizer_19.Add(objectsButtons1Sizer, 0, wxLEFT|wxRIGHT|wxTOP|wxEXPAND, 4)
        objectsButtons2Sizer.Add(self.button_11_1, 0, wxRIGHT, 4)
        objectsButtons2Sizer.Add(self.button_3, 0, wxRIGHT, 4)
        objectsButtons2Sizer.Add(self.button_13_1, 0, wxRIGHT, 4)
        objectsButtons2Sizer.Add(self.button_4, 0, wxRIGHT, 4)
        sizer_19.Add(objectsButtons2Sizer, 0, wxALL, 4)
        sizer_3.Add(sizer_19, 0, wxLEFT|wxRIGHT|wxTOP, 7)
        sizer_21.Add(self.voiEnabledCheckBox, 0, wxALIGN_CENTER_VERTICAL, 0)
        sizer_21.Add(self.label_7, 0, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        sizer_21.Add(self.voiBoundsText, 1, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        sizer_21.Add(self.label_7_1, 0, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        sizer_21.Add(self.voiExtentText, 1, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        sizer_20.Add(sizer_21, 0, wxALL|wxEXPAND, 4)
        sizer_3.Add(sizer_20, 0, wxALL|wxEXPAND, 7)
        self.panel_3.SetAutoLayout(1)
        self.panel_3.SetSizer(sizer_3)
        sizer_3.Fit(self.panel_3)
        sizer_3.SetSizeHints(self.panel_3)
        sizer_16.Add(self.panel_3, 0, 0, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_16)
        sizer_16.Fit(self)
        sizer_16.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class controlFrame


class ControlFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # content of this block not found: did you rename this class?
        pass

    def __set_properties(self):
        # content of this block not found: did you rename this class?
        pass

    def __do_layout(self):
        # content of this block not found: did you rename this class?
        pass

# end of class ControlFrame


class MainFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # content of this block not found: did you rename this class?
        pass

    def __set_properties(self):
        # content of this block not found: did you rename this class?
        pass

    def __do_layout(self):
        # content of this block not found: did you rename this class?
        pass

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

