/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_itkNormalizeImageFilter.cxx,v $
  Language:  C++
  Date:      $Date: 2004/12/04 00:39:58 $
  Version:   $Revision: 1.2 $

  Copyright (c) Insight Software Consortium. All rights reserved.
  See ITKCopyright.txt or http://www.itk.org/HTML/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even 
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/
#include "itkImage.h"
#include "itkNormalizeImageFilter.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
#include "itkCSwigImages.h"

namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkNormalizeImageFilter);
  namespace wrappers
  {
    ITK_WRAP_OBJECT2(NormalizeImageFilter,  image::F2,  image::F2,   itkNormalizeImageFilterF2F2);
    ITK_WRAP_OBJECT2(NormalizeImageFilter, image::SS2, image::SS2, itkNormalizeImageFilterSS2SS2);

    ITK_WRAP_OBJECT2(NormalizeImageFilter,  image::F3,  image::F3,   itkNormalizeImageFilterF3F3);
    ITK_WRAP_OBJECT2(NormalizeImageFilter, image::SS3, image::SS3, itkNormalizeImageFilterSS3SS3);
  }
}


#endif
