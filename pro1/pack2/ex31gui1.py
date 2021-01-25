#GUI ( 프레임을 통해  결과를 출력) / 윈도우 프로그래밍 - wxPython
import wx

class Ex(wx.Frame):
    def __init__(self, parent, title):
        super(Ex, self).__init__(parent, title = title, size =(300,300))
        
        #TextBox
        #self.txtA = wx.TextCtrl(self)
        #self.txtA = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        
        self.CreateStatusBar()
        self.SetStatusText('Hello')
        
        # 메뉴
        menuBar = wx.MenuBar()
        
        mnuFile = wx.Menu()
        
        mnuNew = mnuFile.Append(wx.ID_NEW, 'New', '새글')
        mnuOpen = mnuFile.Append(wx.ID_OPEN, '&Open...\tCtrl-o', '열기')
        mnuFile.AppendSeparator()
        mnuExit = mnuFile.Append(wx.ID_EXIT, 'Exit', '종료')
        
        menuBar.Append(mnuFile, '&File')
        self.SetMenuBar(menuBar)                # Frame 에 menuBar를 장착
        
        #메뉴에 이벤트 장착
        self.Bind(wx.EVT_MENU, self.OnEvent1, mnuNew)
        self.Bind(wx.EVT_MENU, self.OnEvent2, mnuOpen)
        self.Bind(wx.EVT_MENU, self.OnEvent3, mnuExit)
        
        # 라벨과 텍스트박스 특정 위치에 등록/label & textbox
        panel = wx.Panel(self)
        wx.StaticText(panel, label = 'i d : ', pos = (5, 5))
        wx.StaticText(panel, label = 'pwd : ', pos = (5, 40))
        self.txtA = wx.TextCtrl(panel, pos=(40, 5))
        self.txtB = wx.TextCtrl(panel, pos=(40, 40), size = (200, -1))
        
        #버튼 등록
        btn1 = wx.Button(panel, label = '일반버튼', pos = (5, 100))             #얘는 현재 메소드 내에서만 부름
        btn2 = wx.ToggleButton(panel, label = '토글버튼', pos = (100, 100))
        btn3 = wx.Button(panel, label = '종료', pos = (200, 100))
        
#         #버튼에 이벤트 장착 1.     -          각각의 버튼에 이벤트 핸들러를 매핑
#         btn1.Bind(wx.EVT_BUTTON, self.OnClick1)
#         btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClick2)
#         btn3.Bind(wx.EVT_BUTTON, self.OnClick3)
        
        #버튼에 이벤트 장착 2.        -         모든 버튼에 이벤트 핸들러는 하나로 매핑
        btn1.id = 1; btn2.id = 2; btn3.id = 3;  #id는 동적, 변경 가능//
        btn1.Bind(wx.EVT_BUTTON, self.OnHanaro)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnHanaro)
        btn3.Bind(wx.EVT_BUTTON, self.OnHanaro)
        
        
        
        
        self.Center()
        self.Show()
        
    def Abc(self):      #일반 메소드
        print('이건 메소드')
    
    def OnEvent1(self, event):      #이벤트 핸들러 메소드
        #대화상자
        msgDial = wx.MessageDialog(self, '메세지', '제목', wx.OK)
        msgDial.ShowModal()
        msgDial.Destroy()
        
        self.Abc()      # Modal 창이 종료되면 수행
    
    def OnEvent2(self, event):      
        print('열기 메뉴 누름')
    
    def OnEvent3(self, event):      
        self.Close(True)        # Frame 닫기
        
    def OnClick1(self, event):
        self.SetTitle('버튼 1 클릭')
    
    def OnClick2(self, event):
        print(event.GetEventObject().GetValue())
        if event.GetEventObject().GetValue() :
            self.txtA.SetLabelText('kbs')
            self.txtB.SetLabelText('9')
        else:
            self.txtA.SetLabelText('')
            self.txtB.SetLabelText('')
    def OnClick3(self, event):
        self.SetTitle('버튼 3 클릭')
    
    def OnHanaro(self, event):
        #print('ok')
        #print(event.GetEventObject().id)
        if event.GetEventObject().id == 1:
            self.txtA.SetLabelText('첫번째 버튼')
        elif event.GetEventObject().id == 2:
            self.txtB.SetLabelText('두번째 버튼')
        else:
            self.Close(True)
            
             
if __name__ == '__main__':
    app = wx.App()
    Ex(None, title = '제목')
    app.MainLoop()
        
        

