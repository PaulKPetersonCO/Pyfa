from gui.contextMenu import ContextMenu
from gui.itemStats import ItemStatsDialog
import eos.types
import gui.mainFrame
import service
import gui.globalEvents as GE
import wx

class ChangeAmount(ContextMenu):
    def __init__(self):
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()

    def display(self, srcContext, selection):
        return srcContext in ("cargoItem","projectedFit","fighterItem","projectedFighter")

    def getText(self, itmContext, selection):
        return "Change {0} Quantity".format(itmContext)

    def activate(self, fullContext, selection, i):
        srcContext = fullContext[0]
        dlg = AmountChanger(self.mainFrame, selection[0], srcContext)
        dlg.ShowModal()

ChangeAmount.register()

class AmountChanger(wx.Dialog):

    def __init__(self, parent, thing, context):
        wx.Dialog.__init__(self, parent, title="Select Amount", size=wx.Size(220, 60))
        self.thing = thing
        self.context = context

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.input = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)

        bSizer1.Add(self.input, 1, wx.ALL, 5)
        self.input.Bind(wx.EVT_CHAR, self.onChar)
        self.input.Bind(wx.EVT_TEXT_ENTER, self.change)
        self.button = wx.Button(self, wx.ID_OK, u"Done")
        bSizer1.Add(self.button, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)
        self.button.Bind(wx.EVT_BUTTON, self.change)

    def change(self, event):
        sFit = service.Fit.getInstance()
        mainFrame = gui.mainFrame.MainFrame.getInstance()
        fitID = mainFrame.getActiveFit()

        if isinstance(self.thing, eos.types.Cargo):
            sFit.addCargo(fitID, self.thing.item.ID, int(self.input.GetLineText(0)), replace=True)
        elif isinstance(self.thing, eos.types.Fit):
            sFit.changeAmount(fitID, self.thing, int(self.input.GetLineText(0)))
        elif isinstance(self.thing, eos.types.Fighter):
            sFit.changeActiveFighters(fitID, self.thing, int(self.input.GetLineText(0)))

        wx.PostEvent(mainFrame, GE.FitChanged(fitID=fitID))

        event.Skip()
        self.Close()

    ## checks to make sure it's valid number
    def onChar(self, event):
        key = event.GetKeyCode()

        acceptable_characters = "1234567890"
        acceptable_keycode    = [3, 22, 13, 8, 127] # modifiers like delete, copy, paste
        if key in acceptable_keycode or key >= 255 or (key < 255 and chr(key) in acceptable_characters):
            event.Skip()
            return
        else:
            return False

