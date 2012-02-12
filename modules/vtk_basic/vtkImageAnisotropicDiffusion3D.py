# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkImageAnisotropicDiffusion3D(SimpleVTKClassModuleBase):
    def __init__(self, module_manager):
        SimpleVTKClassModuleBase.__init__(
            self, module_manager,
            vtk.vtkImageAnisotropicDiffusion3D(), 'Processing.',
            ('vtkImageData',), ('vtkImageData',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
