/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_itkFixedArray.cxx,v $
  Language:  C++
  Date:      $Date: 2004/12/03 23:50:14 $
  Version:   $Revision: 1.1 $

  Copyright (c) Insight Software Consortium. All rights reserved.
  See ITKCopyright.txt or http://www.itk.org/HTML/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even 
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/
#include "itkFixedArray.h"

#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
namespace _cable_
{
  const char* const group = ITK_WRAP_GROUP(itkFixedArray);
  namespace wrappers
  {
    typedef itk::FixedArray<double, 2 >::FixedArray itkFixedArrayD2;
    typedef itk::FixedArray<double, 3 >::FixedArray itkFixedArrayD3;
    typedef itk::FixedArray<unsigned int, 2 >::FixedArray itkFixedArrayUI2;
    typedef itk::FixedArray<unsigned int, 3 >::FixedArray itkFixedArrayUI3;
  }
}
#endif
