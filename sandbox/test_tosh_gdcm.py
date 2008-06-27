# script to demonstrate difference in behaviour of GDCM with toshiba
# dataset on Windows (MIP is okay) and on Linux (MIP is empty!)

# bang, this was due to a dl / DLFCN thing on AMD64.  You can't import
# vtk before vtkgdcm, then it screws up.  Apply this patch to fix:
#http://public.kitware.com/cgi-bin/viewcvs.cgi/Wrapping/Python/vtk/__init__.py?r1=1.13&r2=1.14&pathrev=MAIN

import vtkgdcm
import gdcm
import vtk

r = vtkgdcm.vtkGDCMImageReader()
r.SetFileName('tosh_data')
r.Update()

print r.GetMedicalImageProperties()
print 'DIMENSIONS:', r.GetOutput().GetDimensions()
print r.GetNumberOfScalarComponents()

