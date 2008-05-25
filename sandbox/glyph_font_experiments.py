import vtk
import vtkdevide

def make_glyph(ren, pos, message):
    """vtkTextActor3D does almost exactly what I need, even
    multi-lines, although the documentation claims otherwise.

    Only thing I need now is to be able to query the bounds of the
    generated texture image.

    From experiments with the sphere at the origin, it does seem that
    setting the font size to x-points, makes the text line, from the
    bottom-most feature to the top-most, x-world units high.  I don't
    know how to get to the inter-line spacing yet though...
    """
    ta = vtkdevide.vtkDVTextActor3D()
    ta.SetInput(message)

    tprop = ta.GetTextProperty()
    tprop.SetFontFamilyToArial()
    #tprop.SetVerticalJustificationToCentered()
    tprop.SetFontSize(32)
    tprop.SetBold(0)
    tprop.SetItalic(0)
    tprop.SetShadow(0)
    tprop.SetColor((0,0,0))

    ta.SetPosition((pos[0], pos[1],0))
    #ta.SetPosition((pos[0], pos[1]))

    ta.UpdateImageActor()

    # I have *NO* idea why I have to this, but if I don't,  I get the
    # following error message with "What ghte hell" (it's the 'g'):
    # 
    # RuntimeError: ERROR: In ..\..\..\archive\VTK\
    # Filtering\vtkStreamingDemandDrivenPipeline.cxx, line 698
    # vtkStreamingDemandDrivenPipeline (0182B9B0): The update extent 
    # specified in the information for output port 0 on algorithm 
    # vtkTrivialProducer(01829DA8) is 0 255 0 63 0 0, which is 
    # outside the whole extent 0 255 0 31 0 0.
    # investigation shows that the DisplayExtent of the imageactor is
    # indeed larger than the wholeextent of the imagedata, although
    # these two are set to be equal in the UpdateImageActor.
    ta.GetImageActor().SetDisplayExtent(ta.GetImageData().GetWholeExtent())


    ren.AddActor(ta)


    ss = vtk.vtkSphereSource()
    ss.SetRadius(32)
    sm = vtk.vtkPolyDataMapper()
    sm.SetInput(ss.GetOutput())
    sa = vtk.vtkActor()
    sa.SetMapper(sm)
    sa.SetPosition((pos[0],pos[1],0))
    ren.AddActor(sa)

    return ta

def main():
    rwi = vtk.vtkRenderWindowInteractor()

    istyle = vtk.vtkInteractorStyleImage()
    rwi.SetInteractorStyle(istyle)

    rw = vtk.vtkRenderWindow()
    rwi.SetRenderWindow(rw)

    ren = vtk.vtkRenderer()
    ren.SetBackground(1,1,1)
    ren.GetActiveCamera().SetParallelProjection(1)
    rw.AddRenderer(ren)

    rwi.Initialize()


    ta1 = make_glyph(ren, (0,0), 'Hello there\nHoo you too')

    ta2 = make_glyph(ren, (0,100), 'What ghte hell')

    ren.ResetCamera()
    try:
        rw.Render()
    except RuntimeError:
        import pdb
        pdb.set_trace()

    print ta2.GetBounds()

    rwi.Start()

if __name__ == "__main__":
    main()

