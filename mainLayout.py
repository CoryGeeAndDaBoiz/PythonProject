<<<<<<< .merge_file_yNDQpZ
import wx
import wx.lib.scrolledpanel as sp

ID_FILE_NEW_COMP = wx.NewId()
ID_FILE_OPEN = wx.NewId()
ID_EXIT_MAIN = wx.NewId()
ID_EXIT_LOGIN = wx.NewId()
ID_EXIT_CREATE_USR = wx.NewId()


# Search for a new company by the stock symbol
class newCompanyFrame(wx.Frame):
    
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Company Search',size=(1000,550))
        new_comp_panel = wx.Panel(self)

        wx.StaticText(new_comp_panel, -1, "Sym:", (8,13), (200,-1))
        compName = wx.TextCtrl(new_comp_panel, pos=(45,10), size=(180,-1))
        btn_Search = wx.Button(new_comp_panel, label="Search", pos=(227,9), size=(90,25))




class MyStocksPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        txt = wx.StaticText(parent, -1, "foo bar this is new", (440,100), (200,-1))



# Main view the user will see
class mainFrame(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Your Portfolio',size=(1000,550))
        main_panel = wx.Panel(self)

        # create a statusbar
        status = self.CreateStatusBar()

        # creating a menu bar
        menubar = wx.MenuBar()
        fileMenuItem = wx.Menu() # one drop down for the menubar
        editMenuItem = wx.Menu() # another drop down for menubar
        exitMenuItem = wx.Menu() # exit menu item

        # add items to fileMenuItem and exitMenuItem
        # first param creats the item inside first
        # second param creates the label for the item
        # third param lets the statusbar know what it should display
        fileMenuItem.Append(ID_FILE_NEW_COMP, "Search", "Search for a new company")
        fileMenuItem.Append(ID_FILE_OPEN, "Open...", "This will open a new window")
        exitMenuItem.Append(ID_EXIT_MAIN, "Exit", "Will exit the current window")

        # add menus (first, second) to menubar
        # first param the item you want to add the menubar
        # second param the label for the item in the menubar
        menubar.Append(fileMenuItem, "File")
        menubar.Append(editMenuItem, "Edit")
        menubar.Append(exitMenuItem, "Exit")
        self.SetMenuBar(menubar) # actually sets the menubar on the screen

        # setting up the events for the menu items
        wx.EVT_MENU(self, ID_FILE_NEW_COMP, self.newcompany)
        wx.EVT_MENU(self, ID_FILE_OPEN, self.openfile)
        wx.EVT_MENU(self, ID_EXIT_MAIN, self.closewindow)


        btn_viewStocks = wx.Button(main_panel, label="My Stocks", pos=(0,0), size=(90,25))
        self.Bind(wx.EVT_BUTTON, self.viewStocksPressed, btn_viewStocks)
        
        btn_foo = wx.Button(main_panel, label="Another", pos=(90,0), size=(90,25))
        self.Bind(wx.EVT_BUTTON, self.fooPressed, btn_foo)
        
        btn_boo = wx.Button(main_panel, label="Boo", pos=(180,0), size=(90,25))
        self.Bind(wx.EVT_BUTTON, self.booPressed, btn_boo)

    def viewStocksPressed(self, event):
        self.viewStocksPanel = MyStocksPanel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.viewStocksPanel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    def fooPressed(self, event):
        dlg = wx.MessageDialog(self, 'another panel will be here', 'foo',
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def booPressed(self, event):
        dlg = wx.MessageDialog(self, 'another panel will be here', 'boo',
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def newcompany(self, event):
        newCompFrame = newCompanyFrame(parent=None, id=-1)
        newCompFrame.Show()

    def openfile(self, event):
        pass

    def closewindow(self, event):
        self.Destroy()


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
    
=======
import MyPortfolioFrame as mpf
import CreateUserFrame as cuf
import MainFrame as mf
import wx    
>>>>>>> .merge_file_2TmOrO

# Login view
class startFrame(wx.Frame):

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
<<<<<<< .merge_file_yNDQpZ
        mFrame = mainFrame(parent=None, id=-1)
=======
        mFrame = mf.mainFrame(parent=None, id=-1)
>>>>>>> .merge_file_2TmOrO
        mFrame.Show()
        self.Destroy()

    def createUsrBtnPressed(self, event):
<<<<<<< .merge_file_yNDQpZ
        cFrame = createUsrFrame(parent=None, id=-1)
=======
        cFrame = cuf.createUsrFrame(parent=None, id=-1)
>>>>>>> .merge_file_2TmOrO
        cFrame.Show()
        self.Destroy()



if __name__ == '__main__':
    app = wx.App(False)
    sFrame = startFrame(parent=None, id=-1)
    sFrame.Show()
    app.MainLoop()
