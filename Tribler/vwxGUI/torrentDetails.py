# -*- coding: iso-8859-1 -*- 
# Don't modify comment 

import wx
from bgPanel import *
#[inc]add your include files here

#[inc]end your include

class torrentDetails(wx.Panel):
    def __init__(self,parent,id = -1,pos = wx.Point(0,0),size = wx.Size(300,462),style = wx.TAB_TRAVERSAL,name = 'panel'):
        pre=wx.PrePanel()
        self.OnPreCreate()
        pre.Create(parent,id,pos,size,style,name)
        self.PostCreate(pre)
        self.initBefore()
        self.VwXinit()
        self.initAfter()

    def __del__(self):
        self.Ddel()
        return


    def VwXinit(self):
        self.fileImgBuf=[None] * 1
        self.fileImgBuf[0] = wx.Bitmap("images/triblerpanel_topcenter.png",wx.BITMAP_TYPE_PNG)
        self.pn10cImg0=self.fileImgBuf[0];
        self.Show(True)
        self.SetForegroundColour(wx.Colour(216,216,191))
        self.pn10c = wx.Panel(self,-1,wx.Point(16,0),wx.Size(218,21))
        self.pn10c.SetForegroundColour(wx.Colour(255,255,255))
        self.pn10c.SetBackgroundColour(wx.Colour(255,51,0))
        self.pn10c.Bind(wx.EVT_ERASE_BACKGROUND,self.VwXpn10c_VwXEvOnEraseBackground)
        self.st64c = wx.StaticText(self.pn10c,-1,"",wx.Point(0,4),wx.Size(194,17),wx.ST_NO_AUTORESIZE)
        self.st64c.SetLabel("The sony bravia commercial")
        self.playbackControls = bgPanel(self, -1, wx.Point(0,196), wx.Size(20,20))
        self.6_160x90 = bgPanel(self, -1, wx.Point(0,26), wx.Size(302,170))
        self.tabs = wx.Panel(self,-1,wx.Point(0,162),wx.Size(20,20))
        self.tabs.SetBackgroundColour(wx.Colour(110,110,110))
        self.pn39cCCC = wx.Panel(self.tabs,-1,wx.Point(3,3),wx.Size(40,15))
        self.pn39cCCC.SetBackgroundColour(wx.Colour(255,255,255))
        self.st60cCC = wx.StaticText(self.pn39cCCC,-1,"",wx.Point(5,0),wx.Size(20,10),wx.ST_NO_AUTORESIZE)
        self.st60cCC.SetLabel("info")
        self.pn39cCC2C = wx.Panel(self.tabs,-1,wx.Point(46,3),wx.Size(65,15))
        self.pn39cCC2C.SetBackgroundColour(wx.Colour(205,205,205))
        self.st60cCC = wx.StaticText(self.pn39cCC2C,-1,"",wx.Point(5,0),wx.Size(49,13),wx.ST_NO_AUTORESIZE)
        self.st60cCC.SetLabel("comments")
        self.st60cCC.SetForegroundColour(wx.Colour(0,0,0))
        self.details = wx.Panel(self,-1,wx.Point(0,242),wx.Size(20,20))
        self.details.SetBackgroundColour(wx.Colour(255,255,255))
        self.white_bottom = bgPanel(self, -1, wx.Point(3,437), wx.Size(302,5))
        self.orange_top_left = bgPanel(self, -1, wx.Point(0,0), wx.Size(10,21))
        self.orange_top_right = bgPanel(self, -1, wx.Point(288,0), wx.Size(10,21))
        self.sz3s = wx.BoxSizer(wx.VERTICAL)
        self.header = wx.BoxSizer(wx.HORIZONTAL)
        self.sz65s = wx.BoxSizer(wx.HORIZONTAL)
        self.tabsCCC = wx.BoxSizer(wx.HORIZONTAL)
        self.sz61sCC = wx.BoxSizer(wx.HORIZONTAL)
        self.sz61sCC = wx.BoxSizer(wx.HORIZONTAL)
        self.sz3s.Add(self.header,0,wx.EXPAND|wx.FIXED_MINSIZE,0)
        self.sz3s.Add(self.6_160x90,0,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.sz3s.Add(self.playbackControls,0,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.sz3s.Add(self.tabs,0,wx.BOTTOM|wx.EXPAND|wx.FIXED_MINSIZE,6)
        self.sz3s.Add(self.details,1,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.sz3s.Add(self.white_bottom,0,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.header.Add(self.orange_top_left,0,wx.EXPAND|wx.FIXED_MINSIZE,0)
        self.header.Add(self.pn10c,1,wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.header.SetItemMinSize(self.pn10c,20,10)
        self.header.Add(self.orange_top_right,0,wx.EXPAND|wx.FIXED_MINSIZE,0)
        self.sz65s.Add(self.st64c,1,wx.TOP|wx.EXPAND,4)
        self.tabsCCC.Add(self.pn39cCCC,0,wx.TOP|wx.LEFT|wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.tabsCCC.Add(self.pn39cCC2C,0,wx.TOP|wx.LEFT|wx.RIGHT|wx.EXPAND|wx.FIXED_MINSIZE,3)
        self.sz61sCC.Add(self.st60cCC,0,wx.LEFT|wx.EXPAND|wx.FIXED_MINSIZE,5)
        self.sz61sCC.SetItemMinSize(self.st60cCC,20,10)
        self.sz61sCC.Add(self.st60cCC,0,wx.LEFT|wx.EXPAND|wx.FIXED_MINSIZE,5)
        self.SetSizer(self.sz3s);self.SetAutoLayout(1);self.Layout();
        self.pn10c.SetSizer(self.sz65s);self.pn10c.SetAutoLayout(1);self.pn10c.Layout();
        self.tabs.SetSizer(self.tabsCCC);self.tabs.SetAutoLayout(1);self.tabs.Layout();
        self.pn39cCCC.SetSizer(self.sz61sCC);self.pn39cCCC.SetAutoLayout(1);self.pn39cCCC.Layout();
        self.pn39cCC2C.SetSizer(self.sz61sCC);self.pn39cCC2C.SetAutoLayout(1);self.pn39cCC2C.Layout();
        self.Refresh()
        return
    def VwXDrawBackImg(self,event,win,bitMap,opz):
        if (event.GetDC()):
            dc=event.GetDC()
        else: dc = wx.ClientDC(win)
        dc.SetBackground(wx.Brush(win.GetBackgroundColour(),wx.SOLID))
        dc.Clear()
        if (opz==0):
            dc.DrawBitmap(bitMap,0, 0, 0)
        if (opz==1):
            rec=wx.Rect()
            rec=win.GetClientRect()
            rec.SetLeft((rec.GetWidth()-bitMap.GetWidth())   / 2)
            rec.SetTop ((rec.GetHeight()-bitMap.GetHeight()) / 2)
            dc.DrawBitmap(bitMap,rec.GetLeft(),rec.GetTop(),0)
        if (opz==2):
            rec=wx.Rect()
            rec=win.GetClientRect()
            for y in range(0,rec.GetHeight(),bitMap.GetHeight()):
                for x in range(0,rec.GetWidth(),bitMap.GetWidth()):
                    dc.DrawBitmap(bitMap,x,y,0)

    def VwXDelComp(self):
        return
    def VwXpn10c_VwXEvOnEraseBackground(self,event):
        self.VwXDrawBackImg(event,self.pn10c,self.pn10cImg0,2)
        self.pn10c_VwXEvOnEraseBackground(event)
        event.Skip(False)

        return

#[win]add your code here

    def pn10c_VwXEvOnEraseBackground(self,event): #init function
        #[144]Code event VwX...Don't modify[144]#
        #add your code here
        event.Skip()

        return #end function

    def OnPreCreate(self):
        #add your code here

        return

    def initBefore(self):
        #add your code here

        return

    def initAfter(self):
        #add your code here

        return

    def Ddel(self): #init function
        #[142]Code VwX...Don't modify[142]#
        #add your code here

        return #end function

#[win]end your code
