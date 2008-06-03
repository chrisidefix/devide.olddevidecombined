import vtk

def make_glyph(ren, pos, message):
    ta = vtk.vtkTextActor3D()
    ta.SetInput(message)

    tprop = ta.GetTextProperty()
    tprop.SetFontFamilyToArial()
    tprop.SetFontSize(32)
    tprop.SetBold(0)
    tprop.SetItalic(0)
    tprop.SetShadow(0)
    tprop.SetColor((0,0,0))

    ta.SetPosition((pos[0], pos[1],0))

    ren.AddActor(ta)

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


    # with the string "what gh", this will generate the following
    # error at render:

    # RuntimeError: ERROR: In ..\..\..\archive\VTK\Filtering\
    # vtkStreamingDemandDrivenPipeline.cxx, line 698
    # vtkStreamingDemandDrivenPipeline (017CF3C8): The update 
    # extent specified in the information for output port 0 on 
    # algorithm vtkTrivialProducer(017D2FF0) is 0 255
    # 0 63 0 0, which is outside the whole extent 0 255 0 31 0 0.

    # with the string "what h" (i.e. without the g and its downward
    # stroke, there's no error)
    ta2 = make_glyph(ren, (0,0), 'What h')

    ren.ResetCamera()
    rw.Render()

    rwi.Start()

if __name__ == "__main__":
    main()

