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
        
        wx.StaticText(panel, -1, "Mas/Ph.D.:", (40, 20))
        wx.Choice(panel, -1, (110, 18), choices=sampleList3)
        
        wx.StaticText(panel, -1, "Bachelor:", (40, 60))
        wx.Choice(panel, -1, (110, 58), choices=sampleList)  
        
        wx.StaticText(panel, -1, "Master:", (40, 100))
        wx.Choice(panel, -1, (110, 98), choices=sampleList)
        
        wx.StaticText(panel, -1, "BaMajor:", (40, 140))
        wx.Choice(panel, -1, (110, 138), choices=sampleList2)  

        wx.StaticText(panel, -1, "MaMajor:", (40, 180))
        wx.Choice(panel, -1, (110, 178), choices=sampleList2)
        
        wx.StaticText(panel, -1, "ApMajor:", (40, 220))
        wx.Choice(panel, -1, (110, 218), choices=sampleList2)   
        
                
        wx.StaticText(panel, -1, "BaGPA:", (260, 20))
        wx.TextCtrl(panel, -1, 'GPA 3.5', (330, 18))          
        
        wx.StaticText(panel, -1, "MaGPA:", (260, 60))
        wx.TextCtrl(panel, -1,'GPA 3.5',  (330, 58))  

        wx.StaticText(panel, -1, "GRE:", (260, 100))
        wx.TextCtrl(panel, -1, 'GRE 1100', (330, 98))          
        
        wx.StaticText(panel, -1, "TOELF:", (260, 140))
        wx.TextCtrl(panel, -1,'TOELF 95',  (330, 138))      
        
        wx.StaticText(panel, -1, "Papers:", (260, 180))
        wx.TextCtrl(panel, -1, '5', (330, 178))          
        
        wx.StaticText(panel, -1, "SCI:", (260, 220))
        wx.TextCtrl(panel, -1,'2',  (330, 218))   
        
        wx.StaticText(panel, -1, "录取院校:", (150, 260))
        wx.Choice(panel, -1, (220, 258), choices=sampleList4)   

        self.button = wx.Button(panel, -1, "提交", pos=(200, 300))  
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)  
        self.button.SetDefault()  
        
    def OnClick(self, event):  
        self.button.SetLabel("提交成功")  
    
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    ChoiceFrame().Show()
    app.MainLoop() 
