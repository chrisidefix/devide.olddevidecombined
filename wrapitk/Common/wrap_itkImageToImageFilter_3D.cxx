/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_itkImageToImageFilter_3D.cxx,v $
  Language:  C++
  Date:      $Date: 2004/12/05 00:17:02 $
  Version:   $Revision: 1.2 $

  Copyright (c) Insight Software Consortium. All rights reserved.
  See ITKCopyright.txt or http://www.itk.org/HTML/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even 
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/
#include "itkImageToImageFilter.h"
#include "itkImage.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigImages.h"
#include "itkCSwigMacros.h"
namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkImageToImageFilter_3D);
  namespace wrappers
  {
    // to self
    ITK_WRAP_OBJECT2(ImageToImageFilter, image::F3, image::F3, itkImageToImageFilterF3F3);

    // Image to Image of vectors
    ITK_WRAP_OBJECT2(ImageToImageFilter, image::F3 , image::VF3 ,itkImageToImageFilterF3VF3 );
  }
}
#endif
