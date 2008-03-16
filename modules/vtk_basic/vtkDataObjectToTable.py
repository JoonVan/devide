# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkDataObjectToTable(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkDataObjectToTable(), 'Processing.',
            ('vtkDataObject',), ('vtkTable',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)