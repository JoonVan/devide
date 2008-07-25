from module_base import ModuleBase
from moduleMixins import scriptedConfigModuleMixin
import moduleUtils
import vtk

class wsMeshSmooth(scriptedConfigModuleMixin, ModuleBase):
    def __init__(self, moduleManager):
        # initialise our base class
        ModuleBase.__init__(self, moduleManager)
        

        self._wsPDFilter = vtk.vtkWindowedSincPolyDataFilter()

        moduleUtils.setupVTKObjectProgress(self, self._wsPDFilter,
                                           'Smoothing polydata')
        

        # setup some defaults
        self._config.numberOfIterations = 20
        self._config.passBand = 0.1
        self._config.featureEdgeSmoothing = False
        self._config.boundarySmoothing = True

        config_list = [
            ('Number of iterations', 'numberOfIterations', 'base:int', 'text',
             'Algorithm will stop after this many iterations.'),
            ('Pass band (0 - 2, default 0.1)', 'passBand', 'base:float',
             'text', 'Indication of frequency cut-off, the lower, the more '
             'it smoothes.'),
            ('Feature edge smoothing', 'featureEdgeSmoothing', 'base:bool',
             'checkbox', 'Smooth feature edges (large dihedral angle)'),
            ('Boundary smoothing', 'boundarySmoothing', 'base:bool',
             'checkbox', 'Smooth boundary edges (edges with only one face).')]

        scriptedConfigModuleMixin.__init__(
            self, config_list,
            {'Module (self)' : self,
             'vtkWindowedSincPolyDataFilter' : self._wsPDFilter})
   
        self.sync_module_logic_with_config()

    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        for inputIdx in range(len(self.get_input_descriptions())):
            self.set_input(inputIdx, None)

        # this will take care of all display thingies
        scriptedConfigModuleMixin.close(self)

        ModuleBase.close(self)
            
        # get rid of our reference
        del self._wsPDFilter

    def get_input_descriptions(self):
        return ('vtkPolyData',)

    def set_input(self, idx, inputStream):
        self._wsPDFilter.SetInput(inputStream)

    def get_output_descriptions(self):
        return (self._wsPDFilter.GetOutput().GetClassName(), )

    def get_output(self, idx):
        return self._wsPDFilter.GetOutput()

    def logic_to_config(self):
        self._config.numberOfIterations = self._wsPDFilter.\
                                          GetNumberOfIterations()
        self._config.passBand = self._wsPDFilter.GetPassBand()
        self._config.featureEdgeSmoothing = bool(
            self._wsPDFilter.GetFeatureEdgeSmoothing())
        self._config.boundarySmoothing = bool(
            self._wsPDFilter.GetBoundarySmoothing())

    def config_to_logic(self):
        self._wsPDFilter.SetNumberOfIterations(self._config.numberOfIterations)
        self._wsPDFilter.SetPassBand(self._config.passBand)
        self._wsPDFilter.SetFeatureEdgeSmoothing(
            self._config.featureEdgeSmoothing)
        self._wsPDFilter.SetBoundarySmoothing(
            self._config.boundarySmoothing)


    def execute_module(self):
        self._wsPDFilter.Update()

    # no streaming yet :) (underlying filter works with 2 streaming 
    # pieces, no other settings)


        

