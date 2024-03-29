# Copyright (c) Charl P. Botha, TU Delft
# All rights reserved.
# See COPYRIGHT for details.

import vtk
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor
import wx
from module_kits.wx_kit import utils as wxutils

import wx.lib.agw.aui as aui
wx.aui = aui

from wx.html import HtmlWindow

class SimpleHTMLListBox(wx.HtmlListBox):
    """Simple class to emulate normal wx.ListBox (Append, Clear, GetClientData
    and GetString methods) with the super-powers of the wx.HtmlListBox.

    @author Charl P. Botha <http://cpbotha.net/>
    """

    def __init__(self, *args, **kwargs):
        wx.HtmlListBox.__init__(self, *args, **kwargs)
        self.items = []
        self.Clear()

    def Append(self, text, data=None, refresh=True):
        """Emulates wx.ListBox Append method, except for refresh bit.

        Set refresh to False if you're going to be appending bunches of
        items.  When you're done, call the DoRefresh() method explicitly.
        """
        
        self.items.append((text, data))
        if refresh:
            self.SetItemCount(len(self.items))
            self.Refresh()

    def DoRefresh(self):
        """To be used after adding large amounts of items with Append and
        refresh=False.
        """
        
        self.SetItemCount(len(self.items))
        self.Refresh()

    def Clear(self):
        del self.items[:]
        self.SetSelection(-1)
        self.SetItemCount(0)

    def GetClientData(self, n):
        if n >= 0 and n < len(self.items):
            return self.items[n][1]
        else:
            return None

    def GetCount(self):
        return len(self.items)
    
    def GetSelections(self):
        """Return list of selected indices just like the wx.ListBox.
        """
        
        # coded up this method purely to see if we could use SimpleHTMLListBox also
        # for the module categories thingy

        sels = []
        item, cookie = self.GetFirstSelected()            
        while item != wx.NOT_FOUND:
            sels.append(item)
            # ... process item ...
            item = self.GetNextSelected(cookie)
            
        return sels        
        

    def GetString(self, n):
        if n >= 0 and n < len(self.items):
            return self.items[n][0]
        else:
            return None
        
    def OnGetItem(self, n):
        try:
            return '<font size=-1>%s</font>' % (self.items[n][0],)
        except IndexError:
            return ''


class ProgressStatusBar(wx.StatusBar):
    """
    StatusBar with progress gauge embedded.
    
    Code adapted from wxPython demo.py | CustomStatusBar.
    """

    def __init__(self, parent):
        wx.StatusBar.__init__(self, parent, -1)

        # This status bar has three fields
        self.SetFieldsCount(2)
        # Sets the three fields to be relative widths to each other.
        self.SetStatusWidths([-2, -1])
        self.sizeChanged = False
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

        # Field 0 ... just text
        #self.SetStatusText("A Custom StatusBar...", 0)

        # This will fall into field 1 (the second field)
        self.gauge = wx.Gauge(self, -1, 100)
        self.gauge.SetValue(50)

        # set the initial position of the checkbox
        self.Reposition()
        
        # i have this timer purely for the progress bar to pulsate
        # up and down. personally, it's nice to see that the software
        # is alive.
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(50)
        self.Notify()
        
    def Notify(self):
        if self.gauge.GetValue() == 100:
            self.gauge.Pulse()
    

    def OnSize(self, evt):
        self.Reposition()  # for normal size events

        # Set a flag so the idle time handler will also do the repositioning.
        # It is done this way to get around a buglet where GetFieldRect is not
        # accurate during the EVT_SIZE resulting from a frame maximize.
        self.sizeChanged = True


    def OnIdle(self, evt):
        if self.sizeChanged:
            self.Reposition()


    # reposition the checkbox
    def Reposition(self):
        border = 3
        rect = self.GetFieldRect(1)
        self.gauge.SetPosition((rect.x+border, rect.y+border))
        self.gauge.SetSize((rect.width-border*2, rect.height-border*2))
        self.sizeChanged = False

class MainWXFrame(wx.Frame):
    """Class for building main user interface frame.

    All event handling and other intelligence should be elsewhere.
    """

    def __init__(self, parent, id=-1, title="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE |
                                            wx.SUNKEN_BORDER |
                                            wx.CLIP_CHILDREN):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        # tell FrameManager to manage this frame        
        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(self)

        self._make_menu()

        # statusbar
        self.statusbar = ProgressStatusBar(self)
        self.SetStatusBar(self.statusbar)

        self.SetMinSize(wx.Size(400, 300))

        # could make toolbars here

        # now we need to add panes

        # on GTK, this sequence is flipped!  search panel is at the
        # bottom, module list at the top.
        sp = self._create_module_search_panel()
        self._mgr.AddPane(
            sp,
            wx.aui.AuiPaneInfo().Name('module_search').
            Caption('Module Search and Categories').Left().Position(0).
            MinSize(sp.GetSize()).
            CloseButton(False))

        # a little trick I found in the PyAUI source code.  This will make
        # sure that the pane is as low (small y) as it can be
        p = self._mgr.GetPane('module_search')
        p.dock_proportion = 0

        self.module_list = self._create_module_list()
        self._mgr.AddPane(
            self.module_list,
            wx.aui.AuiPaneInfo().Name('module_list').Caption('Module List').
            Left().CloseButton(False))


        ##################################################################
        # setup VTK rendering pipeline for the graph editor

        self._rwi, self._ren = self._create_graph_canvas()

        self._mgr.AddPane(
            self._rwi,
            wx.aui.AuiPaneInfo().Name('graph_canvas').
            Caption('Graph Canvas').CenterPane())

        ##################################################################
        # these two also get swapped on GTK
       
        self._mgr.AddPane(
            self._create_documentation_window(),
            wx.aui.AuiPaneInfo().Name('doc_window').
            Caption('Module Help').Bottom().CloseButton(False))

        self._mgr.AddPane(
            self._create_log_window(),
            wx.aui.AuiPaneInfo().Name('log_window').
            Caption('Log Messages').Bottom().CloseButton(False))
 
      
        self._mgr.Update()
        
        # save this perspective
        self.perspective_default = self._mgr.SavePerspective()

        wx.EVT_MENU(self, self.window_default_view_id,
                    lambda e: self._mgr.LoadPerspective(
            self.perspective_default) and self._mgr.Update())
        

    def close(self):
        self._ren.RemoveAllViewProps()
        del self._ren
        self._rwi.GetRenderWindow().Finalize()
        self._rwi.SetRenderWindow(None)
        del self._rwi
        self.Destroy()

    def _create_documentation_window(self):
        self.doc_window = HtmlWindow(self, -1, size=(200,80))
        fsa = wxutils.create_html_font_size_array()
        self.doc_window.SetFonts("", "", fsa) 
        return self.doc_window

    def _create_graph_canvas(self):


        rwi = wxVTKRenderWindowInteractor(self, -1,
                size=(400,400))

        # we have to call this, else moving a modal dialogue over the
        # graph editor will result in trails.  Usually, a wxVTKRWI
        # refuses to render if its top-level parent is disabled.  This
        # is to stop VTK pipeline updates whilst wx.SafeYield() is
        # being called.  In _this_ case, the VTK pipeline is safe, so
        # we can disable this check.
        rwi.SetRenderWhenDisabled(True)
        ren = vtk.vtkRenderer()
        rwi.GetRenderWindow().AddRenderer(ren)

        rw = rwi.GetRenderWindow()
        rw.SetLineSmoothing(1)
        rw.SetPointSmoothing(1)

        # PolygonSmoothing is not really necessary for the GraphEditor
        # (yet), and on a GeForce 4600 Ti on Linux with driver version
        # 1.0-9639, you can see triangle lines bisecting quads.  Not
        # a nice artifact, so I've disabled this for now.
        #rw.SetPolygonSmoothing(1)

        return (rwi, ren)



    def _create_log_window(self):
        tc = wx.TextCtrl(
            self, -1, "", size=(200, 80),
            style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        self.message_log_text_ctrl = tc
        return tc

    def _create_module_list(self):
        self.module_list_box = SimpleHTMLListBox(
            self, -1, size=(200,200),
            style=wx.LB_SINGLE|wx.LB_NEEDED_SB)
        return self.module_list_box

    def _create_module_search_panel(self):
        search_panel = wx.Panel(self, -1)

        self.search = wx.SearchCtrl(search_panel, size=(200,-1), style=wx.TE_PROCESS_ENTER)
        self.search.ShowSearchButton(1)
        self.search.ShowCancelButton(1)
        
        self.module_cats_choice = wx.Choice(search_panel,-1, size=(200,-1)) 

        tl_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # option=0 so it doesn't fill vertically
        tl_sizer.Add(self.search, 0, wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, 4)
        tl_sizer.Add(self.module_cats_choice, 0, wx.EXPAND|wx.ALL, 4)
        
        search_panel.SetAutoLayout(True)
        search_panel.SetSizer(tl_sizer)
        search_panel.GetSizer().Fit(search_panel)
        search_panel.GetSizer().SetSizeHints(search_panel)

        return search_panel

    def _create_progress_panel(self):
        progress_panel = wx.Panel(self, -1)#, size=wx.Size(100, 50))
        self.progress_text = wx.StaticText(progress_panel, -1, "...")
        self.progress_text.SetFont(
           wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.progress_gauge = wx.Gauge(progress_panel, -1, 100)
        self.progress_gauge.SetValue(50)
        #self.progress_gauge.SetBackgroundColour(wx.Colour(50, 50, 204))

        tl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # these are in a vertical sizer, so expand will make them draw
        # out horizontally as well
        sizer.Add(self.progress_text, 0, wx.EXPAND | wx.BOTTOM, 4)
        sizer.Add(self.progress_gauge, 0, wx.EXPAND)

        tl_sizer.Add(sizer, 1, wx.EXPAND | wx.ALL, 7)
        
        #sizer.SetMinSize((100, 50))
        progress_panel.SetAutoLayout(True)
        progress_panel.SetSizer(tl_sizer)
        progress_panel.GetSizer().Fit(progress_panel)
        progress_panel.GetSizer().SetSizeHints(progress_panel)

        return progress_panel

    def _make_menu(self):
        # Menu Bar
        self.menubar = wx.MenuBar()
        self.SetMenuBar(self.menubar)
        self.fileNewId = wx.NewId()
        self.fileOpenId = wx.NewId()
        self.fileOpenSegmentId = wx.NewId()
        self.fileSaveId = wx.NewId()
        self.id_file_save_as = wx.NewId()
        self.id_file_export = wx.NewId()
        self.fileSaveSelectedId = wx.NewId()
        self.fileExportAsDOTId = wx.NewId()
        self.fileExportSelectedAsDOTId = wx.NewId()
        self.fileExitId = wx.NewId()
        self.window_python_shell_id = wx.NewId()
        self.helpShowHelpId = wx.NewId()
        self.helpAboutId = wx.NewId()

        
        file_menu = wx.Menu()
        file_menu.Append(self.fileNewId, "&New\tCtrl-N",
                         "Create new network.", wx.ITEM_NORMAL)
        file_menu.Append(self.fileOpenId, "&Open\tCtrl-O",
                         "Open and load existing network.", wx.ITEM_NORMAL)
        file_menu.Append(
            self.fileOpenSegmentId, "Open as Se&gment\tCtrl-G",
            "Open a DeVIDE network as a segment in the copy buffer.",
            wx.ITEM_NORMAL)
        file_menu.Append(self.fileSaveId, "&Save\tCtrl-S",
                         "Save the current network.", wx.ITEM_NORMAL)
        file_menu.Append(self.id_file_save_as, "Save &As",
                         "Save the current network with a new filename.", wx.ITEM_NORMAL)
        file_menu.Append(self.id_file_export, "&Export\tCtrl-E",
                "Export the current network with relative filenames",
                wx.ITEM_NORMAL)
        file_menu.Append(self.fileSaveSelectedId,
                         "Save se&lected Glyphs\tCtrl-L",
                         "Save the selected glyphs as a network.",
                         wx.ITEM_NORMAL)
        file_menu.AppendSeparator()
        file_menu.Append(
            self.fileExportAsDOTId, "Export as DOT file",
            "Export the current network as a GraphViz DOT file.",
            wx.ITEM_NORMAL)
        file_menu.Append(self.fileExportSelectedAsDOTId,
                         "Export selection as DOT file",
                         "Export the selected glyphs as a GraphViz DOT file.",
                         wx.ITEM_NORMAL)
        file_menu.AppendSeparator()
        file_menu.Append(self.fileExitId, "E&xit\tCtrl-Q",
                         "Exit DeVIDE!", wx.ITEM_NORMAL)
        self.menubar.Append(file_menu, "&File")

        self.edit_menu = wx.Menu()
        self.menubar.Append(self.edit_menu, "&Edit")

        modules_menu = wx.Menu()

        self.id_modules_search = wx.NewId()
        modules_menu.Append(
            self.id_modules_search, "Search for modules\tCtrl-F",
            "Change input "
            "focus to module search box.", wx.ITEM_NORMAL)
        
        self.id_rescan_modules = wx.NewId()
        modules_menu.Append(
            self.id_rescan_modules, "Rescan modules", "Recheck all module "
            "directories for new modules and metadata.", wx.ITEM_NORMAL)

        self.id_refresh_module_kits = wx.NewId()
        modules_menu.Append(
            self.id_refresh_module_kits, "Refresh module kits",
            "Attempt to refresh / reload all module_kits.", wx.ITEM_NORMAL)
        
        self.menubar.Append(modules_menu, "&Modules")

        self.network_menu = wx.Menu()
        self.menubar.Append(self.network_menu, "&Network")

        window_menu = wx.Menu()

        self.window_default_view_id = wx.NewId()
        window_menu.Append(
            self.window_default_view_id, "Restore &default view",
            "Restore default perspective / window configuration.",
            wx.ITEM_NORMAL)
        
        window_menu.Append(self.window_python_shell_id, "&Python Shell",
                                "Show the Python Shell interface.",
                                wx.ITEM_NORMAL)
        self.menubar.Append(window_menu, "&Window")

        help_menu = wx.Menu()
        help_menu.Append(self.helpShowHelpId, "Show &Help\tF1", "",
                         wx.ITEM_NORMAL)
        help_menu.Append(self.helpAboutId, "About", "",
                                wx.ITEM_NORMAL)
        
        self.menubar.Append(help_menu, "&Help")
        # Menu Bar end

    def set_progress(self, percentage, message):
        self.statusbar.gauge.SetValue(percentage)
        self.statusbar.SetStatusText(message, 0)
        
