import wx
import wx.xrc

class Jikwon ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"직원 자료", pos = wx.DefaultPosition, size = wx.Size( 602,483 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"사번 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtNo = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtNo, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"직원명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.btnLogin = wx.Button( self.m_panel1, wx.ID_ANY, u"로그인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btnLogin, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staNum = wx.StaticText( self.m_panel2, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.staNum.Wrap( -1 )
        bSizer3.Add( self.staNum, 0, wx.ALL, 5 )
        
        self.m_staticText6 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"번 직원의 관리 고객", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstGogek = wx.ListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer4.Add( self.lstGogek, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.lstGogek.InsertColumn(0, '고객 번호', width = -1)
        self.lstGogek.InsertColumn(1, '고객명', width = -1)
        self.lstGogek.InsertColumn(2, '고객 전화', width = -1)

        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"인원수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.staCount = wx.StaticText( self.m_panel4, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer5.Add( self.staCount, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 0, wx.ALL|wx.EXPAND, 5 )
        
        

        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnLogin.Bind( wx.EVT_BUTTON, self.ShowList )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def ShowList( self, event ):
        
        if self.txtNo.GetValue() == '':
            wx.MessageBox('사번을 입력하시오', '에러', wx.OK)
            return
        elif self.txtName.GetValue() == '':
            wx.MessageBox('이름을 입력하시오', '에러', wx.OK)
            return
            
        
        self.lstGogek.DeleteAllItems()
        self.staCount.SetLabel('0')
        ''''''    
        config = {
            'host':'127.0.0.1',
            'user':'root',
            'password':'123',
            'database':'test',
            'port':3306,
            'charset':'utf8',
            'use_unicode':True
        }
        
        import MySQLdb
    
        try:
            conn = MySQLdb.connect(**config) # dict type을 읽을 때는 ** (※ *: tuple)
            cursor = conn.cursor()
            
            no = self.txtNo.GetValue()
            name = self.txtName.GetValue()
            sql = '''
                SELECT jikwon_no, jikwon_name
                FROM jikwon WHERE jikwon_no={0} AND jikwon_name='{1}'
            '''.format(no, name)
            # print(sql)
            
            try:
                cursor.execute(sql)
            except Exception:
                wx.MessageBox('직원 정보가 없습니다.', '정보 없음', wx.OK)
                return
            
            self.staNum.SetLabel(no)
            
            sql = '''
                SELECT gogek_no, gogek_name, gogek_tel
                FROM gogek WHERE gogek_damsano={0}
            '''.format(no)
            
            cursor.execute(sql)
            datas = cursor.fetchall()
            
            if len(datas) == 0:
                errMsg =['고객', '자료가', '없습니다']
                index = self.lstGogek.InsertItem(1,errMsg[0])
                self.lstGogek.SetItem(index, 1, errMsg[1])
                self.lstGogek.SetItem(index, 2, errMsg[2])
                
                return
        
            for d in datas:
                # print(d[0], d[1], d[2])
                index = self.lstGogek.InsertItem(100, str(d[0]))
                self.lstGogek.SetItem(index, 1, d[1])
                self.lstGogek.SetItem(index, 2, d[2])
            
            # print('인원 수 : ' + str(len(datas)))
            self.staCount.SetLabel(str(len(datas)))
            
        except Exception as e1:
            print('err1 : ' + str(e1))
        finally:
            cursor.close()
            conn.close()
    
if __name__ == '__main__':
    app = wx.App()
    Jikwon(None).Show()
    app.MainLoop()
