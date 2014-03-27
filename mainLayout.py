import MyPortfolioFrame as mpf
import CreateUserFrame as cuf
import MainFrame as mf
import wx    

# Login view
class StartFrame(wx.Frame):

    def __init__ (self,parent,id):
        wx.Frame.__init__(self,parent,id,'Your Stock Portfolio',size=(1000,550))
        panel = wx.Panel(self)

        wx.StaticText(panel, -1, "Username", (440,38), (200,-1))
        self.txt_uname = wx.TextCtrl(panel, pos=(440,55), size=(180,-1))

        wx.StaticText(panel, -1, "Password", (440,83), (200,-1))
        self.txt_password = wx.TextCtrl(panel, pos=(440,100), size=(180,-1))

        btn_Login = wx.Button(panel, label="Login", pos=(440,130), size=(90,25))
        self.Bind(wx.EVT_BUTTON, self.loginBtnPressed, btn_Login)

        btn_CreateUsr = wx.Button(panel, label="Create User", pos=(532,130), size=(90,25))
        self.Bind(wx.EVT_BUTTON, self.createUsrBtnPressed, btn_CreateUsr)

    def loginBtnPressed(self, event):
        # TODO: add the login password confirmation logic here...
        mFrame = mf.mainFrame(parent=None, id=-1)
        mFrame.Show()
        self.Destroy()

    def createUsrBtnPressed(self, event):
        cFrame = cuf.createUsrFrame(parent=None, id=-1)
        cFrame.Show()
        self.Destroy()



if __name__ == '__main__':
    app = wx.App(False)
    sFrame = StartFrame(parent=None, id=-1)
    sFrame.Show()
    app.MainLoop()
