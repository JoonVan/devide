# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkSLCReader(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkSLCReader(), 'Reading vtkSLC.',
            (), ('vtkSLC',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)