/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_itkSigmoidImageFilter.cxx,v $
  Language:  C++
  Date:      $Date: 2004/12/03 23:50:14 $
  Version:   $Revision: 1.1 $

  Copyright (c) Insight Software Consortium. All rights reserved.
  See ITKCopyright.txt or http://www.itk.org/HTML/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/
#include "itkSigmoidImageFilter.h"
#include "itkImage.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
#include "itkCSwigImages.h"

namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkSigmoidImageFilter);
  namespace wrappers
  {
    //===========2D Wrapped Filters==============
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::F2 , image::F2 , itkSigmoidImageFilterF2F2  );
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::D2 , image::D2 , itkSigmoidImageFilterD2D2  );
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::UC2, image::UC2, itkSigmoidImageFilterUC2UC2);
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::US2, image::US2, itkSigmoidImageFilterUS2US2);
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::UI2, image::UI2, itkSigmoidImageFilterUI2UI2);
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::SC2, image::SC2, itkSigmoidImageFilterSC2SC2);
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::SS2, image::SS2, itkSigmoidImageFilterSS2SS2);
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::SI2, image::SI2, itkSigmoidImageFilterSI2SI2);

    //===========3D Wrapped Filters==============
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::F3 , image::F3 , itkSigmoidImageFilterF3F3  );
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::D3 , image::D3 , itkSigmoidImageFilterD3D3  );
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::UC3, image::UC3, itkSigmoidImageFilterUC3UC3);
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::US3, image::US3, itkSigmoidImageFilterUS3US3);
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::UI3, image::UI3, itkSigmoidImageFilterUI3UI3);
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::SC3, image::SC3, itkSigmoidImageFilterSC3SC3);
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::SS3, image::SS3, itkSigmoidImageFilterSS3SS3);
    ITK_WRAP_OBJECT2(SigmoidImageFilter, image::SI3, image::SI3, itkSigmoidImageFilterSI3SI3);
  }
}


#endif
