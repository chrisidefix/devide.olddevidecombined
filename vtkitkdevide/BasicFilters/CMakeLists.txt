#
# Source files
#
# Here is where you can add the name of your local BasicFilters classes.
#

SET (BasicFilters_SRCS 
     vtkITKDVCannyEdgeDetectionImageFilter.cxx)

# --------------------------------------------------------------------------
# You probably do not need to modify anything below this line

#
# Create the vtkitkdvBasicFilters C++ library
#

ADD_LIBRARY (vtkitkdvBasicFilters BasicFilters_SRCS)

#
# Create the vtkitkdvBasicFilters Tcl library
#

IF (VTK_WRAP_TCL AND VTKITKDV_WRAP_TCL)

  VTK_WRAP_TCL (vtkitkdvBasicFiltersTCL BasicFiltersTCL_SRCS ${BasicFilters_SRCS})
  ADD_LIBRARY (vtkitkdvBasicFiltersTCL SHARED BasicFiltersTCL_SRCS)
  TARGET_LINK_LIBRARIES (vtkitkdvBasicFiltersTCL
                         vtkitkdvBasicFilters
                         vtkitkdvCommonTCL
			 vtkFilteringTCL
			 vtkCommonTCL)

ENDIF (VTK_WRAP_TCL AND VTKITKDV_WRAP_TCL)

#
# Create the vtkitkdvBasicFilters Python library
#

IF (VTK_WRAP_PYTHON AND VTKITKDV_WRAP_PYTHON)

  VTK_WRAP_PYTHON (vtkitkdvBasicFiltersPython BasicFiltersPython_SRCS ${BasicFilters_SRCS})
  ADD_LIBRARY(vtkitkdvBasicFiltersPython SHARED ${BasicFiltersPython_SRCS})
  TARGET_LINK_LIBRARIES(vtkitkdvBasicFiltersPython
  			vtkitkdvBasicFilters
                        vtkitkdvCommonPython
			vtkFilteringPython
			vtkImagingPython
			vtkCommonPython)

ENDIF (VTK_WRAP_PYTHON AND VTKITKDV_WRAP_PYTHON)

#
# Link to VTK and local
#

TARGET_LINK_LIBRARIES (
  vtkitkdvBasicFilters
  vtkFiltering
  vtkImaging
  vtkCommon
  ITKIO
  ITKNumerics
  ITKBasicFilters
  ITKBasicFilters
)
