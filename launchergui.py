import wx
import urllib.request
import os
from zipfile import ZipFile


class LauncherFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title="RoseClient Launcher")

        panel = wx.Panel(self)

        frame_sizer = wx.BoxSizer(wx.VERTICAL) 

        start_btn = wx.Button(panel, label="Start Client (1.8.8)", size=(500, 50))

        start_btn.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, 0, 90, underline=False, faceName=""))
        start_btn.SetBackgroundColour((61, 130, 219, 255))
        start_btn.SetForegroundColour((237, 237, 237, 255))

        frame_sizer.Add(start_btn, 0, wx.ALL | wx.CENTER, 5)

        start_btn.Bind(wx.EVT_BUTTON, self.on_press)
        panel.SetSizer(frame_sizer)

        self.SetSize(1280, 720)
        self.Show(True)

    def on_press(self, event):
        try:
            with ZipFile("Client Beta v1.1.zip", "r") as zipObj:
                zipObj.extractall()
            os.system("java -jar RoseClient.jar")
        except:
            print("Error: Failed to run client!")

if __name__ == "__main__":
    app = wx.App()
    frame = LauncherFrame()
    app.MainLoop()