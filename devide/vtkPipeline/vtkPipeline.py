#!/usr/bin/env python
#
# $Id: vtkPipeline.py,v 1.3 2002/04/30 01:25:17 cpbotha Exp $
#
# This python program/module creates a graphical VTK pipeline browser.  
# The objects in the pipeline can be configured.
#
# Copyright (C) 2000 Prabhu Ramachandran
# Conversion to wxPython copyright (c) 2002 Charl P. Botha
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
# 
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA  02111-1307, USA.
#
# Author contact information:
#   Prabhu Ramachandran <prabhu_r@users.sf.net>
#   http://www.aero.iitm.ernet.in/~prabhu/
#
#   Charl P. Botha <cpbotha@ieee.org>
#   http://cpbotha.net/


"""  This python program/module creates a graphical VTK pipeline
browser.   The pipeline tree is made using the TreeWidget from IDLE.
The objects in the pipeline can be configured.  The configuration is
done by using the ConfigVtkObj class.
"""

from wxPython.wx import *
import string, re, types
import ConfigVtkObj

# set this to 1 if you want to see debugging messages - very useful if
# you have problems
DEBUG=0
def debug (msg):
    if DEBUG:
	print msg

# A hack to prevent vtkTransform.GetInverse() infinite loops
last_transform = 0

icon_map = {'RenderWindow': 'renwin', 'Renderer': 'ren',
            'Actor': 'actor', 'Light': 'light', 'Camera': 'camera',
            'Mapper': 'process', 'Property': 'file',
	    'Coordinate': 'coord', 'Source': 'data', 
            'LookupTable': 'colormap', 'Reader': 'data',
            'Assembly': 'actor', 'Python': 'python', 'Dummy1': 'question'}

def get_icon (vtk_obj):
    strng = vtk_obj.GetClassName ()[3:]
    for key in icon_map.keys ():
	if string.find (strng, key) > -1:
	    return [key, vtk_obj, icon_map[key]]
    return ["", vtk_obj, "question"]


def remove_method (name, methods, method_names):
    "Removes methods if they have a particular name."
    
    debug ("vtkPipeline.py: remove_methods(\'%s\', methods, "\
           "method_names)"%name)
    try:
        idx = method_names.index(name)
    except ValueError:
        pass
    else:
        del methods[idx], method_names[idx]
    return methods, method_names
    

def get_methods (vtk_obj):
    """Obtain the various methods from the passed object.  This
    function also cleans up the method names to check for."""

    debug ("vtkPipeline.py: get_methods(vtk_obj)")
    methods = str (vtk_obj)
    methods = string.split (methods, "\n")
    del methods[0]

    # using only the first set of indented values.
    patn = re.compile ("  \S")
    for method in methods[:]:
	if patn.match (method):
            if string.find (method, ":") == -1:
                methods.remove (method)
            elif string.find (method[1], "none") > -1:
                methods.remove (method)	
        else:
	    methods.remove (method)    

    method_names = []
    for i in range (0, len (methods)):
	strng = methods[i]
	strng = string.replace (strng, " ", "")
	methods[i] = string.split (strng, ":")
        method_names.append (methods[i][0])

    # Bug! :(
    # Severe bug - causes segfault with readers and renderwindows on
    # older VTK releases    
    if re.match ("vtk\w*RenderWindow", vtk_obj.GetClassName ()) or \
       re.match ("vtk\w*Reader", vtk_obj.GetClassName ()):
        remove_method('FileName', methods, method_names)

    if re.match ("vtk\w*Renderer", vtk_obj.GetClassName ()):
	methods.append (["ActiveCamera", ""])

    if re.match ("vtk\w*Assembly", vtk_obj.GetClassName ()):
        methods.append (["Parts", ""])
        methods.append (["Volumes", ""])
        methods.append (["Actors", ""])

    # fixes bug with infinite loop for GetInverse() method.  Thanks to
    # "Blezek, Daniel J" <blezek@crd.ge.com> for reporting it.    
    global last_transform
    if vtk_obj.IsA('vtkAbstractTransform'):
        if last_transform:
            remove_method('Inverse', methods, method_names)
        else:
            last_transform = last_transform + 1
    else:
        last_transform = 0

    # Some of these object are removed because they arent useful in
    # the browser.  I check for Source and Input anyway so I dont need
    # them.    
    for name in ('Output', 'FieldData', 'CellData', 'PointData',
                 'Source', 'Input'):
        remove_method(name, methods, method_names)
    
    return methods


# A new idea - more general.  Using this I can obtain a lot more
# objects in the pipeline
def get_vtk_objs (vtk_obj):
    "Obtain vtk objects from the passed objects."

    debug ("vtkPipeline.py: get_vtk_objs (%s)"%
	   (vtk_obj.GetClassName ()))
    methods = get_methods(vtk_obj)

    vtk_objs = []
    for method in methods:
	try:
	    t = eval ("vtk_obj.Get%s ().GetClassName ()"%method[0])
	except:
	    pass
	else:
	    if string.find (t, "Collection") > -1:		
		col = eval ("vtk_obj.Get%s ()"%method[0])
		col.InitTraversal ()
		n = col.GetNumberOfItems ()
		prop = 0
		if re.match ("vtkProp\w*C", t):
		    prop = 1
		for i in range (0, n):
		    if prop:
			obj = col.GetNextProp ()
		    else:
			obj = col.GetNextItem ()
		    icon = get_icon (obj)
		    vtk_objs.append (["%s%d"%(icon[0], i), obj, icon[2]])
	    else:
		obj = eval ("vtk_obj.Get%s ()"%method[0])
		vtk_objs.append (get_icon (obj))

    icon = icon_map['Source']
    try:
        obj = vtk_obj.GetSource ()
    except:
        pass
    else:
        if obj:
            vtk_objs.append (["Source", obj, icon])
    try: 
        n_s = vtk_obj.GetNumberOfSources ()
    except:
        pass
    else:
        for i in range (0, n_s):
            obj = vtk_obj.GetSource (i)
            vtk_objs.append (["Source%d"%i, obj, icon])

    try:  
        obj = vtk_obj.GetInput ()
    except:  
        pass
    else:
        if obj:
            icon = get_icon (obj)
            vtk_objs.append (icon)
    
    return vtk_objs

def recursively_add_children(tree_ctrl, parent_node):
    """Utility function to fill out wxTreeCtrl.

    Pass this function a wxTreeCtrl and _a_ node, and it will fill out
    everything below it by using Prabhu's code.
    """
    children = get_vtk_objs(tree_ctrl.GetPyData(parent_node))
    for i in children:
        # get_vtk_objs() conveniently calls get_icon as well
        img_idx = icon_map.values().index(i[2])
        if i[0]:
            text = i[0] + " (" + i[1].GetClassName() + ")"
        else:
            text = i[1].GetClassName()
        # now add the node with image index
        ai = tree_ctrl.AppendItem(parent_node, text, img_idx)
        # and set the data to be the actual vtk object
        tree_ctrl.SetPyData(ai, i[1])
        
        # and we get to call ourselves!
        recursively_add_children(tree_ctrl, ai)

def item_activate_cb(parent_window, renwin, tree_ctrl, tree_event):
    """Callback for activation (double clicking) of tree node.

    parent_window is the window of which the configuration window will be a
    child.  renwin is the render window that will be updated.
    """
    obj = tree_ctrl.GetPyData(tree_event.GetItem())
    if hasattr(obj, 'GetClassName'):
        conf = ConfigVtkObj.ConfigVtkObj(renwin)
        conf.configure(parent_window, obj)
        


class vtkPipelineBrowser:
    "Browses the VTK pipleline given a vtkRenderWindow."

    def __init__ (self, parent, renwin, objs=None):
        """Constructor of the vtkPipelineBrowser.

        If objs == None, this class assumes that you want a full pipeline
        which it will extract starting at the renwin.  If you have some
        vtk objects however, this class will act as a segment browser with
        those objects as the root nodes.
        """
        
	self.renwin = renwin
        self._objs = objs

        self._frame = wxFrame(parent=parent, id=-1,
                              title="VTK Pipeline Browser")
        EVT_CLOSE(self._frame, self.close)

        panel = wxPanel(parent=self._frame, id=-1)

        tree_id = wxNewId()
        self._tree_ctrl = wxTreeCtrl(parent=panel,
                                     id=tree_id,
                                     size=wxSize(300,400),
                                     style=wxTR_HAS_BUTTONS)
        EVT_TREE_ITEM_ACTIVATED(panel, tree_id,
                                lambda e, pw=self._frame, rw=self.renwin,
                                tc=self._tree_ctrl:
                                item_activate_cb(pw, rw, tc, e))

        button_sizer = wxBoxSizer(wxHORIZONTAL)

        refr_id = wxNewId()
        refr = wxButton(parent=panel, id=refr_id, label="Refresh")
        EVT_BUTTON(panel, refr_id, self.refresh)
        button_sizer.Add(refr)

        q_id = wxNewId()
        q = wxButton(parent=panel, id=q_id, label="Close")
        EVT_BUTTON(panel, q_id, self.close)
        button_sizer.Add(q)

        top_sizer = wxBoxSizer(wxVERTICAL)

        top_sizer.Add(self._tree_ctrl, option=1, flag=wxEXPAND)
        top_sizer.Add(button_sizer, option=0, flag=wxALIGN_CENTER_HORIZONTAL)

        panel.SetAutoLayout(true)
        panel.SetSizer(top_sizer)
        top_sizer.Fit(self._frame)
        top_sizer.SetSizeHints(self._frame)

        self._frame.Show(true)

        self._image_list = wxImageList(16,16)
        for i in icon_map.keys():
            self._image_list.Add(wxBitmap("Icons/" + icon_map[i] + ".xpm",
                                          wxBITMAP_TYPE_XPM))
        self._tree_ctrl.SetImageList(self._image_list)

    def browse (self):
	"Display the tree and interact with the user."
        self.clear()

        if self._objs == None:
            rw_idx = icon_map.keys().index("RenderWindow")
            self._root = self._tree_ctrl.AddRoot(text="RenderWindow",
                                                 image=rw_idx)
            self._tree_ctrl.SetPyData(self._root, self.renwin)
            recursively_add_children(self._tree_ctrl, self._root)
        else:
            im_idx = icon_map.keys().index("Python")
            self._root = self._tree_ctrl.AddRoot(text="Root",
                                                 image=im_idx)
            self._tree_ctrl.SetPyData(self._root, None)
            
            for i in self._objs:
                # we should probably do a stricter check
                if hasattr(i, 'GetClassName'):
                    icon = get_icon(i)
                    img_idx = icon_map.values().index(icon[2])
                    if icon[0]:
                        text = "%s (%s)" % (icon[0],i.GetClassName())
                    else:
                        text = i.GetClassName()
                    ai = self._tree_ctrl.AppendItem(self._root, text, img_idx)
                    self._tree_ctrl.SetPyData(ai, i)
                    recursively_add_children(self._tree_ctrl, ai)
                
        
        self._tree_ctrl.Expand(self._root)
        
    def refresh (self, event=None):
        self.browse()

    def clear (self):
        self._tree_ctrl.DeleteAllItems()

    def close(self, event=None):
	"Exit the browser."
        self.clear()
        self._frame.Destroy()
        


def main ():
    import vtkpython
    from vtk.wx.wxVTKRenderWindow import wxVTKRenderWindow
    
    cone = vtkpython.vtkConeSource()
    cone.SetResolution(8)
    transform = vtkpython.vtkTransformFilter ()
    transform.SetInput ( cone.GetOutput() )
    transform.SetTransform ( vtkpython.vtkTransform() )
    coneMapper = vtkpython.vtkPolyDataMapper()
    coneMapper.SetInput(transform.GetOutput())
    l = vtkpython.vtkLookupTable ()
    coneMapper.SetLookupTable (l)
    coneActor = vtkpython.vtkActor()
    coneActor.SetMapper(coneMapper)    
    axes = vtkpython.vtkCubeAxesActor2D ()

    app = wxPySimpleApp()
    frame = wxFrame(None, -1, "wxRenderWindow", size=wxSize(400,400))
    wid = wxVTKRenderWindow(frame, -1)

    ren = vtkpython.vtkRenderer()
    renWin = wid.GetRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(300,300)
    ren.AddActor (coneActor)
    ren.AddActor (axes)
    axes.SetCamera (ren.GetActiveCamera ())
    renWin.Render ()

    debug ("Starting VTK Pipeline Browser...")
    pipe = vtkPipelineBrowser (frame, renWin)
    pipe.browse ()

    pipe_segment = vtkPipelineBrowser(frame, renWin, (coneActor, axes))
    pipe_segment.browse()

    app.MainLoop()

if __name__ == "__main__":
    main ()
