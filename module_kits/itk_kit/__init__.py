# Copyright (c) Charl P. Botha, TU Delft.
# All rights reserved.
# See COPYRIGHT for details.

"""itk_kit package driver file.

Inserts the following modules in sys.modules: itk, InsightToolkit.

@author: Charl P. Botha <http://cpbotha.net/>
"""

import os
import re
import sys

VERSION = ''

def setDLFlags():
    # brought over from ITK Wrapping/CSwig/Python

    # Python "help(sys.setdlopenflags)" states:
    #
    # setdlopenflags(...)
    #     setdlopenflags(n) -> None
    #     
    #     Set the flags that will be used for dlopen() calls. Among other
    #     things, this will enable a lazy resolving of symbols when
    #     importing a module, if called as sys.setdlopenflags(0) To share
    #     symbols across extension modules, call as
    #
    #     sys.setdlopenflags(dl.RTLD_NOW|dl.RTLD_GLOBAL)
    #
    # GCC 3.x depends on proper merging of symbols for RTTI:
    #   http://gcc.gnu.org/faq.html#dso
    #
    try:
        import dl
        newflags = dl.RTLD_NOW|dl.RTLD_GLOBAL
    except:
        newflags = 0x102  # No dl module, so guess (see above).
        
    try:
        oldflags = sys.getdlopenflags()
        sys.setdlopenflags(newflags)
    except:
        oldflags = None

    return oldflags

def resetDLFlags(data):
    # brought over from ITK Wrapping/CSwig/Python    
    # Restore the original dlopen flags.
    try:
        sys.setdlopenflags(data)
    except:
        pass

def init(theModuleManager, pre_import=True):

    if hasattr(sys, 'frozen') and sys.frozen:
        # if we're frozen, make sure we grab the wrapitk contained in this kit
        p1 = os.path.dirname(__file__)
        p2 = os.path.join(p1, os.path.join('wrapitk', 'python'))
        p3 = os.path.join(p1, os.path.join('wrapitk', 'lib'))
        sys.path.insert(0, p2)
        sys.path.insert(0, p3)

        # and now the LD_LIBRARY_PATH / PATH
        if sys.platform == 'win32':
            so_path_key = 'PATH'

        else:
            so_path_key = 'LD_LIBRARY_PATH'

        # this doesn't work on Linux in anycase
        if so_path_key in os.environ:
            os.environ[so_path_key] = '%s%s%s' % \
                                      (p3, os.pathsep, os.environ[so_path_key])
        else:
            os.environ[so_path_key] = p3


    # with WrapITK, this takes almost no time
    import itk

    theModuleManager.setProgress(5, 'Initialising ITK: start')

    # let's get the version (which will bring in VXLNumerics and Base)

    # setup the kit version
    global VERSION
    isv = itk.Version.GetITKSourceVersion()
    ind = re.match('.*Date: ([0-9]+-[0-9]+-[0-9]+).*', isv).group(1)
    VERSION = '%s (%s)' % (itk.Version.GetITKVersion(), ind)

    theModuleManager.setProgress(45, 'Initialising ITK: VXLNumerics, Base')

    if pre_import:
        # then ItkVtkGlue (at the moment this is fine, VTK is always there;
        # keep in mind for later when we allow VTK-less startups)
        a = itk.VTKImageToImageFilter

        theModuleManager.setProgress(
            75,
            'Initialising ITK: BaseTransforms, SimpleFilters, ItkVtkGlue')
    
    # user can address this as module_kits.itk_kit.utils.blaat()
    import module_kits.itk_kit.utils as utils

    theModuleManager.setProgress(100, 'Initialising ITK: DONE')


