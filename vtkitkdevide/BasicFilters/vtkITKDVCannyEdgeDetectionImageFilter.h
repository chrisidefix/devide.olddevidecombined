/*=========================================================================

  Program:   Visualization Toolkit
  Module:    $RCSfile: vtkITKDVCannyEdgeDetectionImageFilter.h,v $
  Language:  C++
  Date:      $Date: 2004/10/22 15:01:11 $
  Version:   $Revision: 1.1 $
*/
// .NAME vtkITKDVCannyEdgeDetectionImageFilter - Wrapper class around itk::GrayscaleFillholeImageFilterImageFilter
// .SECTION Description
// vtkITKDVCannyEdgeDetectionImageFilter


#ifndef __vtkITKDVCannyEdgeDetectionImageFilter_h
#define __vtkITKDVCannyEdgeDetectionImageFilter_h

#include "vtkITKDVImageToImageFilterFF.h"
#include "itkCannyEdgeDetectionImageFilter.h"
#include "vtkObjectFactory.h"

class VTK_EXPORT vtkITKDVCannyEdgeDetectionImageFilter : public vtkITKDVImageToImageFilterFF
{
 public:
  static vtkITKDVCannyEdgeDetectionImageFilter *New();
  vtkTypeRevisionMacro(vtkITKDVCannyEdgeDetectionImageFilter, vtkITKDVImageToImageFilterFF);


  // THRESHOLD
  void SetThreshold(Superclass::OutputImageType d)
  {
    DelegateSetMacro(Threshold, d);
  }

  Superclass::OutputImageType GetThreshold(void)
  {
    DelegateGetMacro(Threshold);
  }

  // OUTSIDEVALUE
  void SetOutsideValue(Superclass::OutputImageType d)
  {
    DelegateSetMacro(OutsideValue, d);
  }

  Superclass::OutputImageType GetOutsideValue(void)
  {
    DelegateGetMacro(OutsideValue);
  }

  // VARIANCE
  void SetVariance ( double v1, double v2, double v3)
  {
    double v[3];
    v[0] = v1; v[1] = v2; v[2] = v3;
    this->GetImageFilterPointer()->SetVariance (v);
  }

  

  // MAXIMUMERROR
  void SetMaximumError (double e1, double e2, double e3)
  {
    double e[3];
    e[0] = e1; e[1] = e2; e[2] = e3;
    this->GetImageFilterPointer()->SetMaximumError (e);
  }

protected:
  //BTX
  typedef itk::CannyEdgeDetectionImageFilter<Superclass::InputImageType,Superclass::OutputImageType> ImageFilterType;
  vtkITKDVCannyEdgeDetectionImageFilter() : Superclass ( ImageFilterType::New() ){};
  ~vtkITKDVCannyEdgeDetectionImageFilter() {};
  ImageFilterType* GetImageFilterPointer() { return dynamic_cast<ImageFilterType*> ( m_Filter.GetPointer() ); }

  //ETX
  
private:
  vtkITKDVCannyEdgeDetectionImageFilter(const vtkITKDVCannyEdgeDetectionImageFilter&);  // Not implemented.
  void operator=(const vtkITKDVCannyEdgeDetectionImageFilter&);  // Not implemented.
};

vtkCxxRevisionMacro(vtkITKDVCannyEdgeDetectionImageFilter, "$Revision: 1.1 $");
vtkStandardNewMacro(vtkITKDVCannyEdgeDetectionImageFilter);

#endif




