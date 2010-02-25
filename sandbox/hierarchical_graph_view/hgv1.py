import vtk

cur_bs = 0.8

def observer_charevent(obj, evt_name, view):
    global cur_bs
    if obj.GetKeyCode() == 'B':
        cur_bs += 0.1
        if cur_bs > 1.0: cur_bs = 1.0
        view.SetBundlingStrength(cur_bs)
        view.GetRenderWindow().Render()
        print cur_bs
    elif obj.GetKeyCode() == 'b':
        cur_bs -= 0.1
        if cur_bs < 0.0: cur_bs = 0.0
        view.SetBundlingStrength(cur_bs)
        view.GetRenderWindow().Render()
        print cur_bs


def main():  
    tree_fn = "vtklibrary.xml";
    graph_fn = "vtkclasses.xml";

    reader1 = vtk.vtkXMLTreeReader()
    reader1.SetFileName(tree_fn)
    reader1.SetEdgePedigreeIdArrayName("tree edge")
    reader1.GenerateVertexPedigreeIdsOff()
    reader1.SetVertexPedigreeIdArrayName("id")

    reader2 = vtk.vtkXMLTreeReader()
    reader2.SetFileName(graph_fn)
    reader2.SetEdgePedigreeIdArrayName("graph edge")
    reader2.GenerateVertexPedigreeIdsOff()
    reader2.SetVertexPedigreeIdArrayName("id")

    reader1.Update()
    reader2.Update()

    # straight VTK
    # we need this for getting the view going
    rw = vtk.vtkRenderWindow()
    # and this
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(rw)

    iren.AddObserver('CharEvent', lambda o, e: observer_charevent(o,e,view))

    # connect existing rw+iren to the view
    view = vtk.vtkHierarchicalGraphView()
    view.SetupRenderWindow(rw)

    #view.DisplayHoverTextOff()
    view.GetRenderWindow().SetMultiSamples(0)
    view.SetHierarchyFromInputConnection(reader1.GetOutputPort())
    view.SetGraphFromInputConnection(reader2.GetOutputPort())
    view.SetVertexColorArrayName("VertexDegree")
    view.SetColorVertices(True)
    view.SetVertexLabelArrayName("id")
    view.SetVertexLabelVisibility(True)
    view.SetScalingArrayName("TreeRadius")
    view.SetBundlingStrength(cur_bs)

    view.Update()
    #view.SetGraphEdgeColorArrayName("graph edge")
    #view.SetColorGraphEdgesByArray(True)

    lstrat = 'tree'
    if lstrat == 'cosmic tree':
        cls = vtk.vtkCosmicTreeLayoutStrategy()
        cls.SetNodeSizeArrayName("VertexDegree")
        cls.SetSizeLeafNodesOnly(True)
    elif lstrat == 'circ':
        cls = vtk.vtkCircularLayoutStrategy()
    elif lstrat == 'tree':
        cls = vtk.vtkTreeLayoutStrategy()
        cls.SetAngle(360)
        cls.SetRadial(True)
        cls.SetLogSpacingValue(0.8)
        cls.SetLeafSpacing(0.9)

    view.SetLayoutStrategy(cls)

    theme = vtk.vtkViewTheme.CreateMellowTheme()
    theme.SetLineWidth(1)
    view.ApplyViewTheme(theme)
     
    view.GetRenderer().ResetCamera()
 
    iren.Initialize()
    rw.Render()
    iren.Start()


if __name__ == '__main__':
    main()


