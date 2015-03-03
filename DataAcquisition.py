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
        sampleList = ["北京大学","清华大学","复旦大学","浙江大学","上海交通大学","南京大学",
                      "中山大学","吉林大学","武汉大学","中国科技大学","华中科技大学",
                      "中国人民大学","四川大学","南开大学","山东大学","北京师范大学",
                      "哈尔滨工业大学","西安交通大学","中南大学","厦门大学","东南大学",
                      "天津大学","北京航空航天大学","大连理工大学","华东师范大学",
                      "华南理工大学","中国农业大学","湖南大学","兰州大学","重庆大学",
                      "西北工业大学","东北大学","北京理工大学","华东理工大学","北京协和医学院",
                      "东北师范大学","北京科技大学","中国地质大学","武汉理工大学","华中师范大学",
                      "西北大学","中国矿业大学","华中农业大学","电子科技大学","长安大学",
                      "东华大学","西南大学","中国海洋大学","南京航空航天大学","南京理工大学",
                      "西南交通大学","北京交通大学","苏州大学","中国石油大学","云南大学",
                      "北京化工大学","西安电子科技大学","南京农业大学","西北农林科技大学",
                      "南京师范大学","上海大学","郑州大学","河海大学","北京邮电大学",
                      "哈尔滨工程大学","合肥工业大学","湖南师范大学","暨南大学","福州大学",
                      "南昌大学","北京林业大学","北京工业大学","华南师范大学","陕西师范大学",
                      "江南大学","华南农业大学","首都医科大学","中国政法大学","新疆大学",
                      "广西大学","内蒙古大学","华北电力大学","上海财经大学","中央民族大学",
                      "南京医科大学","山西大学","河南大学","太原理工大学","中南财经政法大学",
                      "安徽大学","南方医科大学","湘潭大学","贵州大学","哈尔滨医科大学",
                      "南京工业大学","燕山大学","浙江工业大学","东北林业大学","辽宁大学","其他"]
        sampleList2 = ['CS','EE','ME','Sta']  
        sampleList3 = ['Master','Ph.D.']  
        sampleList4 = ["普林斯顿大学","哈佛大学","耶鲁大学","斯坦福大学","芝加哥大学","哥伦比亚大学",
        "麻省理工学院","宾夕法尼亚大学","杜克大学","加利福尼亚理工学院","达特茅斯学院","约翰霍普金斯大学",
        "美国西北大学","圣路易斯华盛顿大学","康奈尔大学","布朗大学","圣母诺特丹大学","范德堡大学",
        "莱斯大学","加州大学伯克利分校","埃默里大学","乔治城大学","加州大学洛杉矶分校","弗吉尼亚大学",
        "卡内基梅隆大学","南加州大学","威克弗里斯特大学","塔夫斯大学","密歇根大学安娜堡分校",
        "北卡罗来纳州大学教堂山分校","波士顿学院","纽约大学","罗彻斯特大学","威廉玛丽学院",
        "布兰戴斯大学","佐治亚理工学院","加州大学圣地亚哥分校","加州大学戴维斯分校","凯斯西储大学",
        "加州大学圣塔芭芭拉分校","利哈伊大学","伦斯勒理工学院","波士顿大学","加州大学欧文分校",
        "伊利诺伊大学香槟分校","美国东北大学","威斯康星大学-麦迪逊分校","耶斯希瓦大学",
        "华盛顿大学","佛罗里达大学","迈阿密大学","宾州州立大学","德克萨斯大学-奥斯汀分校",
        "佩珀代因大学","乔治华盛顿大学","俄亥俄州立大学","杜兰大学","雪城大学","南卫理公会大学",
        "康涅狄格大学","佛罕大学","匹兹堡大学","乔治亚大学","杨百翰大学","克莱蒙森大学",
        "马里兰大学-伯克分校","普渡大学本校","伍斯特理工学院","德州农工大学康莫斯校区","罗格斯大学",
        "明尼苏达大学","贝勒大学","美国大学","爱荷华大学","弗吉尼亚理工大学","史蒂文斯科技学院",
        "麻省大学-艾默斯特校区","克拉克大学","德克萨斯基督教大学","印第安纳大学伯明顿主校区",
        "德拉华大学","马凯特大学","迈阿密大学-牛津分校","纽约州立大学-环境科学与林业科学学院",
        "佛蒙特大学","加州大学圣克鲁兹分校","密歇根州立大学","宾汉姆顿大学","纽约州立大学-石溪分校",
        "罗拉多矿业大学","丹佛大学","塔尔萨大学","科罗拉多大学波德分校","阿拉巴马大学",
        "佛罗里达州立大学","圣地亚哥大学","德雷塞尔大学","北卡罗来纳州立大学","内布拉斯加大学林肯校区",
        "新罕布什尔大学","密苏里大学","圣路易斯大学","纽约州立大学-水牛城分校","代顿大学",
        "奥本大学","俄克拉荷马大学","奥瑞冈大学","芝加哥洛约拉大学","堪萨斯大学","旧金山大学",
        "田纳西大学","爱荷华州立大学","加州大学河滨分校","南卡罗来纳大学哥伦比亚分校","圣托马斯大学",
        "太平洋大学","迪尤肯大学","美国天主教大学","密歇根理工大学","伊利诺理工学院","天普大学",
        "克拉克森大学","亚利桑那大学","科罗拉多州立大学","德保罗大学","薛顿贺尔大学","奥尔巴尼大学",
        "罗格斯大学纽瓦克分校","犹他大学","亚利桑那州立大学","辛辛那提大学","俄亥俄大学","肯塔基大学",
        "路易斯安那州立大学","霍夫斯特拉大学","阿肯色大学","新学院","华盛顿州立大学","乔治梅森大学",
        "密苏里理工大学","俄勒冈州立大学","堪萨斯州立大学","伊利诺伊州立大学","圣约翰费舍尔大学",
        "圣约翰大学（纽约）","哈沃德大学","德克萨斯大学-达拉斯分校","俄克拉荷马州立大学","阿德菲大学",
        "伊利诺伊大学芝加哥分校","阿拉巴马大学伯明翰分校","新泽西理工学院","圣地亚哥州立大学",
        "密西西比大学","马里兰大学巴尔的摩县分校","美国密西西比州立大学","弗吉尼亚联邦大学",
        "德州理工大学","玛萨诸塞大学","圣路易斯玛丽维尔大学","罗德岛大学","怀俄明大学",
        "南佛罗里达大学","拜欧拉大学","路易斯维尔大学","爱达荷大学","加州拉文大学","北达科他大学",
        "南达科他大学","西弗吉尼亚大学","夏威夷大学","安德鲁大学","佛罗里达理工学院","博林格林州立大学",
        "中佛罗里达大学","缅因州立大学","西密歇根大学","博尔州立大学","阿苏萨太平洋大学","佩斯大学",
        "北卡罗来纳大学格林波若分校","明尼苏达圣玛丽大学","依马库雷塔大学","斯伯汀大学","艾格伍学院",
        "南达科塔州立大学","北达科他州立大学","阿拉巴马汉茨维尔大学","休斯顿大学","密苏里大学-堪萨斯分校",
        "新墨西哥大学","南伊利诺伊大学卡本代尔校区","威得恩大学","内华达州立大学雷诺分校","肯特州立大学",
        "中央密西根大学","犹他州立大学","北伊利诺伊大学","蒙大拿州立大学",
        "印第安纳大学与普渡大学印第安纳波里斯联合分校","路易斯安那理工大学","北卡罗莱纳-夏洛特分校","其他"
]  
        
        self.Label1=wx.StaticText(panel, -1, "Mas/Ph.D.:", (40, 20))
        self.Choice1=wx.Choice(panel, -1, (110, 18), choices=sampleList3)
        self.Choice1.Bind(wx.EVT_CHOICE, self.onChoice1)
        
        self.Label2=wx.StaticText(panel, -1, "Bachelor:", (40, 60))
        self.Choice2=wx.Choice(panel, -1, (110, 58), choices=sampleList)
        self.Choice2.Bind(wx.EVT_CHOICE, self.onChoice2)
      
        self.Label3=wx.StaticText(panel, -1, "Master:", (40, 100))
        self.Choice3=wx.Choice(panel, -1, (110, 98), choices=sampleList)
        self.Choice3.Bind(wx.EVT_CHOICE, self.onChoice3)
       
        self.Label4=wx.StaticText(panel, -1, "BaMajor:", (40, 140))
        self.Choice4=wx.Choice(panel, -1, (110, 138), choices=sampleList2) 
        self.Choice4.Bind(wx.EVT_CHOICE, self.onChoice4)

        self.Label5=wx.StaticText(panel, -1, "MaMajor:", (40, 180))
        self.Choice5=wx.Choice(panel, -1, (110, 178), choices=sampleList2)
        self.Choice5.Bind(wx.EVT_CHOICE, self.onChoice5)
        
        self.Label6=wx.StaticText(panel, -1, "ApMajor:", (40, 220))
        self.Choice6=wx.Choice(panel, -1, (110, 218), choices=sampleList2) 
        self.Choice6.Bind(wx.EVT_CHOICE, self.onChoice6)
                        
        self.Label7=wx.StaticText(panel, -1, "BaGPA:", (260, 20))
        self.Text1=wx.TextCtrl(panel, -1, '3.5', (330, 18)) 
        self.Text1.Bind(wx.EVT_CHOICE, self.onText1)         
        
        self.Label8=wx.StaticText(panel, -1, "MaGPA:", (260, 60))
        self.Text2=wx.TextCtrl(panel, -1,'3.5',  (330, 58)) 
        self.Text2.Bind(wx.EVT_CHOICE, self.onText2)  

        self.Label9=wx.StaticText(panel, -1, "GRE:", (260, 100))
        self.Text3=wx.TextCtrl(panel, -1, '1100', (330, 98)) 
        self.Text3.Bind(wx.EVT_CHOICE, self.onText3)           
        
        self.Label10=wx.StaticText(panel, -1, "TOELF:", (260, 140))
        self.Text4=wx.TextCtrl(panel, -1,'95',  (330, 138))
        self.Text4.Bind(wx.EVT_CHOICE, self.onText4)  
        
        self.Label11=wx.StaticText(panel, -1, "Papers:", (260, 180))
        self.Text5=wx.TextCtrl(panel, -1, '5', (330, 178))
        self.Text5.Bind(wx.EVT_CHOICE, self.onText5)            
        
        self.Label12=wx.StaticText(panel, -1, "SCI:", (260, 220))
        self.Text6=wx.TextCtrl(panel, -1,'2',  (330, 218))
        self.Text6.Bind(wx.EVT_CHOICE, self.onText6)  
        
        self.Label13=wx.StaticText(panel, -1, "录取院校:", (60, 260))
        self.Choice7=wx.Choice(panel, -1, (130, 258), choices=sampleList4)   

        self.button = wx.Button(panel, -1, "提交", pos=(200, 300))  
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)  
        self.button.SetDefault()  
        
    def onChoice1(self, event):
        """"""
        choice = self.Choice1.GetSelection()+1
        print choice
        
    def onChoice2(self, event):
        """"""
        choice = self.Choice2.GetSelection()+1
        print choice
        
    def onChoice3(self, event):
        """"""
        choice = self.Choice3.GetSelection()+1
        print choice
        
    def onChoice4(self, event):
        """"""
        choice = self.Choice4.GetSelection()+1
        print choice
        
    def onChoice5(self, event):
        """"""
        choice = self.Choice5.GetSelection()+1
        print choice
        
    def onChoice6(self, event):
        """"""
        choice = self.Choice6.GetSelection()+1
        print choice

    def onText1(self, event):
        """"""
        text = float(self.Text1.GetValue())
        print text        

    def onText2(self, event):
        """"""
        text = float(self.Text2.GetValue())
        print text

    def onText3(self, event):
        """"""
        text = int(self.Text3.GetValue())
        print text

    def onText4(self, event):
        """"""
        text = int(self.Text4.GetValue())
        print text

    def onText5(self, event):
        """"""
        text = int(self.Text5.GetValue())
        print text

    def onText6(self, event):
        """"""
        text = int(self.Text6.GetValue())
        print text      
                 
    def OnClick(self, event):  
        Feature=[self.Choice1.GetSelection()+1,self.Choice2.GetSelection()+1,
                      self.Choice3.GetSelection()+1,self.Choice4.GetSelection()+1,
                      self.Choice5.GetSelection()+1,self.Choice6.GetSelection()+1,
                      float(self.Text1.GetValue()),float(self.Text2.GetValue()),
                      int(self.Text3.GetValue()),int(self.Text4.GetValue()),
                      int(self.Text5.GetValue()),int(self.Text6.GetValue())]
        Result=[self.Choice7.GetSelection()+1]
        
        f = open('TrainData.txt', 'a+') 
        f.write(str(Feature)) 
        f.write(str(Result)) 
        f.write('\n')
        f.close() 
        
        print Feature
        print Result
#        self.button.SetLabel("提交成功") 
        
                
if __name__ == '__main__':
    app = wx.PySimpleApp()
    LeonFrame=ChoiceFrame()
    LeonFrame.Show()
    app.MainLoop() 
