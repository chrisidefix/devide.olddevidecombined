/*=========================================================================

  Program:   Visualization Toolkit
  Module:    $RCSfile: vtkITKDVCannyEdgeDetectionImageFilter.h,v $
  Language:  C++
  Date:      $Date: 2004/10/23 21:40:18 $
  Version:   $Revision: 1.2 $
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
  void SetThreshold(double d)
  {
    DelegateSetMacro(Threshold, d);
  }

  double GetThreshold(void)
  {
    DelegateGetMacro(Threshold);
  }

  // OUTSIDEVALUE
  void SetOutsideValue(double d)
  {
    DelegateSetMacro(OutsideValue, d);
  }

  double GetOutsideValue(void)
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


  virtual void GetVariance(double &v1, double &v2, double &v3)
  {
    v1 = this->GetImageFilterPointer()->GetVariance().GetElement(0);
    v2 = this->GetImageFilterPointer()->GetVariance().GetElement(1);
    v3 = this->GetImageFilterPointer()->GetVariance().GetElement(2);
  }

  virtual void GetVariance(double v[3])
  {
    this->GetVariance(v[0], v[1], v[2]);
  }

  // VERY IMPORTANT: for VTK to wrap this correctly, there HAS to be an entry in
  // the local "hints" file specifying the number of elements in the returned array.
  // If vtkGetVectorNMacro() is used, the hint isn't necessary (N is used)
  virtual double *GetVariance()
  {
    // need to convert to ivar so we can return the pointer
    this->GetVariance(this->TempVariance);
    return this->TempVariance;
  }


  // MAXIMUMERROR
  void SetMaximumError (double e1, double e2, double e3)
  {
    double e[3];
    e[0] = e1; e[1] = e2; e[2] = e3;
    this->GetImageFilterPointer()->SetMaximumError (e);
  }

  void SetMaximumError(double e[3])
  {
    this->SetMaximumError(e[0], e[1], e[2]);
  }

  void GetMaximumError(double e[3])
  {
    for (int i = 0; i < 3; i++)
      {
      e[i] = this->GetImageFilterPointer()->GetMaximumError().GetElement(i);
      }
  }

protected:
  //BTX
  typedef itk::CannyEdgeDetectionImageFilter<Superclass::InputImageType,Superclass::OutputImageType> ImageFilterType;
  vtkITKDVCannyEdgeDetectionImageFilter() : Superclass ( ImageFilterType::New() ){};
  ~vtkITKDVCannyEdgeDetectionImageFilter() {};
  ImageFilterType* GetImageFilterPointer() { return dynamic_cast<ImageFilterType*> ( m_Filter.GetPointer() ); }
  double TempVariance[3];
  //ETX
  
private:
  vtkITKDVCannyEdgeDetectionImageFilter(const vtkITKDVCannyEdgeDetectionImageFilter&);  // Not implemented.
  void operator=(const vtkITKDVCannyEdgeDetectionImageFilter&);  // Not implemented.
};

vtkCxxRevisionMacro(vtkITKDVCannyEdgeDetectionImageFilter, "$Revision: 1.2 $");
vtkStandardNewMacro(vtkITKDVCannyEdgeDetectionImageFilter);

#endif




