#include "itkImage.h"
#include "itkTPGACLevelSetImageFilter.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
#include "itkCSwigImages.h"

namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkTPGACLevelSetImageFilter);
  namespace wrappers
  {
    ITK_WRAP_OBJECT2(TPGACLevelSetImageFilter, image::F3, image::F3,
                     itkTPGACLevelSetImageFilterF3F3);
  }
}

#endif
