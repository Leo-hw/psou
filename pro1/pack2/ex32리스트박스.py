# ListCtrl 컴포넌트로 데이터 출력

fdatas = [
    ('홍길동', '서울','1999'),
    ('김치국', '인천','1995'),
]


import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, size = (300,250))
        
        self.m_list = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        
        self.m_list.InsertColumn(0, '이름', width=80)    # 컬럼 추가
        self.m_list.InsertColumn(0, '주소', width=120)
        self.m_list.InsertColumn(0, '출생년도', width=80)
        
        tu = ('공기밥', '수원', '1996')
        fdatas.append(tu)
        for f in fdatas:
            index = self.m_list.InsertItem(1000, f[0])
            self.m_list.SetItem(index, 1, f[1])
            self.m_list.SetItem(index, 2, f[2])
            
        
        self.Centre()
        
if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, -1, 'Test').Show()
    app.MainLoop()