#
# Source files
#
# Here is where you can add the name of your local Common classes.
#

SET (Common_SRCS 
     vtkITKDVImageToImageFilter.cxx
     vtkITKDVImageToImageFilterFF.cxx)
     
SET_SOURCE_FILES_PROPERTIES(
vtkITKDVImageToImageFilter
vtkITKDVImageToImageFilterFF
ABSTRACT
)

# --------------------------------------------------------------------------
# You probably do not need to modify anything below this line

#
# Create the vtkitkdvCommon C++ library
#

ADD_LIBRARY (vtkitkdvCommon Common_SRCS)

#
# Create the vtkitkdvCommon Tcl library
#

IF (VTK_WRAP_TCL AND VTKITKDV_WRAP_TCL)

  VTK_WRAP_TCL2 (vtkitkdvCommonTCL CommonTCL_SRCS ${Common_SRCS})
  ADD_LIBRARY (vtkitkdvCommonTCL SHARED CommonTCL_SRCS)
  TARGET_LINK_LIBRARIES (vtkitkdvCommonTCL 
			 vtkFilteringTCL
			 vtkCommonTCL)

ENDIF (VTK_WRAP_TCL AND VTKITKDV_WRAP_TCL)

#
# Create the vtkitkdvCommon Python library
#

IF (VTK_WRAP_PYTHON AND VTKITKDV_WRAP_PYTHON)

  VTK_WRAP_PYTHON2 (vtkitkdvCommonPython CommonPython_SRCS ${Common_SRCS})
  ADD_LIBRARY(vtkitkdvCommonPython SHARED ${CommonPython_SRCS})
  TARGET_LINK_LIBRARIES(vtkitkdvCommonPython
  			vtkitkdvCommon
			vtkFilteringPython
			vtkImagingPython
			vtkCommonPython)

ENDIF (VTK_WRAP_PYTHON AND VTKITKDV_WRAP_PYTHON)

#
# Link to VTK and local
#

TARGET_LINK_LIBRARIES (
  vtkitkdvCommon
  vtkFiltering
  vtkImaging
  vtkCommon
  ITKIO
  ITKNumerics
  ITKBasicFilters
  ITKCommon
)
