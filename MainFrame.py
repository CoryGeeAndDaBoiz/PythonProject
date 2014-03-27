import wx
import NewCompanyFrame as ncf

ID_FILE_NEW_COMP = wx.NewId()
ID_FILE_OPEN = wx.NewId()
ID_EXIT_MAIN = wx.NewId()
ID_EXIT_LOGIN = wx.NewId()

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
        self.viewStocksPanel = mpf.MyStocksPanel(self)
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
        newCompFrame = ncf.newCompanyFrame(parent=None, id=-1)
        newCompFrame.Show()

    def openfile(self, event):
        pass

    def closewindow(self, event):
        self.Destroy()
