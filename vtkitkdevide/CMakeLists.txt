#
# Set the project name.
#

PROJECT (VTKITKDV)

#
# Assume everything is set up correctly for build.
#
# If some requirements are not met, set it to 0.
# In that case, the build won't be done.
#

SET (VTKITKDV_CAN_BUILD 1)

#
# Load CMake commands that you probably should not modify.
#

INCLUDE (${VTKITKDV_SOURCE_DIR}/CMakeOptions.cmake)

#
# If everything is OK, then go into the sub directories and build.
#

IF (VTKITKDV_CAN_BUILD)

  #
  # Here is where you can list the sub-directories holding your local 
  # classes. Sorting classes by 'package' type like VTK does (Common, 
  # Rendering, Filtering, Imaging, IO, etc.) is a good thing and prevents 
  # numerous dependencies problems.
  #

  SUBDIRS (
    Algorithms
  )

  #
  # You can put your include path(s) here
  #

  #INCLUDE_DIRECTORIES(${VTKITKDV_SOURCE_DIR}/IO)
  INCLUDE_DIRECTORIES(${VTKITK_INCLUDE_PATH}/Common)
  
  
  #
  # Common configuration settings
  #
  # Do not worry about this one.
  #

  CONFIGURE_FILE(
    ${VTKITKDV_SOURCE_DIR}/vtkitkdvConfigure.h.in
    ${VTKITKDV_BINARY_DIR}/vtkitkdvConfigure.h
  )

  INCLUDE_DIRECTORIES(${VTKITKDV_BINARY_DIR})

ENDIF (VTKITKDV_CAN_BUILD)
