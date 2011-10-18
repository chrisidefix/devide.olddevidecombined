import wx
import wx.aui

def main():
    app = wx.PySimpleApp()

    frame = wx.Frame(None, -1, "AUI Ordering Problem", size=(400,400))
    mgr = wx.aui.AuiManager()
    mgr.SetManagedWindow(frame)

    mgr.AddPane(wx.StaticText(frame, -1, 
    'Windows: Top Left\nLinux: Bottom Left'), 
            wx.aui.AuiPaneInfo().
            Name('top_left').Caption('Top Left').Left())

    mgr.AddPane(wx.StaticText(frame, -1, 
        'Windows: Bottom Left\nLinux: Top Left'), 
            wx.aui.AuiPaneInfo().
            Name('bottom_left').Caption('Bottom Left').Left())


    mgr.AddPane(wx.StaticText(frame, -1, 'HEEEEELP!'), 
            wx.aui.AuiPaneInfo().
            Name('center').Caption('Center').Center())

    mgr.Update() 

    frame.Show()

    app.MainLoop()



if __name__ == '__main__':
    main()

