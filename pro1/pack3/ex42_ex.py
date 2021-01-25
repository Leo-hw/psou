import MySQLdb
import wx
import wx.xrc
import ast
with open('mariadb.txt', mode='r') as f:
    config = ast.literal_eval(f.read())

datas = []
rec_r = 0

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 559,334 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"사번 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtNo = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer1.Add( self.txtNo, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"이름 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer1.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"부서명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txtBuser = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer1.Add( self.txtBuser, 0, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"직급 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txtJik = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer1.Add( self.txtJik, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer1 )
        self.m_panel1.Layout()
        bSizer1.Fit( self.m_panel1 )
        bSizer5.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.m_panel2, wx.ID_ANY, u"||<<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel2, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.m_panel2, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btn3, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.m_panel2, wx.ID_ANY, u">>||", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer11 )
        self.m_panel2.Layout()
        bSizer11.Fit( self.m_panel2 )
        bSizer5.Add( self.m_panel2, 0, wx.EXPAND|wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer12 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_listCtrl2 = wx.ListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer12.Add( self.m_listCtrl2, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel3.SetSizer( bSizer12 )
        self.m_panel3.Layout()
        bSizer12.Fit( self.m_panel3 )
        bSizer5.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText17 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"고객 수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        bSizer13.Add( self.m_staticText17, 0, wx.ALL, 5 )
        
        self.staCount = wx.StaticText( self.m_panel4, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer13.Add( self.staCount, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer13 )
        self.m_panel4.Layout()
        bSizer13.Fit( self.m_panel4 )
        bSizer5.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer5 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.txtNo.Enable(enable=False)  # 보기만 가능 커서 안됨
        self.txtName.Enable(enable=False)
        self.txtBuser.Enable(enable=False)
        self.txtJik.Enable(enable=False)
        
        self.m_listCtrl2.InsertColumn(0, '고객번호') # 칼럼 추가
        self.m_listCtrl2.InsertColumn(1, '고객명')
        self.m_listCtrl2.InsertColumn(2, '고객전화')
        self.m_listCtrl2.InsertColumn(3, '성별')
        
        # 버튼의 이벤트 핸들러 장착
        self.btn1.id = 1
        self.btn2.id = 2
        self.btn3.id = 3
        self.btn4.id = 4
        
        
        # Connect Events
        self.btn1.Bind( wx.EVT_BUTTON, self.ClickFunc )
        self.btn2.Bind( wx.EVT_BUTTON, self.ClickFunc )
        self.btn3.Bind( wx.EVT_BUTTON, self.ClickFunc )
        self.btn4.Bind( wx.EVT_BUTTON, self.ClickFunc )
        
        self.DataLoad()
        self.GogekList(str(datas[rec_r][0]))
    
    def __del__( self ):
        pass
    
    def DataLoad(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            # sql문 작성
            sql = "select jikwon_no, jikwon_name, buser_name, jikwon_jik from jikwon,buser where buser_num = buser_no"
            cursor.execute(sql)
            global datas
            datas = cursor.fetchall()
            self.ShowData()
        except Exception as e:
            print("ShowData err: " + str(e))
        finally:
            cursor.close()
            conn.close()
        
    
    def ShowData(self):
        global rec_r
        #print(datas)
        self.txtNo.SetLabel(str(datas[rec_r][0]))
        self.txtName.SetLabel(datas[rec_r][1])
        self.txtBuser.SetLabel(datas[rec_r][2])
        self.txtJik.SetLabel(datas[rec_r][3])
        

    # Virtual event handlers, overide them in your derived class
    def GogekList(self, a):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = "select gogek_no, gogek_name, gogek_tel, case when SUBSTR(gogek_jumin, 8, 1) = 1 then '남' ELSE '여' \
            END AS gogek_gen from gogek inner join jikwon on gogek_damsano = jikwon_no where jikwon_no=%s"%a
            cursor.execute(sql)
            
            lists = cursor.fetchall()
            self.m_listCtrl2.DeleteAllItems()
                 
            for list in lists:
                i = self.m_listCtrl2.InsertItem(1000, 0)
                self.m_listCtrl2.SetItem(i, 0, str(list[0]))
                self.m_listCtrl2.SetItem(i, 1, list[1])
                self.m_listCtrl2.SetItem(i, 2, str(list[2]))
                self.m_listCtrl2.SetItem(i, 3, list[3])
            
            self.staCount.SetLabel(str(len(lists)))   #인원수
        except:
            pass
        finally:
            cursor.close()
            conn.close()
    
    def ClickFunc( self, event ):
        id = event.GetEventObject().id
        global rec_r
        if id == 1: # 처음으로
            rec_r = 0
        elif id == 2: # 이전으로
            rec_r -= 1
            if rec_r < 0: rec_r = 0
        elif id == 3: # 다음으로
            rec_r += 1
            if rec_r > (len(datas) - 1): rec_r = (len(datas) - 1) 
        elif id == 4: # 맨끝으로
            rec_r = (len(datas) - 1)
        
        self.ShowData()
        self.GogekList(str(rec_r + 1))        
        
if __name__ == "__main__":
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()
    
    
    