#include "itkImage.h"
#include "itkLevelSetMotionRegistrationFilter.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
#include "itkCSwigImages.h"

namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(
    itkLevelSetMotionRegistrationFilter);
  namespace wrappers
  {
    ITK_WRAP_OBJECT3(LevelSetMotionRegistrationFilter,
                     image::F2, image::F2, image::VF2,
                     itkLevelSetMotionRegistrationFilterF2F2);
    ITK_WRAP_OBJECT3(LevelSetMotionRegistrationFilter,
                     image::F3, image::F3, image::VF3,
                     itkLevelSetMotionRegistrationFilterF3F3);
  }
}

#endif
