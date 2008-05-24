import vtk

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
    ta = vtk.vtkTextActor3D()
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

    print ta.GetBounds()

    ren.AddActor(ta)


    ss = vtk.vtkSphereSource()
    ss.SetRadius(32)
    sm = vtk.vtkPolyDataMapper()
    sm.SetInput(ss.GetOutput())
    sa = vtk.vtkActor()
    sa.SetMapper(sm)
    sa.SetPosition((pos[0],pos[1],0))
    ren.AddActor(sa)

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

    if False:
        # add a sphere source to calibrate
        # this should in theory be at the same position as the
        # vtkTextActor
        ss = vtk.vtkSphereSource()
        ss.SetRadius(0.1)
        sm = vtk.vtkPolyDataMapper()
        sm.SetInput(ss.GetOutput())
        sa = vtk.vtkActor()
        sa.SetMapper(sm)
        sa.SetPosition((x,y,0))
        ren.AddActor(sa)

        # add a sphere source to calibrate
        # this should in theory be at the same position as the
        # vtkTextActor
        ss = vtk.vtkSphereSource()
        ss.SetRadius(0.1)
        sm = vtk.vtkPolyDataMapper()
        sm.SetInput(ss.GetOutput())
        sa = vtk.vtkActor()
        sa.SetMapper(sm)
        sa.SetPosition((x2,y2,0))
        ren.AddActor(sa)

    make_glyph(ren, (0,0), 'Hello there\nHoo you too')

    make_glyph(ren, (0,100), 'Hey there g\nand hoo goo')

    ren.ResetCamera()
    rw.Render()

    rwi.Start()

if __name__ == "__main__":
    main()

