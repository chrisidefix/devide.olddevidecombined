#include "itkImage.h"
#include "itkSymmetricForcesDemonsRegistrationFilter.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
#include "itkCSwigImages.h"

namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(
    itkSymmetricForcesDemonsRegistrationFilter);
  namespace wrappers
  {
    ITK_WRAP_OBJECT3(SymmetricForcesDemonsRegistrationFilter,
                     image::F2, image::F2, image::VF2,
                     itkSymmetricForcesDemonsRegistrationFilterF2F2);
    ITK_WRAP_OBJECT3(SymmetricForcesDemonsRegistrationFilter,
                     image::F3, image::F3, image::VF3,
                     itkSymmetricForcesDemonsRegistrationFilterF3F3);
  }
}

#endif
