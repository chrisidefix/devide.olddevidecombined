#
# Source files
#
# Here is where you can add the name of your local Algorithms classes.
#

SET (Algorithms_SRCS 
     vtkITKPDEDeformableRegistrationFilter.cxx)

# --------------------------------------------------------------------------
# You probably do not need to modify anything below this line

#
# Create the vtkitkdvAlgorithms C++ library
#

ADD_LIBRARY (vtkitkdvAlgorithms Algorithms_SRCS)

#
# Create the vtkitkdvAlgorithms Tcl library
#

IF (VTK_WRAP_TCL AND VTKITKDV_WRAP_TCL)

  VTK_WRAP_TCL2 (vtkitkdvAlgorithmsTCL AlgorithmsTCL_SRCS ${Algorithms_SRCS})
  ADD_LIBRARY (vtkitkdvAlgorithmsTCL SHARED AlgorithmsTCL_SRCS)
  TARGET_LINK_LIBRARIES (vtkitkdvAlgorithmsTCL 
			 vtkFilteringTCL
			 vtkCommonTCL)

ENDIF (VTK_WRAP_TCL AND VTKITKDV_WRAP_TCL)

#
# Create the vtkitkdvAlgorithms Python library
#

IF (VTK_WRAP_PYTHON AND VTKITKDV_WRAP_PYTHON)

  VTK_WRAP_PYTHON2 (vtkitkdvAlgorithmsPython AlgorithmsPython_SRCS ${Algorithms_SRCS})
  ADD_LIBRARY(vtkitkdvAlgorithmsPython SHARED ${AlgorithmsPython_SRCS})
  TARGET_LINK_LIBRARIES(vtkitkdvAlgorithmsPython
  			vtkitkdvAlgorithms
			vtkFilteringPython
			vtkImagingPython
			vtkCommonPython)

ENDIF (VTK_WRAP_PYTHON AND VTKITKDV_WRAP_PYTHON)

#
# Link to VTK and local
#

TARGET_LINK_LIBRARIES (
  vtkitkdvAlgorithms
  vtkFiltering
  vtkImaging
  vtkCommon
  ITKIO
  ITKNumerics
  ITKBasicFilters
  ITKAlgorithms
)
