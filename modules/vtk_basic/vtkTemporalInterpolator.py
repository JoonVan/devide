# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkTemporalInterpolator(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkTemporalInterpolator(), 'Processing.',
            ('vtkTemporalDataSet',), ('vtkTemporalDataSet',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)