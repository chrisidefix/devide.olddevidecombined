/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_itkVoronoiSegmentationImageFilter.cxx,v $
  Language:  C++
  Date:      $Date: 2004/12/03 23:50:14 $
  Version:   $Revision: 1.1 $

  Copyright (c) Insight Software Consortium. All rights reserved.
  See ITKCopyright.txt or http://www.itk.org/HTML/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even 
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/
#include "itkImage.h"
#include "itkVoronoiSegmentationImageFilter.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
#include "itkCSwigImages.h"

namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkVoronoiSegmentationImageFilter);
  namespace wrappers
  {
    ITK_WRAP_OBJECT3(VoronoiSegmentationImageFilter, image::UC2, image::UC2, image::UC2,
                     itkVoronoiSegmentationImageFilterUC2UC2UC2);
  }
}

#endif
