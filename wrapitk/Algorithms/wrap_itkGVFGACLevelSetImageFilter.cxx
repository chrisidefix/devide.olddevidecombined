#include "itkImage.h"
#include "itkGVFGACLevelSetImageFilter.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
#include "itkCSwigImages.h"

namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkGVFGACLevelSetImageFilter);
  namespace wrappers
  {
    ITK_WRAP_OBJECT2(GVFGACLevelSetImageFilter, image::F3, image::F3,
                     itkGVFGACLevelSetImageFilterF3F3);
  }
}

#endif
