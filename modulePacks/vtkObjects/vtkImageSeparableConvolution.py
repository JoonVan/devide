# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkImageSeparableConvolution(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkImageSeparableConvolution(), 'Processing.',
            ('vtkImageData',), ('vtkImageData',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)