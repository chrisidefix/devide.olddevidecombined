/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_itkFiniteDifferenceImageFilter.cxx,v $
  Language:  C++
  Date:      $Date: 2004/12/05 00:17:02 $
  Version:   $Revision: 1.2 $

  Copyright (c) Insight Software Consortium. All rights reserved.
  See ITKCopyright.txt or http://www.itk.org/HTML/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even 
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/
#include "itkImage.h"
#include "itkFiniteDifferenceImageFilter.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigImages.h"
#include "itkCSwigMacros.h"

namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkFiniteDifferenceImageFilter);
  namespace wrappers
  {
    //===========2D Wrapped Filters==============
    ITK_WRAP_OBJECT2(FiniteDifferenceImageFilter, image::F2 , image::F2 , itkFiniteDifferenceImageFilterF2F2  );
    ITK_WRAP_OBJECT2(FiniteDifferenceImageFilter, image::F2 , image::VF2 ,itkFiniteDifferenceImageFilterF2VF2 );

    //===========3D Wrapped Filters==============
    ITK_WRAP_OBJECT2(FiniteDifferenceImageFilter, image::F3 , image::F3 , itkFiniteDifferenceImageFilterF3F3  );
    ITK_WRAP_OBJECT2(FiniteDifferenceImageFilter, image::F3 , image::VF3 ,itkFiniteDifferenceImageFilterF3VF3);
  }
}
#endif
