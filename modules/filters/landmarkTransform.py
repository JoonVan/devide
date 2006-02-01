# landmarkTransform.py copyright (c) 2003 by Charl P. Botha <cpbotha@ieee.org>
# $Id$
# see module documentation

# TODO:
# * make mode configurable by the user

import genUtils
from moduleBase import moduleBase
from moduleMixins import scriptedConfigModuleMixin
import moduleUtils
import wx
import vtk

class landmarkTransform(scriptedConfigModuleMixin, moduleBase):
    """The landmarkTransform will calculate a 4x4 linear transform that maps
    from a set of source landmarks to a set of target landmarks.

    The mapping is optimised with a least-squares metric.  You have to supply
    two sets of points, all points names in the source set have to start with
    'Source' and all the points names in the target set have to start with
    'Target'.

    This module will supply a vtkTransform at its output.  By
    connecting the vtkTransform to a transformPolyData module, you'll
    be able to perform the actual transformation.
    """

    def __init__(self, moduleManager):
        moduleBase.__init__(self, moduleManager)

        self._inputPoints = None
        self._sourceLandmarks = None
        self._targetLandmarks = None

        self._config.mode = 'Rigid'

        configList = [('Transformation mode:', 'mode', 'base:str', 'choice',
                       'Rigid: rotation + translation;\n'
                       'Similarity: rigid + isotropic scaling\n'
                       'Affine: rigid + scaling + shear',
                       ('Rigid', 'Similarity', 'Affine'))]

        scriptedConfigModuleMixin.__init__(self, configList)

        self._landmarkTransform = vtk.vtkLandmarkTransform()

        self._createWindow(
            {'Module (self)' : self,
             'vtkLandmarkTransform': self._landmarkTransform})

        self.configToLogic()
        self.logicToConfig()
        self.configToView()

    def close(self):
        # we play it safe... (the graph_editor/module_manager should have
        # disconnected us by now)
        for inputIdx in range(len(self.getInputDescriptions())):
            self.setInput(inputIdx, None)

        # this will take care of all display thingies
        scriptedConfigModuleMixin.close(self)
        
        # get rid of our reference
        del self._landmarkTransform

    def getInputDescriptions(self):
        return ('Source and Target Points',)

    def setInput(self, idx, inputStream):
        if inputStream is not self._inputPoints:

            if inputStream == None:
                # disconnect
                if self._inputPoints:
                    self._inputPoints.removeObserver(
                        self._observerInputPoints)
                    
                self._inputPoints = None

            elif hasattr(inputStream, 'devideType') and \
                 inputStream.devideType == 'namedPoints':
                # correct type... first disconnect the old
                if self._inputPoints:
                    self._inputPoints.removeObserver(
                        self._observerInputPoints)

                self._inputPoints = inputStream
                self._inputPoints.addObserver(self._observerInputPoints)

                # initial update
                self._observerInputPoints(None)

            else:
                raise TypeError, 'This input requires a named points type.'

    def getOutputDescriptions(self):
        return ('vtkTransform',)

    def getOutput(self, idx):
            return self._landmarkTransform

    def logicToConfig(self):
        mas = self._landmarkTransform.GetModeAsString()
        if mas == 'RigidBody':
            mas = 'Rigid'
        self._config.mode = mas
    
    def configToLogic(self):
        if self._config.mode == 'Rigid':
            self._landmarkTransform.SetModeToRigidBody()
        elif self._config.mode == 'Similarity':
            self._landmarkTransform.SetModeToSimilarity()
        else:
            self._landmarkTransform.SetModeToAffine()
    
    def executeModule(self):
        self._landmarkTransform.Update()

    def view(self, parent_window=None):
        # if the window was visible already. just raise it
        self._viewFrame.Show(True)
        self._viewFrame.Raise()

    def _observerInputPoints(self, obj):
        # the points have changed, let's see if they really have

        if not self._inputPoints:
            return
        
        tempSourceLandmarks = [i['world'] for i in self._inputPoints
                               if i['name'].lower().startswith('source')]
        tempTargetLandmarks = [i['world'] for i in self._inputPoints
                               if i['name'].lower().startswith('target')]

        print "hi there"
        
        if tempSourceLandmarks != self._sourceLandmarks or \
           tempTargetLandmarks != self._targetLandmarks:

            print "seems like I have to update"

            if len(tempSourceLandmarks) != len(tempTargetLandmarks):
                md= wx.MessageDialog(
                    self._moduleManager.getModuleViewParentWindow(),
                    "landmarkTransform: Your 'Source' landmark set and "
                    "'Target' landmark set should be of equal size.",
                    "Landmark Set Size",
                    wx.ICON_INFORMATION | wx.OK)
                
                md.ShowModal()

            else:
                self._sourceLandmarks = tempSourceLandmarks
                self._targetLandmarks = tempTargetLandmarks

                sourceLandmarks = vtk.vtkPoints()
                targetLandmarks = vtk.vtkPoints()
                landmarkPairs = ((self._sourceLandmarks, sourceLandmarks),
                                 (self._targetLandmarks, targetLandmarks))
                
                for lmp in landmarkPairs:
                    lmp[1].SetNumberOfPoints(len(lmp[0]))
                    for pointIdx in range(len(lmp[0])):
                        lmp[1].SetPoint(pointIdx, lmp[0][pointIdx])
                                 
                self._landmarkTransform.SetSourceLandmarks(sourceLandmarks)
                self._landmarkTransform.SetTargetLandmarks(targetLandmarks)
                
        
        