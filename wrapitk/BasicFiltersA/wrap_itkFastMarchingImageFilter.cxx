/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_itkFastMarchingImageFilter.cxx,v $
  Language:  C++
  Date:      $Date: 2004/12/04 00:39:56 $
  Version:   $Revision: 1.2 $

  Copyright (c) Insight Software Consortium. All rights reserved.
  See ITKCopyright.txt or http://www.itk.org/HTML/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/
#include "itkImage.h"
#include "itkFastMarchingImageFilter.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
#include "itkCSwigImages.h"

//=================================
//THIS FILE GENERATED WITH MakeConsistentWrappedClasses.sh
//=================================
namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkFastMarchingImageFilter);
  namespace wrappers
  {
    //===========2D Wrapped Filters==============
    ITK_WRAP_OBJECT2(FastMarchingImageFilter, image::F2 , image::F2 , itkFastMarchingImageFilterF2F2  );


    //===========3D Wrapped Filters==============
    ITK_WRAP_OBJECT2(FastMarchingImageFilter, image::F3 , image::F3 , itkFastMarchingImageFilterF3F3  );
  }
}
#endif
