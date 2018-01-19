#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.7.2 on Thu Jan 18 18:46:35 2018
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainView(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainView.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_copybuttons = wx.ScrolledWindow(self, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.button_edit = wx.Button(self, wx.ID_ANY, "&Edit")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.button_edit_click, self.button_edit)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainView.__set_properties
        self.SetTitle("copyboard")
        self.SetSize((442, 398))
        self.panel_copybuttons.SetScrollRate(10, 10)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainView.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_copybuttons = wx.BoxSizer(wx.VERTICAL)
        self.panel_copybuttons.SetSizer(self.sizer_copybuttons)
        sizer_1.Add(self.panel_copybuttons, 1, wx.EXPAND, 0)
        sizer_4.Add(self.button_edit, 0, 0, 0)
        sizer_4.Add((20, 20), 0, 0, 0)
        sizer_1.Add(sizer_4, 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def button_edit_click(self, event):  # wxGlade: MainView.<event_handler>
        print "Event handler 'button_edit_click' not implemented!"
        event.Skip()

# end of class MainView

class EditView(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: EditView.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_editors = wx.ScrolledWindow(self, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.button_add = wx.Button(self, wx.ID_ANY, "&Add")
        self.button_remove = wx.Button(self, wx.ID_ANY, "&Remove")
        self.button_ok = wx.Button(self, wx.ID_ANY, "&OK")
        self.button_cancel = wx.Button(self, wx.ID_ANY, "&Cancel")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.button_add_click, self.button_add)
        self.Bind(wx.EVT_BUTTON, self.button_remove_click, self.button_remove)
        self.Bind(wx.EVT_BUTTON, self.button_ok_click, self.button_ok)
        self.Bind(wx.EVT_BUTTON, self.button_cancel_click, self.button_cancel)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: EditView.__set_properties
        self.SetTitle("copyboard - edit")
        self.panel_editors.SetScrollRate(10, 10)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: EditView.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_editors = wx.BoxSizer(wx.VERTICAL)
        self.panel_editors.SetSizer(self.sizer_editors)
        sizer_2.Add(self.panel_editors, 1, wx.EXPAND, 0)
        sizer_3.Add(self.button_add, 0, 0, 0)
        sizer_3.Add(self.button_remove, 0, 0, 0)
        sizer_3.Add(self.button_ok, 0, 0, 0)
        sizer_3.Add(self.button_cancel, 0, 0, 0)
        sizer_3.Add((20, 20), 0, 0, 0)
        sizer_2.Add(sizer_3, 0, 0, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

    def button_add_click(self, event):  # wxGlade: EditView.<event_handler>
        print "Event handler 'button_add_click' not implemented!"
        event.Skip()

    def button_remove_click(self, event):  # wxGlade: EditView.<event_handler>
        print "Event handler 'button_remove_click' not implemented!"
        event.Skip()

    def button_ok_click(self, event):  # wxGlade: EditView.<event_handler>
        print "Event handler 'button_ok_click' not implemented!"
        event.Skip()

    def button_cancel_click(self, event):  # wxGlade: EditView.<event_handler>
        print "Event handler 'button_cancel_click' not implemented!"
        event.Skip()

# end of class EditView
