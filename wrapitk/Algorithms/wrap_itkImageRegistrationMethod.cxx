/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_itkImageRegistrationMethod.cxx,v $
  Language:  C++
  Date:      $Date: 2005/01/05 15:41:45 $
  Version:   $Revision: 1.2 $

  Copyright (c) Insight Software Consortium. All rights reserved.
  See ITKCopyright.txt or http://www.itk.org/HTML/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even 
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/
#include "itkImage.h"
#include "itkImageRegistrationMethod.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
#include "itkCSwigImages.h"

namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkImageRegistrationMethod);
  namespace wrappers
  {
    ITK_WRAP_OBJECT2(ImageRegistrationMethod, image::F2, image::F2,
                     itkImageRegistrationMethodF2F2);
    ITK_WRAP_OBJECT2(ImageRegistrationMethod, image::F3, image::F3,
                     itkImageRegistrationMethodF3F3);

  }
}

#endif
