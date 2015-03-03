# -*- coding: utf-8 -*-
"""
Created on Tue Mar 03 21:30:53 2015

@author: Angie
"""

#coding:utf-8
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8") 

#import wx,sys,os,win32ui
import wx
########################################################################
#set the file filter
wildcard1 = "All files (*.*)|*.*|" \
            "Python source (*.py; *.pyc)|*.py;*.pyc"
wildcard2 = "Python source (*.py; *.pyc)|*.py;*.pyc|" \
            "All files (*.*)|*.*"
########################################################################
class MyForm(wx.Frame):

    #-------------------------------------------------------------------
    #set the window layout
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,\
                          "模型训练",\
                          pos =(0,0), size =(410,500))
        #def the global variance
        global TxtCfn,Contents,TrainNumber,ModelChoice,btnT
        
        sampleList=['Ordinary Least Squares','Ridge Regression','Bayesian Regression'];
        #layout the Frame
        panel = wx.Panel(self, wx.ID_ANY)
        TxtCfn=wx.TextCtrl(panel,pos=(15,5),size=(200,25))
        btnO = wx.Button(panel, label="Open",pos=(225,5),size=(70,25))
        btnS = wx.Button(panel, label="Save",pos=(300,5),size=(70,25))
        Contents=wx.TextCtrl(panel,pos=(15,35),size=(360,260),
                     style=wx.TE_MULTILINE|wx.HSCROLL)

        wx.StaticText(panel, -1, "模型选择:", pos=(15,305),size=(60,25))
        ModelChoice=wx.Choice(panel, -1, pos=(80,300),size=(280,25),choices=sampleList)
                             
        wx.StaticText(panel, -1, "训练次数:", pos=(15,335),size=(60,25))
        TrainNumber=wx.TextCtrl(panel, -1, '10', pos=(80,330),size=(280,25))
        
        btnT = wx.Button(panel, label="开始训练",pos=(15,360),size=(360,25))
                   
        #bind the button event
        btnO.Bind(wx.EVT_BUTTON, self.onOpenFile)
        btnS.Bind(wx.EVT_BUTTON, self.onSaveFile)
        btnT.Bind(wx.EVT_BUTTON, self.onTrainModel)
     #-------------------------------------------------------------------
     #def [onOpenFile] function of the label [open]button
    def onOpenFile(self, event):
        """
        Create and show the Open FileDialog
        """
        btnT.SetLabel("开始训练") 
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard=wildcard1,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            tmp=""
            #paths = dlg.GetPaths()
            paths = dlg.GetPaths()
            print paths
            #print "You chose the following file(s):"
            for path in paths:
                tmp=tmp+path
            #set the value of TextCtrl[filename]
            TxtCfn.SetValue(tmp)
            #set the value to the TextCtrl[contents]
            file=open(TxtCfn.GetValue())
            Contents.SetValue(file.read())
            file.close()
        dlg.Destroy()
      #def onSaveFile function
    def onSaveFile(self,event):
        """
        Create and show the Save FileDialog
        """
        dlg = wx.FileDialog(self,
                            message="select the Save file style",
                            defaultFile="",
                            wildcard=wildcard2,
                            style=wx.SAVE
                            )
        if dlg.ShowModal() == wx.ID_OK:
            filename=""
            paths = dlg.GetPaths()
            #split the paths
            for path in paths:
                filename=filename+path
            #write the contents of the TextCtrl[Contents] into the file
            file=open(filename,'w')
            file.write(Contents.GetValue())
            file.close()
            #show the save file path
            TxtCfn.SetValue(filename)
        dlg.Destroy()   

    def onTrainModel(self,event):
        btnT.SetLabel("完成训练") 
           
#-----------------------------------------------------------------------
        
##########################################################################
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
