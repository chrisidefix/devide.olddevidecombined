/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_itkImageSource.cxx,v $
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
#include "itkImageToImageFilter.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigImages.h"
#include "itkCSwigMacros.h"

namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkImageSource);
  namespace wrappers
  {
    ITK_WRAP_OBJECT1(ImageSource, image::F2 , itkImageSourceF2 );
    ITK_WRAP_OBJECT1(ImageSource, image::VF2 , itkImageSourceVF2 );

    ITK_WRAP_OBJECT1(ImageSource, image::F3 , itkImageSourceF3 );
    ITK_WRAP_OBJECT1(ImageSource, image::VF3 , itkImageSourceVF3 );
  }
}
#endif
