import vtk
import wx
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor

def main():
    """Like it says, just a simple example
    """
    # every wx app needs an app
    app = wx.PySimpleApp()

    # create the top-level frame, sizer and wxVTKRWI
    frame = wx.Frame(None, -1, "vtk text rendering", size=(400,400))
    widget = wxVTKRenderWindowInteractor(frame, -1)
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(widget, 1, wx.EXPAND)
    frame.SetSizer(sizer)
    frame.Layout()

    # It would be more correct (API-wise) to call widget.Initialize() and
    # widget.Start() here, but Initialize() calls RenderWindow.Render().
    # That Render() call will get through before we can setup the 
    # RenderWindow() to render via the wxWidgets-created context; this
    # causes flashing on some platforms and downright breaks things on
    # other platforms.  Instead, we call widget.Enable().  This means
    # that the RWI::Initialized ivar is not set, but in THIS SPECIFIC CASE,
    # that doesn't matter.
    widget.Enable(1)

    widget.AddObserver("ExitEvent", lambda o,e,f=frame: f.Close())

    istyle = vtk.vtkInteractorStyleImage()
    widget.SetInteractorStyle(istyle)

    ren = vtk.vtkRenderer()
    ren.SetBackground(1,1,1)
    ren.GetActiveCamera().SetParallelProjection(1)
    widget.GetRenderWindow().AddRenderer(ren)

    if True:
        # vtkCaptionActor2D #####

        tsa = vtk.vtkCaptionActor2D()
        tsa.SetCaption('1: Hello World')
        tsa.LeaderOff()
        #tsa.BorderOff()

        tsa.SetAttachmentPoint(0,0,0)
        tsa.GetPositionCoordinate().SetValue(0.0, 0.0)   
        tsa.GetPosition2Coordinate().SetCoordinateSystemToWorld()
        tsa.GetPosition2Coordinate().SetValue(7,2,0)

        tprop = tsa.GetCaptionTextProperty()
        tprop.SetFontFamilyToArial()
        tprop.SetVerticalJustificationToCentered()
        tprop.SetFontSize(12)
        tprop.SetBold(0)
        tprop.SetItalic(0)
        tprop.SetShadow(0)
        #tprop.SetColor((1.0,1.0,1.0))
        tprop.SetColor((0,0,0))

        ############################

        ren.AddActor(tsa)

    if True:
        ta = vtk.vtkTextActor()
        ta.SetInput('2: Hello World')
        ta.ScaledTextOn()

        ta.GetPositionCoordinate().SetCoordinateSystemToWorld()
        ta.GetPositionCoordinate().SetValue(0.0, 2.0)   
        ta.GetPosition2Coordinate().SetCoordinateSystemToWorld()
        ta.GetPosition2Coordinate().SetValue(7,3,0)

        tprop = ta.GetTextProperty()
        tprop.SetFontFamilyToArial()
        tprop.SetVerticalJustificationToCentered()
        tprop.SetFontSize(12)
        tprop.SetBold(0)
        tprop.SetItalic(0)
        tprop.SetShadow(0)
        #tprop.SetColor((1.0,1.0,1.0))
        tprop.SetColor((0,0,0.2))

        ############################

        ren.AddActor(ta)

    # show the window
    frame.Show()

    app.MainLoop()

if __name__ == "__main__":
    main()

