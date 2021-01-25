# 레이아웃 매니저 클래스 중 Sizer 연습
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent,title):
        #wx.Frame.__init__(self, parent, title, size = (300,250))
        super(MyFrame, self).__init__(parent, title=title, size = (300,250))
        
        panel1 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        panel2 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        
        panel1.SetBackgroundColour('BLUE')
        panel2.SetBackgroundColour('red')
        
        boxLayout = wx.BoxSizer(wx.VERTICAL)
        boxLayout.Add(panel1, 3, wx.EXPAND) #3/4 영역 확보
        boxLayout.Add(panel2, 1, wx.EXPAND) #1/4 영역 확보
        
        self.SetSizer(boxLayout)
        self.Center()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, title='레이아웃 연습').Show()
    app.MainLoop()
    