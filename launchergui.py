import wx
import urllib.request
import os
from zipfile import ZipFile

class LauncherFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title="RoseClient Launcher")
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)   
        my_btn = wx.Button(panel, label="Start Client (1.8.8)")
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)   
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        panel.SetSizer(my_sizer)        
        self.Show()
    
    def on_press(self, event):
        with ZipFile("Client Beta v1.0.zip", "r") as zipObj:
            zipObj.extractall()
        os.system("java -jar RoseClient.jar");

if __name__ == "__main__":
    app = wx.App()
    frame = LauncherFrame()
    app.MainLoop()