# $Id: shell_render_engine.py,v 1.3 2003/09/03 11:13:13 cpbotha Exp $
# example to test shell renderer (*shudder*)

from vtkpython import *
from vtkdscas import *
import time

def bench(camera, rwi):
    initial_time = time.clock()
    for i in range(36):
        camera.Azimuth(10)
        rwi.Render()
    
    end_time = time.clock()

    print "FPS == %f" % (36 / (end_time - initial_time))

def ce_cb(obj, evt_name):
    if obj.GetKeyCode() == 'm':
        crm = splatmapper.GetRenderMode()
	crm = crm + 1
	if crm > 2:
	    crm = 0
        splatmapper.SetRenderMode(crm)
        print "rendermode switched to %d" % (crm)

    elif obj.GetKeyCode() == '\'':
        cur = splatmapper.GetEllipsoidDiameter()
        splatmapper.SetEllipsoidDiameter(cur - 0.1)
        print "EllipsoidDiameter == %s" % str(cur - 0.1)
    elif obj.GetKeyCode() == ',':
        cur = splatmapper.GetEllipsoidDiameter()
        splatmapper.SetEllipsoidDiameter(cur + 0.1)
        print "EllipsoidDiameter == %s" % str(cur + 0.1)
        
    elif obj.GetKeyCode() == 'd':
        cur = splatmapper.GetGaussianRadialExtent()
        splatmapper.SetGaussianRadialExtent(cur - 0.1)
        print "GaussianRadialExtent == %s" % str(cur - 0.1)
    elif obj.GetKeyCode() == 'h':
        cur = splatmapper.GetGaussianRadialExtent()
        splatmapper.SetGaussianRadialExtent(cur + 0.1)
        print "GaussianRadialExtent == %s" % str(cur + 0.1)
        
    elif obj.GetKeyCode() == 't':
        cur = splatmapper.GetGaussianSigma()
        splatmapper.SetGaussianSigma(cur - 0.1)
        print "GaussianSigma == %s" % str(cur - 0.1)
    elif obj.GetKeyCode() == 'n':
        cur = splatmapper.GetGaussianSigma()
        splatmapper.SetGaussianSigma(cur + 0.1)
        print "GaussianSigma == %s" % str(cur + 0.1)
        
    elif obj.GetKeyCode() == 'b':
        bench(ren.GetActiveCamera(), rwi)
        
    rwi.Render()
        
        
reader = vtkImageReader()
reader.SetHeaderSize(0)
reader.SetFileDimensionality(3)
reader.SetFileName("engine.raw")
reader.SetDataScalarType(3)
reader.SetDataExtent(0,255,0,255,0,127)
reader.SetDataSpacing(1,1,1)

otf = vtkPiecewiseFunction()
otf.AddPoint(0.0, 0.0)
otf.AddPoint(130, 0.0)
otf.AddPoint(130.1, 1)
otf.AddPoint(180.0, 1)
otf.AddPoint(180.1, 1)
otf.AddPoint(255.0, 1)

ctf = vtkColorTransferFunction()
ctf.AddRGBPoint(0.0, 0.0, 0.0, 0.0)
ctf.AddRGBPoint(130, 0.0, 0.0, 0.0)
ctf.AddRGBPoint(130.1, 0.80, 0.80, 0.80)
ctf.AddRGBPoint(180.0, 0.80, 0.80, 0.80)
ctf.AddRGBPoint(180.1, 0.91, 0.61, 0.10)
ctf.AddRGBPoint(255.0, 0.91, 0.61, 0.10)

#se = vtkShellExtractor()
#se.SetInput(hdfr.GetOutput())
#se.SetOpacityTF(otf)
#se.SetOmegaL(0.8)
#se.SetOmegaH(0.99)

#se.Update()

splatmapper = vtkOpenGLVolumeShellSplatMapper()
splatmapper.SetOmegaL(0.1)
splatmapper.SetOmegaH(0.2)
splatmapper.SetInput(reader.GetOutput())
splatmapper.SetRenderMode(0)

vprop = vtkVolumeProperty()
vprop.SetScalarOpacity(otf)
vprop.SetColor(ctf);
vprop.ShadeOn()
vprop.SetAmbient(0.1)
vprop.SetDiffuse(0.7)
vprop.SetSpecular(0.2)
vprop.SetSpecularPower(10)

volume = vtkVolume()
volume.SetProperty(vprop)
volume.SetMapper(splatmapper)

ren = vtkRenderer()
ren.SetBackground(0.5, 0.5, 0.5)
ren.AddVolume(volume)
#ren.GetActiveCamera().ParallelProjectionOn()

renwin = vtkRenderWindow()
renwin.AddRenderer(ren)

rwi = vtkRenderWindowInteractor()
rwi.SetRenderWindow(renwin)

rwi.AddObserver('CharEvent', ce_cb)

#rwi.LightFollowCameraOn();
rwi.Initialize()
rwi.Start()

