/*=========================================================================

  Program:   Insight Segmentation & Registration Toolkit
  Module:    $RCSfile: wrap_ITKCommon.cxx,v $
  Language:  C++
  Date:      $Date: 2004/12/03 23:50:14 $
  Version:   $Revision: 1.1 $

  Copyright (c) Insight Software Consortium. All rights reserved.
  See ITKCopyright.txt or http://www.itk.org/HTML/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even 
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/
#ifdef CABLE_CONFIGURATION
#include "itkCSwigMacros.h"
namespace _cable_
{
  const char* const package = ITK_WRAP_PACKAGE_NAME(ITK_WRAP_PACKAGE);
  const char* const groups[] =
  {
    ITK_WRAP_GROUP(ITKCommonBase),
    ITK_WRAP_GROUP(ITKInterpolators),
    ITK_WRAP_GROUP(ITKKernelDeformableTransforms),
    ITK_WRAP_GROUP(ITKRegions),
    ITK_WRAP_GROUP(ITKRigidTransforms),
    ITK_WRAP_GROUP(ITKSimilarityTransforms),
    ITK_WRAP_GROUP(itkAffineTransform),
    ITK_WRAP_GROUP(itkArray),
    ITK_WRAP_GROUP(itkAzimuthElevationToCartesianTransform),
    ITK_WRAP_GROUP(itkBSplineDeformableTransform),
    ITK_WRAP_GROUP(itkBinaryBallStructuringElement),
    ITK_WRAP_GROUP(itkContinuousIndex),
    ITK_WRAP_GROUP(itkDifferenceImageFilter),
    ITK_WRAP_GROUP(itkDenseFiniteDifferenceImageFilter),
    ITK_WRAP_GROUP(itkEventObjectGroup),
    ITK_WRAP_GROUP(itkFiniteDifferenceImageFilter),
    ITK_WRAP_GROUP(itkFixedArray),
    ITK_WRAP_GROUP(itkFunctionBase),
    ITK_WRAP_GROUP(itkIdentityTransform),
    ITK_WRAP_GROUP(itkImage_2D),
    ITK_WRAP_GROUP(itkImage_3D),
    ITK_WRAP_GROUP(itkImageSource),
    ITK_WRAP_GROUP(itkImageConstIterator),
    ITK_WRAP_GROUP(itkImageRegionIterator),
    ITK_WRAP_GROUP(itkImageRegionConstIterator),
    ITK_WRAP_GROUP(itkImageFunction),
    ITK_WRAP_GROUP(itkImageToImageFilter_2D),
    ITK_WRAP_GROUP(itkImageToImageFilter_3D),
    ITK_WRAP_GROUP(itkInPlaceImageFilter),
    ITK_WRAP_GROUP(itkIndex),
    ITK_WRAP_GROUP(itkLevelSet),
    ITK_WRAP_GROUP(itkNeighborhood),
    ITK_WRAP_GROUP(itkPoint),
    ITK_WRAP_GROUP(itkSize),
    ITK_WRAP_GROUP(itkScaleTransform),
    ITK_WRAP_GROUP(itkTranslationTransform),
    ITK_WRAP_GROUP(itkTransform),
#ifdef ITK_TCL_WRAP
    ITK_WRAP_GROUP(ITKUtils),
#endif
#ifdef ITK_PYTHON_WRAP
    ITK_WRAP_GROUP(ITKPyUtils),
#ifdef ITK_PYTHON_NUMERICS
    ITK_WRAP_GROUP(itkPyBuffer),
#endif
#endif
    "SwigExtras",
    ITK_WRAP_GROUP(itkVector),
    ITK_WRAP_GROUP(itkVersorTransformGroup)
  };
}
#endif
