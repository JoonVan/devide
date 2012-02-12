# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkImageFlip(SimpleVTKClassModuleBase):
    def __init__(self, module_manager):
        SimpleVTKClassModuleBase.__init__(
            self, module_manager,
            vtk.vtkImageFlip(), 'Processing.',
            ('vtkImageData', 'vtkImageStencilData'), ('vtkImageData',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
