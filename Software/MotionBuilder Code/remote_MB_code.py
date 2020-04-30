###Import the Python telnet library
##import telnetlib
##import time
###Create a telnet console to your PC (127.0.0.1) and MotionBuilder (4242)
##host = telnetlib.Telnet('127.0.0.1', 4242)
## 
###Find the prompt, so you can enter a command (seriously)
##host.read_until('>>>', 5)
##
###Create a null called 'locator'
##host.write('myCube = FBModelCube("cube")\n')
##host.replace.write('myCube2 = FBModelCube("c3ube")\n')
##
###Close the terminal
##host.close()

import wx
import telnetlib
import pdb

host = telnetlib.Telnet("127.0.0.1", 4242)
#pdb.set_trace()
def mbPipe(command):
    host.read_until('>>>', .01)
    #write the command
    host.write(command + '\n')
    #read all data returned
    raw = str(host.read_until('>>>', .1))
    #removing garbage i don't want
    raw = raw.replace('\n\r>>>','')
    raw = raw.replace('\r','')
    rawArr = raw.split('\n')
    #cleanArr = 
    return rawArr
    
class MyFrame(wx.Frame):

    def __init__(self):
        # create a frame, no parent, default to wxID_ANY
        wx.Frame.__init__(self, None, wx.ID_ANY, 'mbUI test',pos=(200, 150),size=(175,280))

        #create listbox
        self.selListBox = wx.ListBox(self, -1, choices=[],pos=(8,38),size=(150, 145))
        self.selListBox.Bind(wx.EVT_LISTBOX, self.selListBoxChange)

        #create model metadata
        self.translationLabel = wx.StaticText(self,-1,'Pos:',pos=(8,185))
        self.rotationLabel = wx.StaticText(self,-1,'Rot:',pos=(8,200))

        #make buttons
        self.selItems = wx.Button(self, id=-1,label='Get Selected Items',pos=(8, 8),size=(150, 28))
        self.selItems.Bind(wx.EVT_BUTTON, self.selItemsClick)
        self.selItems.SetToolTip(wx.ToolTip("Gets all 'models' selected in Motion Builder"))

        self.delItems = wx.Button(self, id=-1,label='Delete This Model',pos=(8, 217),size=(150, 28))
        self.delItems.Bind(wx.EVT_BUTTON, self.delItemsClick)
        self.delItems.SetToolTip(wx.ToolTip("Will delete selected models"))

        # show the frame
        self.Show(True)
   

    def selItemsClick(self,event):
        mbPipe("selectedModels = FBModelList()")
        mbPipe("FBGetSelectedModels(selectedModels,None,True)")
        self.selListBox.Set([])
        for item in (mbPipe("for item in selectedModels: print item.Name")):
                self.selListBox.Append(item)

    def delItemsClick(self,event):
        mbPipe('FBFindModelByName("' + str(self.selListBox.GetStringSelection()) + '").FBDelete()')
        mbPipe("selectedModels = FBModelList()")
        mbPipe("FBGetSelectedModels(selectedModels,None,True)")
        self.selListBox.Set([])
        for item in (mbPipe("for item in selectedModels: print item.Name")):
                self.selListBox.Append(item)

    def selListBoxChange(self,event):
        trans = mbPipe('FBFindModelByName("' + str(self.selListBox.GetStringSelection()) + '").Translation')
        rot = mbPipe('FBFindModelByName("' + str(self.selListBox.GetStringSelection()) + '").Rotation')
        self.translationLabel.SetLabel(('Pos: ' + trans))
        self.rotationLabel.SetLabel(('Rot: ' + rot))

application = wx.PySimpleApp()
window = MyFrame()
application.MainLoop()
