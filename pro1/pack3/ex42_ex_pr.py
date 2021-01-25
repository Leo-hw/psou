
import wx
import wx.xrc
import ast
import MySQLdb

with open('mariadb.txt', mode='r') as f:
    config = ast.literal_eval(f.read())
datas=[]
rec_r = 0 

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 643,518 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"사번 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtNo = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer2.Add( self.txtNo, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"이름 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"부서명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txtBuser = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtBuser, 0, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"직급 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txtJik = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtJik, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.m_panel2, wx.ID_ANY, u"||<<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel2, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.m_panel2, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btn3, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.m_panel2, wx.ID_ANY, u">>||", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer4 )
        self.m_panel2.Layout()
        bSizer4.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstView = wx.ListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer3.Add( self.lstView, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel3.SetSizer( bSizer3 )
        self.m_panel3.Layout()
        bSizer3.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"고객 수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.staCount = wx.StaticText( self.m_panel4, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer5.Add( self.staCount, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # 컬럼 추가용.
        self.lstView.InsertColumn(0, '고객번호', width=150)
        self.lstView.InsertColumn(1, '고객명', width=150)
        self.lstView.InsertColumn(2, '고객전화', width=150)
        self.lstView.InsertColumn(3, '고객성별', width=150)
        
        # 편집 가능 여부 
        self.txtNo.Enable(enable=False)
        self.txtName.Enable(enable=False)
        self.txtBuser.Enable(enable=False)
        self.txtJik.Enable(enable=False)
        
        
        #버튼 별 id 할당해서 각각 동작에 활용하기 위함.
        self.btn1.id = 1
        self.btn2.id = 2
        self.btn3.id = 3
        self.btn4.id = 4

        # Connect Events// 이벤트 연결
        self.btn1.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btn2.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btn3.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btn4.Bind( wx.EVT_BUTTON, self.OnProcess )
        
        self.DataLoad(a)         # 데이터 불러오기
        
    def __del__( self ):
        pass
    
    def DataLoad(self, a):
        try:
            conn = MySQLdb.connect(**config)        # 마리아 디비 연결    
            cursor = conn.cursor()                          
            sql = '"select jikwon_no, jikwon_name, buser_name, jikwon_jik, gogek_no, gogek_name, gogek_tel, case when substr(gogek_jumin, 8,1) = 1 then '남' when substr(gogek_jumin, 8,1) = 2 then '여'  END as gogek_gen  FROM jikwon left join buser on buser_no = buser_num left join gogek on gogek_damsano = jikwon_no order by jikwon_no where jikwon_no=%s"%a ;
            
            cursor.execute(sql)
            #print(conn)
            
            global datas
            datas= cursor.fetchall()
            a = datas[0][0]
            
            
            #print(datas[0][0])
            #print(datas[1][0])
            print(datas[0])
            
            
            
            
            
            self.ShowData()
            
            
        except Exception as e:
            print('dataload err : ' +str(e))
        
        finally:
            cursor.close()
            conn.close()
    
    
    def ShowData(self):
        self.lstView.DeleteAllItems()
        
        
        
        self.txtNo.SetLabel(str(datas[rec_r][0]))
        self.txtName.SetLabel(datas[rec_r][1])
        self.txtBuser.SetLabel(datas[rec_r][2])
        self.txtJik.SetLabel(datas[rec_r][3])
        
        for d in datas:
            index = self.lstView.InsertItem(100, str(d[0]))
            self.lstView.SetItem(index,1,d[1])
            self.lstView.SetItem(index,2,d[2])
            self.lstView.SetItem(index,3,d[3])
        
        
        self.staCount.SetLabel(str(self.lstView.GetItemCount()))
         
    # Virtual event handlers, overide them in your derived class
    def OnProcess(self, event):
        id = event.GetEventObject().id
        #print(id)
        global rec_r
        if id ==1:   #처음
            rec_r = 0
        elif id ==2:
            rec_r = rec_r -1
            if rec_r <0:rec_r=0
        elif id ==3:
            rec_r = rec_r +1
            if rec_r > (len(datas)-1):rec_r = len(datas)-1
        elif id ==4: #끝으로 
            rec_r = len(datas) -1
        self.ShowData()
        
    
if __name__ =='__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()
    