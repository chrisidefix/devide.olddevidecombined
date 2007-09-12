from gen_mixins import SubjectMixin
import vtk


#############################################################################
class DeVIDECanvasObject(SubjectMixin):
    
    def __init__(self, position):
        # call parent ctor
        SubjectMixin.__init__(self)
        
        self._position = position
        self._canvas = None
        self._observers = {'enter' : [],
                           'exit' : [],
                           'drag' : [],
                           'buttonDown' : [],
                           'buttonUp' : [],
                           'buttonDClick' : [],
                           'motion' : []}
    def close(self):
        """Take care of any cleanup here.
        """

        SubjectMixin.close(self)

    def get_bounds(self):
        raise NotImplementedError

    def get_position(self):
        return self._position

    def set_position(self, destination):
        self._position = destination

    def get_canvas(self):
        return self._canvas

    def hit_test(self, x, y):
        return False

    def isInsideRect(self, x, y, width, height):
        return False

    def set_canvas(self, canvas):
        self._canvas = canvas


#############################################################################

class DeVIDECanvasLine(DeVIDECanvasObject):

    # this is used by the routing algorithm to route lines around glyphs
    # with a certain border; this is also used by updateEndPoints to bring
    # the connection out of the connection port initially
    routingOvershoot = 10

    def __init__(self, fromGlyph, fromOutputIdx, toGlyph, toInputIdx):
        """A line object for the canvas.

        linePoints is just a list of python tuples, each representing a
        coordinate of a node in the line.  The position is assumed to be
        the first point.
        """

        self.fromGlyph = fromGlyph
        self.fromOutputIdx = fromOutputIdx
        self.toGlyph = toGlyph
        self.toInputIdx = toInputIdx

        # 'BLACK' removed
        colourNames = ['BLUE', 'BROWN', 'MEDIUM FOREST GREEN',
                       'DARKORANGE1']
        self.lineColourName = colourNames[self.toInputIdx % (len(colourNames))]
        

        # any line begins with 4 (four) points

        self.updateEndPoints()

        canvasObject.__init__(self, self._linePoints[0])        


    def close(self):
        # delete things that shouldn't be left hanging around
        del self.fromGlyph
        del self.toGlyph

    def draw(self, dc):
        # lines are 2 pixels thick
        dc.SetPen(wx.wxPen(self.lineColourName, 2, wx.wxSOLID))

        # simple mode: just the lines thanks.
        #dc.DrawLines(self._linePoints)

        # spline mode for N points:
        # 1. Only 4 points: drawlines.  DONE
        # 2. Draw line from 0 to 1
        # 3. Draw line from N-2 to N-1 (second last to last)
        # 4. Draw spline from 1 to N-2 (second to second last)
#         if len(self._linePoints) > 4:
#             dc.DrawLines(self._linePoints[0:2]) # 0 - 1
#             dc.DrawLines(self._linePoints[-2:]) # second last to last
#             dc.DrawSpline(self._linePoints[1:-1])
#         else:
#             dc.DrawLines(self._linePoints)

        dc.SetPen(wx.wxPen('BLACK', 4, wx.wxSOLID))
        dc.DrawSpline(self._linePoints)
        dc.SetPen(wx.wxPen(self.lineColourName, 2, wx.wxSOLID))
        dc.DrawSpline(self._linePoints)
                          
    def getBounds(self):
        # totally hokey: for now we just return the bounding box surrounding
        # the first two points - ideally we should iterate through the lines,
        # find extents and pick a position and bounds accordingly
        return (self._linePoints[-1][0] - self._linePoints[0][0],
                self._linePoints[-1][1] - self._linePoints[0][1])

    def getUpperLeftWidthHeight(self):
        """This returns the upperLeft coordinate and the width and height of
        the bounding box enclosing the third-last and second-last points.
        This is used for fast intersection checking with rectangles.
        """

        p3 = self._linePoints[-3]
        p2 = self._linePoints[-2]

        upperLeftX = [p3[0], p2[0]][bool(p2[0] < p3[0])]
        upperLeftY = [p3[1], p2[1]][bool(p2[1] < p3[1])]
        width = abs(p2[0] - p3[0])
        height = abs(p2[1] - p3[1])
                                    
        return ((upperLeftX, upperLeftY), (width,  height))

    def getThirdLastSecondLast(self):
        return (self._linePoints[-3], self._linePoints[-2])
            

    def hitTest(self, x, y):
        # maybe one day we will make the hitTest work, not tonight
        # I don't need it
        return False

    def insertRoutingPoint(self, x, y):
        """Insert new point x,y before second-last point, i.e. the new point
        becomes the third-last point.
        """
        if (x,y) not in self._linePoints:
            self._linePoints.insert(len(self._linePoints) - 2, (x, y))
            return True
        else:
            return False

    def updateEndPoints(self):
        # first get us just out of the port, then create margin between
        # us and glyph
        boostFromPort = self._pHeight / 2 + coLine.routingOvershoot
        
        self._linePoints = [(), (), (), ()]
        
        self._linePoints[0] = self.fromGlyph.getCenterOfPort(
            1, self.fromOutputIdx)
        self._linePoints[1] = (self._linePoints[0][0],
                               self._linePoints[0][1] + boostFromPort)

        
        self._linePoints[-1] = self.toGlyph.getCenterOfPort(
            0, self.toInputIdx)
        self._linePoints[-2] = (self._linePoints[-1][0],
                                self._linePoints[-1][1] - boostFromPort)

#############################################################################
class DeVIDECanvasGlyph(DeVIDECanvasObject):

    # at start and end of glyph
    _horizBorder = 5
    # between ports
    _horizSpacing = 5
    # at top and bottom of glyph
    _vertBorder = 15
    _pWidth = 10
    _pHeight = 10

    _label_height = 10


    t = vtk.vtkVectorText()
    t.SetText('M')
    t.Update()
    b = t.GetOutput().GetBounds()
    _label_scale = _label_height / (b[3] - b[2])

    def __init__(self, position, numInputs, numOutputs,
                 labelList, moduleInstance):
        # parent constructor
        #coRectangle.__init__(self, position, (0,0))
        DeVIDECanvasObject.__init__(self, position)

        # we'll fill this out later
        self._size = (0,0)
        self._numInputs = numInputs
        self.inputLines = [None] * self._numInputs
        self._numOutputs = numOutputs
        # be careful with list concatenation!
        self.outputLines = [[] for i in range(self._numOutputs)]
        self._labelList = labelList
        self.moduleInstance = moduleInstance
        self.draggedPort = None
        self.enteredPort = None
        self.selected = False
        self.blocked = False

        self._assembly = vtk.vtkAssembly()
        self._rbs = vtk.vtkRectangularButtonSource()
        self._rbsa = vtk.vtkActor()
        self._ts = vtk.vtkVectorText()
        self._tsa = vtk.vtkActor()

        self._iportssa = \
            [(vtk.vtkSphereSource(),vtk.vtkActor()) for _ in
                range(self._numInputs)]

        self._oportssa = \
            [(vtk.vtkSphereSource(),vtk.vtkActor()) for _ in
                range(self._numInputs)]

    def close(self):
        del self.moduleInstance
        del self.inputLines
        del self.outputLines

    def create_assembly(self):
        normal_colour = (192, 192, 192)
        selected_colour = (255, 0, 246)
        blocked_colour = (16, 16, 16)

        colour = normal_colour

        if self.selected:
            colour = [selected_colour[i] * 0.5 + colour[i] * 0.5
                      for i in range(3)]

        if self.blocked:
            colour = [blocked_colour[i] * 0.5 + colour[i] * 0.5
                      for i in range(3)]

        colour = tuple([int(i) for i in colour])

        # TEXT LABEL ##############################################
        self._ts.SetText('\n'.join(self._labelList))
        self._ts.Update()
        m= vtk.vtkPolyDataMapper()
        m.SetInput(self._ts.GetOutput())
        self._tsa.SetMapper(m)

        self._tsa.SetScale(self._label_scale)
        inity = self._vertBorder + \
                self._label_height * (len(self._labelList) - 1)
        # still have to tune inity with the space between lines...
        initx = self._horizSpacing
        # y is the bottom left of the first character
        self._tsa.SetPosition(initx, inity, 0.1)

        # we also need the text width for later
        b = self._ts.GetOutput().GetBounds()
        text_width = self._label_scale * (b[1] - b[2]) + \
            2 * self._horizBorder

        self._assembly.AddPart(self._tsa)
        
        # RECT BUTTON ##############################################
        # calculate our size
        # the width is the maximum(textWidth + twice the horizontal border,
        # all ports, horizontal borders and inter-port borders added up)
        maxPorts = max(self._numInputs, self._numOutputs)
        portsWidth = 2 * self._horizBorder + \
                     maxPorts * self._pWidth + \
                     (maxPorts - 1 ) * self._horizSpacing


        
        self._size = (max(text_width, portsWidth),
                      self._label_height * len(self._labelList) + \
                      2 * self._vertBorder)

        self._rbs.SetBoxRatio(1.0)
        self._rbs.SetTwoSided(1)
        self._rbs.SetHeight(self._size[1])
        self._rbs.SetWidth(self._size[0])

        m = vtk.vtkPolyDataMapper()
        m.SetInput(self._rbs.GetOutput())
        self._rbsa.SetMapper(m)
        # usually the position is the CENTRE of the button, so we
        # adjust so that the bottom left corner ends up at 0,0
        self._rbsa.SetPosition((self._size[0] / 2.0, 
            self._size[1] / 2.0, 0.0))

        self._rbsa.GetProperty().SetColor((0.0, 1.0, 0.0))

        self._assembly.AddPart(self._rbsa)

        # INPUTS #################################################### 
        horizOffset = self._horizBorder
        horizStep = self._pWidth + self._horizSpacing
        #connBrush = wx.wxBrush("GREEN")
        #disconnBrush = wx.wxBrush("RED")
        
        for i in range(self._numInputs):
            s,a = self._iportssa[i]
            m = vtk.vtkPolyDataMapper()
            m.SetInput(s.GetOutput())
            a.SetMapper(m)
            a.SetPosition((horizOffset + i * horizStep,
                self._size[1], 0))

            self._assembly.AddPart(a)

        for i in range(self._numOutputs):
            s,a = self._oportssa[i]
            m = vtk.vtkPolyDataMapper()
            m.SetInput(s.GetOutput())
            a.SetMapper(m)
            a.SetPosition((horizOffset + i * horizStep, 0, 0))

            self._assembly.AddPart(a)

        self._assembly.SetPosition(self._position + (0.0,))

    def findPortContainingMouse(self, x, y):
        """Find port that contains the mouse pointer.  Returns tuple
        containing inOut and port index.
        """

        horizOffset = self._position[0] + self._horizBorder
        horizStep = self._pWidth + self._horizSpacing
        
        bx = horizOffset
        by = self._position[1]
        
        for i in range(self._numInputs):
            if x >= bx and x <= bx + self._pWidth and \
               y >= by and y < by + self._pHeight:

                return (0, i)
            
            bx += horizStep

        bx = horizOffset
        by = self._position[1] + self._size[1] - self._pHeight
        
        for i in range(self._numOutputs):
            if x >= bx and x <= bx + self._pWidth and \
               y >= by and y < by + self._pHeight:

                return (1, i)
            
            bx += horizStep
            
        return None

    def getCenterOfPort(self, inOrOut, idx):

        horizOffset = self._position[0] + self._horizBorder
        horizStep = self._pWidth + self._horizSpacing
        cy = self._position[1] + self._pHeight / 2

        if inOrOut:
            cy += self._size[1] - self._pHeight 

        cx = horizOffset + idx * horizStep + self._pWidth / 2

        return (cx, cy)

    def getLabel(self):
        return ' '.join(self._labelList)
        
    def setLabelList(self,labelList):
        self._labelList = labelList
       
