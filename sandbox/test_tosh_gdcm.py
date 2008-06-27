# script to demonstrate difference in behaviour of GDCM with toshiba
# dataset on 32 bit Linux/Windows and on 64 bit Linux

import gdcm
import vtk
import vtkgdcm

r = vtkgdcm.vtkGDCMImageReader()
r.SetFileName('tosh_data')
r.Update()

print r.GetMedicalImageProperties()

