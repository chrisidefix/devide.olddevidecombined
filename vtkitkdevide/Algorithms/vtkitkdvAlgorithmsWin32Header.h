/*=========================================================================

  Program:   Visualization Toolkit
  Module:    $RCSfile: vtkitkdvAlgorithmsWin32Header.h,v $
  Language:  C++
  Date:      $Date: 2004/10/14 17:28:40 $
  Version:   $Revision: 1.1 $

  Copyright (c) 1993-2002 Ken Martin, Will Schroeder, Bill Lorensen 
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even 
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/
// .NAME vtkdevideIOWin32Header - manage Windows system differences
// .SECTION Description
// The vtkdevideIOWin32Header captures some system differences between Unix
// and Windows operating systems. 

#ifndef __vtkitkdvRenderingWin32Header_h
#define __vtkitkdvRenderingWin32Header_h

#include <vtkitkdvConfigure.h>

#if defined(WIN32) && !defined(VTKITKDV_STATIC)
#if defined(vtkitkdvRendering_EXPORTS)
#define VTKITKDV_RENDERING_EXPORT __declspec( dllexport ) 
#else
#define VTKITKDV_RENDERING_EXPORT __declspec( dllimport ) 
#endif
#else
#define VTKITKDV_RENDERING_EXPORT
#endif

#endif
