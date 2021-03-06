#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.3 on Wed Jan 06 13:04:15 2010

import wx

# begin wxGlade: extracode
# end wxGlade



class MaskComBinarMenu(wx.MenuBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MaskComBinarMenu.__init__
        wx.MenuBar.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MaskComBinarMenu.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MaskComBinarMenu.__do_layout
        pass
        # end wxGlade

# end of class MaskComBinarMenu


class MaskOperationsFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MaskOperationsFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.mask_operations_panel = wx.Panel(self, -1)
        self.sizer_metrics_staticbox = wx.StaticBox(self.mask_operations_panel, -1, "Measurements / Metrics")
        self.sizer_diagnostics_staticbox = wx.StaticBox(self.mask_operations_panel, -1, "Diagnostics")
        self.sizer_operations_staticbox = wx.StaticBox(self.mask_operations_panel, -1, "Mask operations")
        self.add_button = wx.Button(self.mask_operations_panel, -1, u"A \u222A B")
        self.subtract_button = wx.Button(self.mask_operations_panel, -1, "A \ B")
        self.and_button = wx.Button(self.mask_operations_panel, -1, u"A \u2229 B")
        self.align_metadata_button = wx.Button(self.mask_operations_panel, -1, "Copy metadata A => B")
        self.align_icp_button = wx.Button(self.mask_operations_panel, -1, "Align B with A (ICP)")
        self.split_disconnected_button = wx.Button(self.mask_operations_panel, -1, "Split A into disconnected parts")
        self.volume_button = wx.Button(self.mask_operations_panel, -1, "Volume A")
        self.dice_button = wx.Button(self.mask_operations_panel, -1, "Dice Coefficient")
        self.hausdorff_button = wx.Button(self.mask_operations_panel, -1, "Hausdorff")
        self.mean_hausdorff_button = wx.Button(self.mask_operations_panel, -1, "Mean Hausdorff")
        self.check_selected_overlaps_button = wx.Button(self.mask_operations_panel, -1, "Check Overlap")
        self.check_all_overlaps_button = wx.Button(self.mask_operations_panel, -1, "Check All Overlaps")
        self.check_selected_dimensions_button = wx.Button(self.mask_operations_panel, -1, "Check Dimensions")
        self.check_all_dimensions_button = wx.Button(self.mask_operations_panel, -1, "Check All Dimensions")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MaskOperationsFrame.__set_properties
        self.SetTitle("Mask Operations")
        self.add_button.SetToolTipString("Union of (adds) selected masks")
        self.subtract_button.SetToolTipString("Subtracts selected masks in B from A")
        self.and_button.SetToolTipString("Intersection of (logical AND) selected masks in A with those in B")
        self.align_metadata_button.SetToolTipString("Copies position, extent, spacing, etc. from A to B")
        self.align_icp_button.SetToolTipString("Uses the Iterative Closest Point algorithm to align B with A")
        self.split_disconnected_button.SetToolTipString("Splits disconnected parts of the selected mask(s) in A")
        self.volume_button.SetToolTipString("Computes the volume of selected masks in A (blue)")
        self.dice_button.SetToolTipString("Computes the Dice Coefficient between A and B")
        self.hausdorff_button.SetToolTipString("Computes the Hausdorff Distance between A and B")
        self.mean_hausdorff_button.SetToolTipString("Computes the mean Hausdorff Distance between A and B")
        self.check_selected_overlaps_button.SetToolTipString("Check whether selected masks overlap")
        self.check_all_overlaps_button.SetToolTipString("Check whether any masks overlap")
        self.check_selected_dimensions_button.SetToolTipString("Check whether selected masks' metadata dimensions agree")
        self.check_all_dimensions_button.SetToolTipString("Check whether all masks' metadata dimensions agree")
        self.mask_operations_panel.SetMinSize((614, 51))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MaskOperationsFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_diagnostics = wx.StaticBoxSizer(self.sizer_diagnostics_staticbox, wx.VERTICAL)
        sizer_check_dimensions = wx.BoxSizer(wx.HORIZONTAL)
        sizer_check_overlaps = wx.BoxSizer(wx.HORIZONTAL)
        sizer_metrics = wx.StaticBoxSizer(self.sizer_metrics_staticbox, wx.HORIZONTAL)
        sizer_4_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_hausdorff = wx.BoxSizer(wx.HORIZONTAL)
        sizer_operations = wx.StaticBoxSizer(self.sizer_operations_staticbox, wx.VERTICAL)
        AddSubtractAnd_sizer = wx.BoxSizer(wx.HORIZONTAL)
        AddSubtractAnd_sizer.Add(self.add_button, 1, wx.EXPAND, 0)
        AddSubtractAnd_sizer.Add(self.subtract_button, 1, wx.EXPAND, 0)
        AddSubtractAnd_sizer.Add(self.and_button, 1, wx.EXPAND, 0)
        sizer_operations.Add(AddSubtractAnd_sizer, 0, wx.EXPAND, 0)
        sizer_operations.Add(self.align_metadata_button, 0, wx.EXPAND, 0)
        sizer_operations.Add(self.align_icp_button, 0, wx.EXPAND, 0)
        sizer_operations.Add(self.split_disconnected_button, 0, wx.EXPAND, 0)
        sizer_3.Add(sizer_operations, 0, wx.EXPAND, 0)
        sizer_4_copy.Add(self.volume_button, 1, wx.EXPAND, 0)
        sizer_4_copy.Add(self.dice_button, 1, wx.EXPAND, 0)
        sizer_hausdorff.Add(self.hausdorff_button, 1, wx.EXPAND, 0)
        sizer_hausdorff.Add(self.mean_hausdorff_button, 1, wx.EXPAND, 0)
        sizer_4_copy.Add(sizer_hausdorff, 1, wx.EXPAND, 0)
        sizer_metrics.Add(sizer_4_copy, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_metrics, 0, wx.EXPAND, 0)
        sizer_check_overlaps.Add(self.check_selected_overlaps_button, 1, wx.EXPAND, 0)
        sizer_check_overlaps.Add(self.check_all_overlaps_button, 1, wx.EXPAND, 0)
        sizer_diagnostics.Add(sizer_check_overlaps, 1, wx.EXPAND, 0)
        sizer_check_dimensions.Add(self.check_selected_dimensions_button, 1, wx.EXPAND, 0)
        sizer_check_dimensions.Add(self.check_all_dimensions_button, 1, wx.EXPAND, 0)
        sizer_diagnostics.Add(sizer_check_dimensions, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_diagnostics, 0, wx.EXPAND, 0)
        self.mask_operations_panel.SetSizer(sizer_3)
        sizer_1.Add(self.mask_operations_panel, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MaskOperationsFrame


class MaskListsFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MaskListsFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.mask_lists_panel = wx.Panel(self, -1)
        self.sizer_5_staticbox = wx.StaticBox(self.mask_lists_panel, -1, "Mask A, Mask B")
        self.list_ctrl_maskA = wx.ListCtrl(self.mask_lists_panel, -1, style=wx.LC_LIST|wx.LC_NO_HEADER|wx.SUNKEN_BORDER)
        self.list_ctrl_maskB = wx.ListCtrl(self.mask_lists_panel, -1, style=wx.LC_LIST|wx.LC_NO_HEADER|wx.SUNKEN_BORDER)
        self.button_clear_selection = wx.Button(self.mask_lists_panel, -1, "Clear Selection")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MaskListsFrame.__set_properties
        self.SetTitle("Mask A, Mask B")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MaskListsFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(self.list_ctrl_maskA, 1, wx.EXPAND, 0)
        sizer_6.Add(self.list_ctrl_maskB, 1, wx.EXPAND, 0)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_5.Add(self.button_clear_selection, 0, wx.EXPAND, 0)
        self.mask_lists_panel.SetSizer(sizer_5)
        sizer_2.Add(self.mask_lists_panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MaskListsFrame


class MaskComBinarPanels(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        mask_lists_frame = MaskListsFrame(None, -1, "")
        self.SetTopWindow(mask_lists_frame)
        mask_lists_frame.Show()
        return 1

# end of class MaskComBinarPanels

if __name__ == "__main__":
    MaskComBinarPanels = MaskComBinarPanels(0)
    MaskComBinarPanels.MainLoop()
