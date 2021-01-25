
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
import locale
import wx
import wx.xrc

class MySangpum ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"상품처리", pos = wx.DefaultPosition, size = wx.Size( 710,366 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        self.SetBackgroundColour( wx.Colour( 239, 207, 171 ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"상품명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtSang = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtSang, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"수량 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtSu = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer2.Add( self.txtSu, 0, wx.ALL, 5 )
        
        self.txtda = wx.StaticText( self.m_panel1, wx.ID_ANY, u"단가", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtda.Wrap( -1 )
        bSizer2.Add( self.txtda, 0, wx.ALL, 5 )
        
        self.txtDan = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtDan, 0, wx.ALL, 5 )
        
        self.btnOk = wx.Button( self.m_panel1, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btnOk.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer2.Add( self.btnOk, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstView = wx.ListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        self.lstView.SetBackgroundColour( wx.Colour( 241, 233, 158 ) )
        
        bSizer3.Add( self.lstView, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txtc = wx.StaticText( self.m_panel3, wx.ID_ANY, u"건수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtc.Wrap( -1 )
        bSizer4.Add( self.txtc, 0, wx.ALL, 5 )
        
        self.staCount = wx.StaticText( self.m_panel3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer4.Add( self.staCount, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnOk.Bind( wx.EVT_BUTTON, self.OnInsert )
        
        
         #표 제목
        self.lstView.InsertColumn(0, '코드', width = 50)
        self.lstView.InsertColumn(1, '상품명', width = 150)
        self.lstView.InsertColumn(2, '단가', width = 150)
        self.lstView.InsertColumn(3, '수량', width = 150)
        self.lstView.InsertColumn(4, '금액', width = 150)
        
        locale.setlocale(locale.LC_NUMERIC) #세 자리마다 ,(comma)를 출력하기 위한 설정
        
        self.ListData()     # 화면 로딩 후 상품자료 바로 보기.
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnInsert( self, event ):
        #입력자료 검사
        if self.txtSang.GetValue() == '' or self.txtSu.GetValue()==''  or self.txtDan.GetValue()=='' :
            wx.MessageBox('입력자료를 모두 채우시오', '알림', wx.OK)
            return
        
        #isdigit() 숫자면 true 아니면 false
        if self.txtSu.GetValue().isalpha() or self.txtDan.GetValue().isalpha():                 # 문자면 true/
            wx.MessageBox('수량과 단가는 숫자만 허용', '알림', wx.OK)
            return
        #...입력 자료 검사는 추가로... 음수는 불가능 등등등
        
         #등록 계속
        sang = self.txtSang.GetValue()
        su = self.txtSu.GetValue()
        dan = self.txtDan.GetValue()
       
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            #새상품 code 얻기(기존에 있는 코드에 1 추가한 숫자.)
            try:
                cursor.execute("select max(code) from sangdata")
                code = cursor.fetchone()[0] +1
            except:
                code = 1
            
            #print('code : ',code)
            
            tdata = (code, sang, su, dan)
            cursor.execute("insert into sangdata values(%s,%s,%s,%s)", tdata)
            conn.commit()
            
            #추가 후 목록보기 및 초기화.
            self.ListData()
            
            self.txtSang.SetLabel('')
            self.txtDan.SetLabel('')
            self.txtSu.SetLabel('')
            
            self.txtSang.SetFocus()
            
        except Exception as e:
            wx.MessageBox('추가 실패 : ' + str(e), wx.OK)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()    
        
    def ListData(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            cursor.execute("select * from sangdata order by code desc")
            
            datas = cursor.fetchall()
            #print(datas)
            
            self.lstView.DeleteAllItems()       # 표 초기화
            
            for row in datas:
                i = self.lstView.InsertItem(1000, 0)        # 최대 가능 행 수, 초기 값
                self.lstView.SetItem(i, 0, str(row[0]))
                self.lstView.SetItem(i, 1, row[1])
                self.lstView.SetItem(i, 2, str(row[2]))
                self.lstView.SetItem(i, 3, str(row[3]))
                price = row[2] * row[3]
                #self.lstView.SetItem(i,4,str(price))
                self.lstView.SetItem(i,4,locale.format_string('%d',price,1))
            
            #건수
            #self.staCount.SetLabel(str(len(datas)))            # 방법 1 -  datas 의 길이를 잰 것
            self.staCount.SetLabel(str(self.lstView.GetItemCount()))     #방법 2 - lstView 의 아이템 갯수 카운트
        except Exception as e:
            wx.MessageBox('목록보기 에러 '+ str(e), '오류', wx.OK)
        finally:
            cursor.close()
            conn.close()
        
       
        
   
    
if __name__ == '__main__':
    app = wx.App()
    MySangpum(None).Show()
    app.MainLoop()

