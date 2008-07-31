#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.3 on Thu Jul 31 11:33:04 2008

import wx

# begin wxGlade: extracode
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor

from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor

# end wxGlade



class SlicinatorFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SlicinatorFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.notebook_1 = wx.Notebook(self.panel_1, -1, style=0)
        self.sizer_9_staticbox = wx.StaticBox(self.panel_1, -1, "Actions")
        self.sizer_8_staticbox = wx.StaticBox(self.panel_1, -1, "Tools")
        self.sizer_5_staticbox = wx.StaticBox(self.panel_1, -1, "Objects")
        self.label_3 = wx.StaticText(self.panel_1, -1, "Select / create:")
        self.choice_1 = wx.Choice(self.panel_1, -1, choices=["object 1", "Create new object ..."])
        self.label_2 = wx.StaticText(self.panel_1, -1, "Create:")
        self.choice_2 = wx.Choice(self.panel_1, -1, choices=["polygonal contour", "2D levelset"])
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.window_1 = wxVTKRenderWindowInteractor(self.panel_1, -1)
        self.spin_ctrl_1 = wx.SpinCtrl(self.panel_1, -1, "", min=0, max=100)
        self.button_1 = wx.Button(self.panel_1, -1, "Burninate")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SlicinatorFrame.__set_properties
        self.SetTitle("The Slicinator")
        self.SetSize((800, 600))
        self.choice_1.SetSelection(0)
        self.choice_2.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SlicinatorFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.StaticBoxSizer(self.sizer_8_staticbox, wx.VERTICAL)
        sizer_9 = wx.StaticBoxSizer(self.sizer_9_staticbox, wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11.Add(self.label_3, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_11.Add(self.choice_1, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_5, 0, 0, 7)
        sizer_10.Add(self.label_2, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_10.Add(self.choice_2, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_9, 0, wx.EXPAND, 0)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "Tool 1")
        sizer_8.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 0, wx.RIGHT|wx.EXPAND, 7)
        sizer_6.Add(self.window_1, 1, wx.EXPAND, 0)
        sizer_7.Add(self.spin_ctrl_1, 0, 0, 0)
        sizer_7.Add(self.button_1, 0, 0, 0)
        sizer_6.Add(sizer_7, 0, 0, 0)
        sizer_3.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.ALL|wx.EXPAND, 7)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class SlicinatorFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    slicinator_frame = SlicinatorFrame(None, -1, "")
    app.SetTopWindow(slicinator_frame)
    slicinator_frame.Show()
    app.MainLoop()
