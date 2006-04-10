#!/usr/bin/env python
# -*- coding: ANSI_X3.4-1968 -*-
# generated by wxGlade 0.4 on Fri Mar 24 11:28:21 2006

import wx
from wx import py
import module_kits.wx_kit

class CodeRunnerFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: CodeRunnerFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.view_frame_panel = wx.Panel(self, -1)
        self.main_splitter = wx.SplitterWindow(self.view_frame_panel, -1, style=wx.SP_3D|wx.SP_BORDER)
        self.window_1_pane_2 = wx.Panel(self.main_splitter, -1)
        self.window_1_pane_1 = wx.Panel(self.main_splitter, -1)
        self.edit_notebook = wx.Notebook(self.window_1_pane_1, -1, style=0)
        self.notebook_1_pane_3 = wx.Panel(self.edit_notebook, -1)
        self.notebook_1_pane_2 = wx.Panel(self.edit_notebook, -1)
        self.notebook_1_pane_1 = wx.Panel(self.edit_notebook, -1)
        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        self.SetMenuBar(self.frame_1_menubar)
        self.file_open_id = wx.NewId()
        self.file_save_id = wx.NewId()
        self.run_id = wx.NewId()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(self.file_open_id, "&Open file to current edit\tCtrl-O", "Load a file into the current edit tab", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(self.file_save_id, "&Save current edit to file\tCtrl-S", "Save current edit tab to file", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(self.run_id, "&Run current edit\tCtrl-Enter", "Run the current edit tab code in the shell context", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "&File")
        # Menu Bar end
        self.scratch_editwindow = module_kits.wx_kit.dvedit_window.DVEditWindow(self.notebook_1_pane_1, -1)
        self.setup_editwindow = module_kits.wx_kit.dvedit_window.DVEditWindow(self.notebook_1_pane_2, -1)
        self.execute_editwindow = module_kits.wx_kit.dvedit_window.DVEditWindow(self.notebook_1_pane_3, -1)
        self.shell_window = module_kits.wx_kit.dvshell.DVShell(self.window_1_pane_2, -1)
        self.statusbar = self.CreateStatusBar(1, 0)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: CodeRunnerFrame.__set_properties
        self.SetTitle("DeVIDE CodeRunner")
        self.SetSize((480, 480))
        self.statusbar.SetStatusWidths([-1])
        # statusbar fields
        statusbar_fields = ["Welcome to the CodeRunner"]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: CodeRunnerFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_6_copy_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_6_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_6.Add(self.scratch_editwindow, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 7)
        self.notebook_1_pane_1.SetAutoLayout(True)
        self.notebook_1_pane_1.SetSizer(sizer_6)
        sizer_6.Fit(self.notebook_1_pane_1)
        sizer_6.SetSizeHints(self.notebook_1_pane_1)
        sizer_6_copy.Add(self.setup_editwindow, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 7)
        self.notebook_1_pane_2.SetAutoLayout(True)
        self.notebook_1_pane_2.SetSizer(sizer_6_copy)
        sizer_6_copy.Fit(self.notebook_1_pane_2)
        sizer_6_copy.SetSizeHints(self.notebook_1_pane_2)
        sizer_6_copy_1.Add(self.execute_editwindow, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 7)
        self.notebook_1_pane_3.SetAutoLayout(True)
        self.notebook_1_pane_3.SetSizer(sizer_6_copy_1)
        sizer_6_copy_1.Fit(self.notebook_1_pane_3)
        sizer_6_copy_1.SetSizeHints(self.notebook_1_pane_3)
        self.edit_notebook.AddPage(self.notebook_1_pane_1, "Scratch")
        self.edit_notebook.AddPage(self.notebook_1_pane_2, "Setup")
        self.edit_notebook.AddPage(self.notebook_1_pane_3, "Execute")
        sizer_5.Add(self.edit_notebook, 1, wx.EXPAND, 0)
        self.window_1_pane_1.SetAutoLayout(True)
        self.window_1_pane_1.SetSizer(sizer_5)
        sizer_5.Fit(self.window_1_pane_1)
        sizer_5.SetSizeHints(self.window_1_pane_1)
        sizer_4.Add(self.shell_window, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 7)
        sizer_4.Add((0, 100), 0, wx.ADJUST_MINSIZE, 0)
        self.window_1_pane_2.SetAutoLayout(True)
        self.window_1_pane_2.SetSizer(sizer_4)
        sizer_4.Fit(self.window_1_pane_2)
        sizer_4.SetSizeHints(self.window_1_pane_2)
        self.main_splitter.SplitHorizontally(self.window_1_pane_1, self.window_1_pane_2)
        sizer_3.Add(self.main_splitter, 1, wx.EXPAND, 0)
        sizer_3.Add((400, 0), 0, wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(sizer_3, 1, wx.ALL|wx.EXPAND, 7)
        self.view_frame_panel.SetAutoLayout(True)
        self.view_frame_panel.SetSizer(sizer_2)
        sizer_2.Fit(self.view_frame_panel)
        sizer_2.SetSizeHints(self.view_frame_panel)
        sizer_1.Add(self.view_frame_panel, 1, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class CodeRunnerFrame


