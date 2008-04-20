# TODO: test this with a VTK head checkout as well

import vtk

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

    for i in range(-4, 3, 1):
        ta = vtk.vtkTextActor()
        ta.SetInput('%d: Hello World' % (i,))
        ta.ScaledTextOn()

        x = 1.0 * i
        y = 2.0 * i

        ta.GetPositionCoordinate().SetCoordinateSystemToWorld()
        ta.GetPositionCoordinate().SetValue(x, y)   

        # documentation claims that p2c is relative to pc, but in
        # VTK ParaView-3-2-1 that is not the case.  x is relative, y
        # is just plain whacky.  See below...

        # CASE A:
        # if we set y2 to 1.0 for example, everything with a y-coord
        # above 0 has the same y-position.  Everything below 0 has
        # half the spacing it should have
        # see http://tinyurl.com/6jlr9e (vtktextactor_ybug_case_a.png)

        # CASE B:
        # if we try working around this by setting y2 to y+1.0 (i.e.
        # we DON'T assume that it's relative), everything with y >= 0
        # is fine, everything below is at the right position, but
        # about half the height of everything with y above 0
        # see http://tinyurl.com/6dfj47 (vtktextactor_ybug_case_b.png) 

        # CASE A:
        #y2 = 1.0

        # CASE B
        y2 = y + 1.0 

        x2 = x + 7

        ta.GetPosition2Coordinate().SetCoordinateSystemToWorld()

        # this is a WORK-AROUND for the broken vtkTextActor position /
        # scaling in VTK ParaView-3-2-1
        # only works if vtkTextActor justification mode is left at
        # default (I think that this has something to do with the fact
        # that the font scaling and the positioning interpret
        # position[2]coordinate differently.
        if y < 0:
            # with y under 0, Position2Coordinate IS relative to
            # PositionCoordinate
            ta.GetPosition2Coordinate().SetValue(7, 1)
        else:
            # with y == 0 or above, Position2Coordinate's y-coordinate
            # has to specified absolutely
            ta.GetPosition2Coordinate().SetValue(7, y2)

        tprop = ta.GetTextProperty()
        tprop.SetFontFamilyToArial()
        #tprop.SetVerticalJustificationToCentered()
        #tprop.SetFontSize(12)
        tprop.SetBold(0)
        tprop.SetItalic(0)
        tprop.SetShadow(0)
        tprop.SetColor((0,0,0.4))

        ############################

        ren.AddActor(ta)

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

    ren.ResetCamera()
    rw.Render()

    rwi.Start()

if __name__ == "__main__":
    main()

