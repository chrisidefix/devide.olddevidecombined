/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_ITKSimilarityTransforms.cxx,v $
  Language:  C++
  Date:      $Date: 2004/12/03 23:50:14 $
  Version:   $Revision: 1.1 $

  Copyright (c) Insight Software Consortium. All rights reserved.
  See ITKCopyright.txt or http://www.itk.org/HTML/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even 
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/
#include "itkSimilarity2DTransform.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"

#define ITK_WRAP_TRANSFORM_1(x) \
  ITK_WRAP_OBJECT1(x, double, itk##x)
    
namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(ITKSimilarityTransforms);
  namespace wrappers
  {
    ITK_WRAP_TRANSFORM_1(Similarity2DTransform);
  }
}
#endif
