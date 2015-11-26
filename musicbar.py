import wx
import pygame
import os
import random
import time
class IsPrimeFrame(wx.Frame):
    def __init__(self,superion,count=0):
        wx.Frame.__init__(self,parent=superion ,title='Big Eye',size = (400,200))
        self.count=count
        panel = wx.Panel(self)
        panel.SetBackgroundColour('Red')
        self.buttonPlay = wx.Button(parent=panel,label='PLAY',pos=(50,90))
        self.Bind(wx.EVT_BUTTON,self.OnbuttonPlay,self.buttonPlay)

        self.buttonPause = wx.Button(parent=panel,label='Pause',pos=(150,90))
        self.Bind(wx.EVT_BUTTON,self.OnbuttonPause,self.buttonPause)

        self.buttonQuit = wx.Button(parent=panel,label='Quit',pos=(250,90))
        self.Bind(wx.EVT_BUTTON,self.OnbuttonQuit,self.buttonQuit)
    def OnbuttonPlay(self,even):
        folder = r'd:\music'
        musics = [folder+'\\'+music for music in os.listdir(folder) if music.endswith('.mp3')]
        pygame.mixer.init()
        total =len(musics)
        if not pygame.mixer.music.get_busy():
            playMusic = random.choice(musics)
            pygame.mixer.music.load(playMusic)
            pygame.mixer.music.play(1)
            print 'playing...',playMusic
        else:
            time.sleep(1)
    def OnbuttonPause(self,even):
        if self.count%2 ==0:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.count = self.count+1
    def OnbuttonQuit(self,even):
        dlg = wx.MessageDialog(self,'Really Quit?','Caution',wx.CANCEL|wx.OK|wx.ICON_QUESTION)
        if dlg.ShowModal() ==wx.ID_OK:
            self.Destroy()
if __name__ == '__main__':
    aa = wx.App()
    frame = IsPrimeFrame(None)
    frame.Show()
    aa.MainLoop()

