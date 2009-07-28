@echo off

@rem this script will invoke the DRE Python driver script (dre.py) with
@rem the locally-built Python interpreter.  Each platform supported by
@rem the DRE (at the moment Windows and Linux) has a small command
@rem interpreter / shell script to bootstrap the main DRE driver, which
@rem does all the work.

@rem this script lives in the top-level DRE directory, i.e. the 'inst'
@rem directory of the johannes build tree.

%~dp0\python\python.exe %~dp0\dre.py %1 %2 %3 %4 %5 %6 %7 %8 %9

