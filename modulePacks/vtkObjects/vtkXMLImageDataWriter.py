# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkXMLImageDataWriter(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkXMLImageDataWriter(), 'Writing vtkXMLImageData.',
            ('vtkXMLImageData',), (),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)