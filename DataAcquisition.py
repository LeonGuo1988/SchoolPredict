# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 09:26:21 2015

@author: loen
"""
#coding:utf-8
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8") 

import wx

class ChoiceFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, '留学预测数据采集', 
                size=(500, 400))
        panel = wx.Panel(self, -1)
        sampleList = ['清华','北大','复旦','人大']
        sampleList2 = ['CS','EE','ME','Sta']  
        sampleList3 = ['Master','Ph.D.']  
        sampleList4 = ['斯坦福大学','加州大学伯克利分校','哈佛大学']  
        
        self.Label1=wx.StaticText(panel, -1, "Mas/Ph.D.:", (40, 20))
        self.Choice1=wx.Choice(panel, -1, (110, 18), choices=sampleList3)
        self.Choice1.Bind(wx.EVT_CHOICE, self.onChoice1)

        
        self.Label2=wx.StaticText(panel, -1, "Bachelor:", (40, 60))
        self.Choice2=wx.Choice(panel, -1, (110, 58), choices=sampleList)

        
        self.Label3=wx.StaticText(panel, -1, "Master:", (40, 100))
        self.Choice3=wx.Choice(panel, -1, (110, 98), choices=sampleList)

        
        self.Label4=wx.StaticText(panel, -1, "BaMajor:", (40, 140))
        self.Choice4=wx.Choice(panel, -1, (110, 138), choices=sampleList2)  

        self.Label5=wx.StaticText(panel, -1, "MaMajor:", (40, 180))
        self.Choice5=wx.Choice(panel, -1, (110, 178), choices=sampleList2)
        
        self.Label6=wx.StaticText(panel, -1, "ApMajor:", (40, 220))
        self.Choice6=wx.Choice(panel, -1, (110, 218), choices=sampleList2)   
        
                
        self.Label7=wx.StaticText(panel, -1, "BaGPA:", (260, 20))
        self.Text1=wx.TextCtrl(panel, -1, 'GPA 3.5', (330, 18))          
        
        self.Label8=wx.StaticText(panel, -1, "MaGPA:", (260, 60))
        self.Text2=wx.TextCtrl(panel, -1,'GPA 3.5',  (330, 58))  

        self.Label9=wx.StaticText(panel, -1, "GRE:", (260, 100))
        self.Text3=wx.TextCtrl(panel, -1, 'GRE 1100', (330, 98))          
        
        self.Label10=wx.StaticText(panel, -1, "TOELF:", (260, 140))
        self.Text4=wx.TextCtrl(panel, -1,'TOELF 95',  (330, 138))      
        
        self.Label11=wx.StaticText(panel, -1, "Papers:", (260, 180))
        self.Text5=wx.TextCtrl(panel, -1, '5', (330, 178))          
        
        self.Label12=wx.StaticText(panel, -1, "SCI:", (260, 220))
        self.Text6=wx.TextCtrl(panel, -1,'2',  (330, 218))   
        
        self.Label13=wx.StaticText(panel, -1, "录取院校:", (150, 260))
        self.Choice7=wx.Choice(panel, -1, (220, 258), choices=sampleList4)   

        self.button = wx.Button(panel, -1, "提交", pos=(200, 300))  
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)  
        self.button.SetDefault()  
        
    def onChoice1(self, event):
        """"""
        choice = self.Choice1.GetStringSelection()
        print choice
        
        
    def OnClick(self, event):  
        Feature=[self.Choice1.GetStringSelection(),self.Choice2.GetStringSelection(),
                      self.Choice3.GetStringSelection(),self.Choice4.GetStringSelection(),
                      self.Choice5.GetStringSelection(),self.Choice6.GetStringSelection(),
                      self.Text1.GetStringSelection(),self.Text2.GetStringSelection(),
                      self.Text3.GetStringSelection(),self.Text4.GetStringSelection(),
                      self.Text5.GetStringSelection(),self.Text6.GetStringSelection()]
        Result=[self.Choice7.GetStringSelection()]
        print Feature
        print Result
        self.button.SetLabel("提交成功") 
        

        
              
if __name__ == '__main__':
    app = wx.PySimpleApp()
    LeonFrame=ChoiceFrame()
    LeonFrame.Show()
    app.MainLoop() 
