# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkXMLPDataSetWriter(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkXMLPDataSetWriter(), 'Writing vtkXMLPDataSet.',
            ('vtkXMLPDataSet',), (),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)