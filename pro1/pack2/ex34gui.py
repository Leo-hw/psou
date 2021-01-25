'''
wxFormBuilder 툴을 이용해 디자인 코드 작성
'''
# -*- coding: utf-8 -*- 


import wx
import wx.xrc


class MyFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"연습", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"이름", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtIrum = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtIrum, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"나이", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtNai = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer2.Add( self.txtNai, 0, wx.ALL, 5 )
        
        self.btnOk = wx.Button( self.m_panel1, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btnOk, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstView = wx.ListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer3.Add( self.lstView, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"인원수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.staInwon = wx.StaticText( self.m_panel3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staInwon.Wrap( -1 )
        bSizer4.Add( self.staInwon, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.lstView.InsertColumn(0, '이름', width = 200)
        self.lstView.InsertColumn(1, '나이', width = 100)
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnOk.Bind( wx.EVT_BUTTON, self.OnInsertData )
    
    
    
    # Virtual event handlers, overide them in your derived class
    def OnInsertData( self, event ):
        irum = self.txtIrum.GetValue()
        nai = self.txtNai.GetValue()
        
        i = self.lstView.InsertItem(5000, 0)
        self.lstView.SetItem(i, 0, irum)
        self.lstView.SetItem(i, 1, nai)
        self.staInwon.SetLabelText(str(self.lstView.GetItemCount()))
        
        self.txtIrum.SetValue('')           #자료 등록 후 입력 창 초기화
        self.txtNai.SetValue('')
        self.txtIrum.SetFocus()
        
if __name__ == '__main__':
    app = wx.App()
    MyFrame(None).Show()
    app.MainLoop()

