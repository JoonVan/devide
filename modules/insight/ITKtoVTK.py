# $Id: ITKF3toVTK.py 2110 2006-06-22 15:11:21Z cpbotha $

import itk
import module_kits.itk_kit as itk_kit
from moduleBase import moduleBase
from moduleMixins import noConfigModuleMixin
import vtk

class ITKtoVTK(noConfigModuleMixin, moduleBase):
    """Convert ITK 3D float data to VTK.

    $Revision: 1.5 $
    """

    def __init__(self, moduleManager):
        moduleBase.__init__(self, moduleManager)
        noConfigModuleMixin.__init__(self)

        self._input = None
        self._itk2vtk = None

        self._viewFrame = self._createViewFrame(
            {'Module (self)' : self,
             'ImageToVTKImageFilter' : self._itk2vtk})

        self.configToLogic()
        self.logicToConfig()
        self.configToView()


    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        for inputIdx in range(len(self.getInputDescriptions())):
            self.setInput(inputIdx, None)

        # this will take care of all display thingies
        noConfigModuleMixin.close(self)

        moduleBase.close(self)

        del self._itk2vtk

    def executeModule(self):
        if self._input:

            try:
                shortstring = itk_kit.utils.get_img_type_and_dim_shortstring(
                    self._input)
                
            except TypeError:
                raise TypeError, 'ITKtoVTK requires an ITK image as input.'
            
            witk_template = getattr(itk, 'ImageToVTKImageFilter')
            witk_type = getattr(itk.Image, shortstring)

            try:
                self._itk2vtk = witk_template[witk_type].New()
                
            except KeyError, e:
                raise RuntimeError, 'Unable to instantiate ITK to VTK ' \
                      'converter with type %s.' % \
                      (shortstring,)
            
            else:
                self._input.UpdateOutputInformation()
                self._input.SetBufferedRegion(
                    self._input.GetLargestPossibleRegion())
                self._input.Update()

                itk_kit.utils.setupITKObjectProgress(
                    self, self._itk2vtk,
                    'ImageToVTKImageFilter',
                    'Converting ITK image to VTK image.')
                
                self._itk2vtk.SetInput(self._input)
                self._itk2vtk.Update()

    def getInputDescriptions(self):
        return ('ITK Image',)

    def setInput(self, idx, input_stream):
        self._input = input_stream

    def getOutputDescriptions(self):
        return ('VTK Image Data',)

    def getOutput(self, idx):
        if self._itk2vtk:
            return self._itk2vtk.GetOutput()
        else:
            return None

    def logicToConfig(self):
        # important so that moduleManager doesn't think our state has changed
        return False
    
    def configToLogic(self):
        # important so that moduleManager doesn't think our state has changed
        return False
    
    def viewToConfig(self):
        pass

    def configToView(self):
        pass
    


        
            