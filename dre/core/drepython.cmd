@echo off

@rem This script can be used as a DRE-enabled Python interpreter on Windows,
@rem for example to configure in Eclipse when you need to develop Python code
@rem that needs the DRE (or DeVIDE) to run.

@rem this script lives in the top-level DRE directory, i.e. the 'inst'
@rem directory of the johannes build tree.

"%~dp0\dre.cmd" python %1 %2 %3 %4 %5 %6 %7 %8 %9
