#테이블 자료에 대해 레코드를 이동하며 출력
# import wx
# import wx.xrc
# import ast
# import MySQLdb
# 
# with open('mariadb.txt', mode='r') as f:
#     config = ast.literal_eval(f.read())
#     #print(config)
#     
# 
# datas=[]
# rec_r = 0 
# 
# 
# class MyFrame ( wx.Frame ):
#     
#     def __init__( self, parent ):
#         wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
#         
#         bSizer1 = wx.BoxSizer( wx.VERTICAL )
#         
#         self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#         bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
#         
#         self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"번호 :", wx.DefaultPosition, wx.DefaultSize, 0 )
#         self.m_staticText2.Wrap( -1 )
#         bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
#         
#         self.txtCode = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
#         bSizer2.Add( self.txtCode, 0, wx.ALL, 5 )
#         
#         self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"상품명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
#         self.m_staticText3.Wrap( -1 )
#         bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
#         
#         self.txtSang = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
#         bSizer2.Add( self.txtSang, 0, wx.ALL, 5 )
#         
#         
#         self.m_panel1.SetSizer( bSizer2 )
#         self.m_panel1.Layout()
#         bSizer2.Fit( self.m_panel1 )
#         bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
#         
#         self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#         bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
#         
#         self.btn1 = wx.Button( self.m_panel2, wx.ID_ANY, u"||<<", wx.DefaultPosition, wx.DefaultSize, 0 )
#         bSizer3.Add( self.btn1, 0, wx.ALL, 5 )
#         
#         self.btn2 = wx.Button( self.m_panel2, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
#         bSizer3.Add( self.btn2, 0, wx.ALL, 5 )
#         
#         self.btn3 = wx.Button( self.m_panel2, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
#         bSizer3.Add( self.btn3, 0, wx.ALL, 5 )
#         
#         self.btn4 = wx.Button( self.m_panel2, wx.ID_ANY, u">>||", wx.DefaultPosition, wx.DefaultSize, 0 )
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
#         bSizer3.Add( self.btn4, 0, wx.ALL, 5 )
#         
#         
#         self.m_panel2.SetSizer( bSizer3 )
#         self.m_panel2.Layout()
#         bSizer3.Fit( self.m_panel2 )
#         bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
#         
#         
#         self.SetSizer( bSizer1 )
#         self.Layout()
#         
#         self.Centre( wx.BOTH )
#         
#         #버튼에 이벤트 핸들러 장착
#         self.btn1.id = 1
#         self.btn2.id = 2
#         self.btn3.id = 3
#         self.btn4.id = 4
#         
#         self.btn1.Bind(wx.EVT_BUTTON, self.ButtonProcess)
#         self.btn2.Bind(wx.EVT_BUTTON, self.ButtonProcess)
#         self.btn3.Bind(wx.EVT_BUTTON, self.ButtonProcess)
#         self.btn4.Bind(wx.EVT_BUTTON, self.ButtonProcess)
#         
#         self.DataLoad()
#         
#         
#         self.txtCode.Enable(False)
#         self.txtSang.Enable(False)
#         #self.txtCode.SetEditable(editable=False)
#         #self.txtSang.SetEditable(editable=False)
#     
#     def __del__( self ):
#         pass
#     
#     def DataLoad(self):
#         try:
#             conn = MySQLdb.connect(**config)
#             cursor = conn.cursor()
#             
#             sql = "select * from sangdata"
#             cursor.execute(sql)          
#             
#             global datas
#             datas = cursor.fetchall()
#             print(datas)
#             print(datas[0][0],datas[0][1])
#             
#             self.ShowData()
#         except Exception as e:
#             print('DataLoad err : ' + str(e))
#         finally:
#             cursor.close()
#             conn.close()
#     
#     def ButtonProcess(self, event):
#         id = event.GetEventObject().id
#         
#         global rec_r
#         
#         if id == 1: #처음으로 
#             rec_r = 0
#         elif id == 2:   #이전으로
#             rec_r = rec_r -1
#             if rec_r < 0 : rec_r = 0
#         elif id == 3:   #다음으로
#             rec_r = rec_r + 1
#             if rec_r > len(datas)-1: rec_r = len(datas)-1
#         elif id == 4:   #끝으로
#             rec_r = len(datas)-1 
#         self.showData()    
#         
#     def ShowData(self):
#         self.txtCode.SetLabel(str(datas[rec_r][0]))
#         self.txtSang.SetLabel(datas[rec_r][1])
#         
#         
#     
# if __name__ == '__main__':
#     app = wx.App()
#     MyFrame(None).Show()
#     app.MainLoop()


# 테이블 자료에 대해 케로드를 이용해 

import wx
import wx.xrc
import ast
import MySQLdb

with open('mariadb.txt', mode='r') as f:
    config = ast.literal_eval(f.read())
datas=[]
rec_r = 0 
print(config)
class MyFrame3 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText14 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"번호:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        bSizer10.Add( self.m_staticText14, 0, wx.ALL, 5 )
        
        self.txtCode = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.txtCode, 0, wx.ALL, 5 )
        
        self.m_staticText15 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"상품명", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        bSizer10.Add( self.m_staticText15, 0, wx.ALL, 5 )
        
        self.txtSang = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.txtSang, 0, wx.ALL, 5 )
        
        
        self.m_panel7.SetSizer( bSizer10 )
        self.m_panel7.Layout()
        bSizer10.Fit( self.m_panel7 )
        bSizer9.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.m_panel8, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel8, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.m_panel8, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btn3, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.m_panel8, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        self.m_panel8.SetSizer( bSizer11 )
        self.m_panel8.Layout()
        bSizer11.Fit( self.m_panel8 )
        bSizer9.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer9 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        #self.txtCode.SetEditable(False)
        self.txtCode.Enable(enable=False)
        self.txtSang.Enable(enable=False)
        
        # 버튼에 이벤트 핸들러 장착
        self.btn1.id =1
        self.btn2.id =2
        self.btn3.id =3
        self.btn4.id =4
        
        self.btn1.Bind(wx.EVT_BUTTON, self.ButtonProcess)
        self.btn2.Bind(wx.EVT_BUTTON, self.ButtonProcess)
        self.btn3.Bind(wx.EVT_BUTTON, self.ButtonProcess)
        self.btn4.Bind(wx.EVT_BUTTON, self.ButtonProcess)
        
        self.DataLoad()
        
    def __del__( self ):
        pass
    def DataLoad(self):
        try:
            conn= MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from sangdata"
            cursor.execute(sql)
            
            global datas
            datas = cursor.fetchall()
            #print(datas[0])
            #print(datas[0][0], datas[0][1])
            self.ShowData()
        except Exception as e:
            print('DataLoad err: '+ str(e))
        finally:
            cursor.close()
            conn.close()
    
    def ShowData(self):     
        self.txtCode.SetLabel(str(datas[rec_r][0]))
        self.txtSang.SetLabel(datas[rec_r][1])
        
    def ButtonProcess(self,event):       
        id = event.GetEventObject().id
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
if __name__ == '__main__':
    app = wx.App()
    MyFrame3(None).Show()
    app.MainLoop()