import wx

# Search for a new company by the stock symbol
class newCompanyFrame(wx.Frame):
    
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Company Search',size=(1000,550))
        new_comp_panel = wx.Panel(self)

        wx.StaticText(new_comp_panel, -1, "Sym:", (8,13), (200,-1))
        compName = wx.TextCtrl(new_comp_panel, pos=(45,10), size=(180,-1))
        btn_Search = wx.Button(new_comp_panel, label="Search", pos=(227,9), size=(90,25))
