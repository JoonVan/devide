# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from moduleMixins import simpleVTKClassModuleBase
import vtk

class vtkGenericEnSightReader(simpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        simpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkGenericEnSightReader(), 'Reading vtkGenericEnSight.',
            (), ('vtkGenericEnSight',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)