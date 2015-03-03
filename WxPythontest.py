# -*- coding: utf-8 -*-
"""
Created on Mon Mar 02 22:14:04 2015

@author: Angie
"""

import wx

########################################################################
class MyFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Callbacks")
        panel = wx.Panel(self)

        self.choice = wx.Choice(panel, choices=["test_A", "test_B"])
        self.choice.Bind(wx.EVT_CHOICE, self.onChoice)

        self.Show()
    #----------------------------------------------------------------------
    def onChoice(self, event):
        """"""
        choice = self.choice.GetStringSelection()
        method = getattr(self, "on_%s" % choice)
        method()

    #----------------------------------------------------------------------
    def on_test_A(self):
        """"""
        print "You chose test_A!"

    #----------------------------------------------------------------------
    def on_test_B(self):
        """"""
        print "You chose test_B!"


#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()