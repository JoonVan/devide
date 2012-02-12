#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.3 on Wed Apr 30 23:31:54 2008

import wx

# begin wxGlade: extracode
# end wxGlade



class DICOMReaderViewFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: DICOMReaderViewFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.view_frame_panel = wx.Panel(self, -1)
        self.sizer_4_staticbox = wx.StaticBox(self.view_frame_panel, -1, "DICOM Files")
        self.dicom_files_lb = wx.ListBox(self.view_frame_panel, -1, choices=[], style=wx.LB_EXTENDED|wx.LB_HSCROLL|wx.LB_NEEDED_SB)
        self.remove_files_b = wx.Button(self.view_frame_panel, -1, "Remove files")
        self.add_files_b = wx.Button(self.view_frame_panel, -1, "Add files")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: DICOMReaderViewFrame.__set_properties
        self.SetTitle("frame_1")
        self.dicom_files_lb.SetMinSize((400,300))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: DICOMReaderViewFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.StaticBoxSizer(self.sizer_4_staticbox, wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.dicom_files_lb, 1, wx.ALL|wx.EXPAND, 7)
        sizer_5.Add(self.remove_files_b, 0, wx.RIGHT, 4)
        sizer_5.Add(self.add_files_b, 0, 0, 0)
        sizer_4.Add(sizer_5, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.ALIGN_RIGHT, 7)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.ALL|wx.EXPAND, 7)
        self.view_frame_panel.SetSizer(sizer_2)
        sizer_1.Add(self.view_frame_panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class DICOMReaderViewFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = DICOMReaderViewFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
