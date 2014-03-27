import wx

ID_EXIT_CREATE_USR = wx.NewId()

# Create a new user view
class createUsrFrame(wx.Frame):
    
    def __init__(self,parent,id):        
        wx.Frame.__init__(self,parent,id,'New User Info',size=(1000,550))
        createUser_panel = wx.Panel(self)

        status = self.CreateStatusBar()

        menubar = wx.MenuBar()
        exitMenuItem = wx.Menu() # exit menu item

        wx.StaticText(createUser_panel, -1, "Username", (440,18), (200,-1))
        txt_uname = wx.TextCtrl(createUser_panel, pos=(440,35), size=(180,-1))
        self.uname = txt_uname.GetValue()

        wx.StaticText(createUser_panel, -1, "Password", (440,63), (200,-1))
        self.txt_password = wx.TextCtrl(createUser_panel, pos=(440,80), size=(180,-1))

        wx.StaticText(createUser_panel, -1, "Confirm Password", (440,106), (200,-1))
        self.txt_confirm_password = wx.TextCtrl(createUser_panel, pos=(440,123), size=(180,-1))

        # add items to fileMenuItem and exitMenuItem
        exitMenuItem.Append(ID_EXIT_CREATE_USR, "Exit", "Will exit the application")
        wx.EVT_MENU(self, ID_EXIT_CREATE_USR, self.closewindow)

        # add menus (first, second) to menubar
        menubar.Append(exitMenuItem, "Exit")
        self.SetMenuBar(menubar) # actually sets the menubar on the screen

        btn_CreateUser = wx.Button(createUser_panel, label="Create User", pos=(439,154), size=(90,25))
        self.Bind(wx.EVT_BUTTON, self.createUser, btn_CreateUser)

    def createUser(self, event):
        pw = self.txt_password.GetValue()
        cpw = self.txt_confirm_password.GetValue()
        if pw == cpw:
            dlg = wx.MessageDialog(self, 'Create User logic here!', 'User Created',
                               wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            dlg = wx.MessageDialog(self, 'Password was not confirmed', 'Error',
                               wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()        

    def closewindow(self, event):
        self.Destroy()
