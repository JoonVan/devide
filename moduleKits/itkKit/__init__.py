# $Id: __init__.py,v 1.3 2005/11/24 13:12:31 cpbotha Exp $

"""itkKit package driver file.

Inserts the following modules in sys.modules: itk, InsightToolkit.

@author: Charl P. Botha <http://cpbotha.net/>
"""

import re
import sys

VERSION = ''
ITK_VERSION_EXTRA = 'update -dAP'

def preImportITK(progressMethod):
    itkImportList = [('VXLNumericsPython', 'VXL Numerics'),
                     ('ITKCommonAPython', 'ITK Common part A'),
                     ('ITKCommonBPython', 'ITK Common part B'),
                     ('ITKBasicFiltersAPython', 'ITK Basic Filters A'),
                     ('ITKBasicFiltersBPython', 'ITK Basic Filters B'),
                     ('ITKNumericsPython', 'ITK Numerics'),
                     ('ITKAlgorithmsPython', 'ITK Algorithms'),
                     ('ITKIOPython', 'ITK IO Python'),
                     ('InsightToolkit', 'Other ITK symbols')] # fixitk
    

    # set the dynamic loading flags.  If we don't do this, we get strange
    # errors on 64 bit machines.  To see this happen, comment this statement
    # and then run the VTK->ITK connection test case.
    oldflags = setDLFlags()

    percentStep = 100.0 / len(itkImportList)
    currentPercent = 0.0

    # do the imports
    for module, message in itkImportList:
        currentPercent += percentStep
        progressMethod(currentPercent, 'Initialising itkKit: %s' % (message,),
                       noTime=True)
        exec('import %s' % (module,))

    # restore previous dynamic loading flags
    resetDLFlags(oldflags)

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

def init(theModuleManager):
    # first do the VTK pre-imports: this is here ONLY to keep the user happy
    # it's not necessary for normal functioning
    preImportITK(theModuleManager.setProgress)

    # brings 'InsightToolkit' into sys.modules
    import InsightToolkit as itk
    # stuff itk in there as well
    sys.modules['itk'] = itk

    import moduleUtils

    # setup the kit version
    global VERSION

    # let's hope McMillan doesn't catch this one!
    isv = itk.itkVersion.GetITKSourceVersion()
    ind = re.match('.*Date: ([0-9]+/[0-9]+/[0-9]+).*', isv).group(1)
    VERSION = '%s (%s: %s)' % (itk.itkVersion.GetITKVersion(), ind,
                               ITK_VERSION_EXTRA)