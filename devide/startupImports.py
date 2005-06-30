# startupImports copyright (c) 2003 by Charl P. Botha http://cpbotha.net/
# $Id: startupImports.py,v 1.11 2005/06/30 17:09:52 cpbotha Exp $
# This is called early on to pre-import some of the larger required libraries
# and give progress messages whilst they are imported.

import os
import sys
import wx

# AIX apparently does not have dl?
try:
    import dl
except ImportError:
    dl = None
except SystemError:
    # this covers us on RHEL3 64 for:
    # SysError: module dl requires sizeof(int) == sizeof(long) == sizeof(char*) 
    dl = None

#import __helper

# set the dlopen flags so that VTK does not run into problems with
# shared symbols.
try:
    # only Python >= 2.2 has this functionality
    orig_dlopen_flags = sys.getdlopenflags()
except AttributeError:
    orig_dlopen_flags = None

if dl and (os.name == 'posix'):
    sys.setdlopenflags(dl.RTLD_NOW|dl.RTLD_GLOBAL)

def defaultProgressMethod(percentage, message):
    print "%s [%3.2f]" % (message, percentage)

def doImports(progressMethod, mainConfig):
    importList = [('vtk.common', 'Loading VTK Common.'),
                  ('vtk.filtering', 'Loading VTK Filtering.'),
                  ('vtk.io', 'Loading VTK IO.'),
                  ('vtk.imaging', 'Loading VTK Imaging.'),
                  ('vtk.graphics', 'Loading VTK Graphics.'),
                  ('vtk.rendering', 'Loading VTK Rendering.'),
                  ('vtk.hybrid', 'Loading VTK Hybrid.'),
                  ('vtk.patented', 'Loading VTK Patented.'),
                  # the following list represents the actual sequence
                  # with which fixitk/InsightToolkit loads the low-level libs
                  # we have to call these explicitly, because doing any
                  # imports from fixitk will import them all in one shot,
                  # thus making the user wait very long without any feedback
                  ('VXLNumericsPython', 'Loading VXL Numerics'),
                  ('ITKCommonAPython', 'Loading ITK Common part A'),
                  ('ITKCommonBPython', 'Loading ITK Common part B'),
                  ('ITKBasicFiltersAPython', 'Loading ITK Basic Filters part A'),
                  ('ITKBasicFiltersBPython', 'Loading ITK Basic Filters part B'),
                  ('ITKNumericsPython', 'Loading ITK Numerics'),
                  ('ITKAlgorithmsPython', 'Loading ITK Algorithms'),
                  ('ITKIOPython', 'Loading ITK IO Python'),
                  # we do the following just for completeness
                  ('fixitk.vxlNumericsPythonTopLevel', 'Loading VXL Numerics'),
                  ('fixitk.itkCommonPythonTopLevel', 'Loading ITK Common'),
                  ('fixitk.itkBasicFiltersPythonTopLevel',
                   'fixitk.Loading ITK BasicFilters'),
                  ('fixitk.itkNumericsPythonTopLevel', 'Loading ITK Numerics'),
                  ('fixitk.itkAlgorithmsPythonTopLevel', 'Loading ITK Algorithms'),
                  ('fixitk.itkIOPythonTopLevel', 'Loading ITK IO')]

    if not mainConfig.useInsight or not mainConfig.itkPreImport:
        # remove ITK things from importList
        importList = [i for i in importList if
                      not i[0].startswith('fixitk') and
                      not i[0].startswith('ITK') and
                      not i[0].startswith('VXL')]
                  
    percentStep = 95.0 / len(importList)
    currentPercent = 0.0

    for module, message in importList:
        currentPercent += percentStep
        progressMethod(currentPercent, message, noTime=True)
        wx.SafeYield()
        exec('import %s' % (module,))

    # just to make sure about any other symbols
    import vtk
