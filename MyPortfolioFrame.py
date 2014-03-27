import wx

class MyStocksPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        txt = wx.StaticText(parent, -1, "foo bar this is new", (440,100), (200,-1))
