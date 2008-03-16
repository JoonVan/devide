# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkMultiBlockDataSetAlgorithm(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkMultiBlockDataSetAlgorithm(), 'Processing.',
            ('vtkMultiBlockDataSet',), ('vtkMultiBlockDataSet',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)