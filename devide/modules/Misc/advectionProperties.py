#
#
#

from moduleBase import moduleBase
from moduleMixins import scriptedConfigModuleMixin
import moduleUtils
import operator
import vtk
import wx

class advectionProperties(scriptedConfigModuleMixin, moduleBase):
    """Given a series of prepared advection volumes (each input is a
    timestep), calculate a number of metrics.

    The first input HAS to have a VolumeIndex PointData attribute/array.  For
    example, the output of the pointsToSpheres that you used BEFORE having
    passed through the first probeFilters.  This first input will NOT be used
    for the actual calculations, but only for point -> volume lookups.
    Calculations will be performed for the second input and onwards.

    $Revision: 1.2 $
    """

    _numberOfInputs = 10

    def __init__(self, moduleManager):
        moduleBase.__init__(self, moduleManager)

        self._config.csvFilename = ''

        configList = [
            ('CSV Filename:', 'csvFilename', 'base:str', 'filebrowser',
             'Filename Comma-Separated-Values file that will be written.',
             {'fileMode' : wx.SAVE,
              'fileMask' : 'CSV files (*.csv)|*.csv|All files (*.*)|*.*'})]
        
        scriptedConfigModuleMixin.__init__(self, configList)

        self._inputs = [None] * self._numberOfInputs
        
        #moduleUtils.setupVTKObjectProgress(self, self._warpVector,
        #                                   'Warping points.')

        self._createWindow(
            {'Module (self)' : self})

        # pass the data down to the underlying logic
        self.configToLogic()
        # and all the way up from logic -> config -> view to make sure
        self.syncViewWithLogic()

    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        for inputIdx in range(len(self.getInputDescriptions())):
            self.setInput(inputIdx, None)

        # this will take care of all display thingies
        scriptedConfigModuleMixin.close(self)
        
        # get rid of any references
        

    def executeModule(self):
        # inputs are arranged according to timesteps (presumably)
        # things have been marked with a VolumeIndex array

        # find valid inputs with VolumeIndex scalars
        newInputs = [i for i in self._inputs if i != None]

        # we need at the very least three inputs:
        # the VolumeIndex input and the actual volumes that will be used
        if len(newInputs) < 3:
            raise Exception, 'This module requires a minimum of 3 inputs.'

        # make sure everything is up to date
        [i.Update() for i in newInputs]        

        # the first input MUST have a VolumeIndex attribute
        if newInputs[0].GetPointData().GetScalars('VolumeIndex') == None:
            raise Exception, 'The first input must have ' \
                  'a VolumeIndex scalar attribute.'

        # now we're going to build up a dictionary to translate
        # from volume index to a list of point ids
        vis = newInputs[0].GetPointData().GetScalars('VolumeIndex')
        volIdxToPtIds = {}
        for ptid in xrange(vis.GetNumberOfTuples()):
            vidx = vis.GetTuple1(ptid)
            if vidx >= 0:
                if vidx in volIdxToPtIds:
                    volIdxToPtIds[vidx].append(ptid)
                else:
                    volIdxToPtIds[vidx] = [ptid]
            
        # 1. calculate centroids
        # centroids is a dictionary with volume index as key
        # centroids over time as the values

        # create dict with keys == volumeIds; values will be lists
        # of centroids over time
        centroids = {}
        for volIdx in volIdxToPtIds:
            centroids[volIdx] = []

        for volIdx in centroids:
            # get all pointIds for this volume
            ptIds = volIdxToPtIds[volIdx]
            # do all timesteps
            for tsi in range(len(newInputs) - 1):
                pd = newInputs[tsi + 1]
                coordSums = [0,0,0]
                for ptId in ptIds:
                    coordSums = map(operator.add, coordSums,
                                    pd.GetPoint(ptId))

                # calc centroid
                numPoints = float(len(ptIds))
                centroid = map(lambda e: e / numPoints, coordSums)
                centroids[volIdx].append(centroid)

        # now use the centroids to build table
        volids = centroids.keys()
        volids.sort()

        # centroidVectors of the format:
        # step-label, vol0 x, vol0 y, vol0 z, vol0 mag, vol1 x, vol1 y, etc.
        centroidVectors = []

        # newInputs - 1 for the first input, -1 because we're doing vectors
        for tsi in range(len(newInputs) - 2):
            # new row
            centroidVectors.append(['%d - %d' % (tsi, tsi+1)])
            for volIdx in volids:
                cvec = map(operator.sub,
                           centroids[volIdx][tsi+1], centroids[volIdx][tsi])
                centroidVectors[-1].extend(cvec)
                # also the sum of motion
                centroidVectors[-1].append(vtk.vtkMath.Norm(cvec))

        if self._config.csvFilename:
            # write centroid vectors
            csvFile = file(self._config.csvFilename, 'w')
            labelString = 'step-label'
            for volid in volids:
                labelString = '%s, vol%d x, vol%d y, vol%d z, vol%d mag' % \
                              (labelString,volid,volid,volid,volid)

            # write label string
            csvFile.write('%s\n' % (labelString,))

            # first we write the centroids (naughty)
            for tsi in range(len(newInputs) - 1):
                cline = "'%d'" % (tsi,)
                for volid in volids:
                    # get me the centroid for this volid and this step
                    c = centroids[volid][tsi]
                    cline = '%s, %.3f, %.3f, %.3f, 0' % \
                            (cline, c[0], c[1], c[2])

                csvFile.write('%s\n' % (cline,))
                    
            
            # then we write the centroid motion vectors
            for cvecLine in centroidVectors:
                # strip off starting and ending []
                csvFile.write('%s\n' % (str(cvecLine)[1:-1],))

    def getInputDescriptions(self):
        return ('vtkPolyData with VolumeIndex attribute',) * \
               self._numberOfInputs

    def setInput(self, idx, inputStream):
        validInput = False
        
        try:
            if inputStream.GetClassName() == 'vtkPolyData':
                validInput = True
        except:
            # we come here if GetClassName() is not callable (or doesn't
            # exist) - but things could still be None
            if inputStream == None:
                validInput = True

        if validInput:
            self._inputs[idx] = inputStream
        else:
            raise TypeError, 'This input requires a vtkPolyData.'

    def getOutputDescriptions(self):
        return ()

    def getOutput(self, idx):
        raise Exception

    def logicToConfig(self):
        pass
    
    def configToLogic(self):
        pass
