#!/usr/bin/env python3

#width = 1080
#height = 1220
#from kivy.config import Config
#Config.set('graphics', 'width', width)
#Config.set('graphics', 'height', height)

from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.list import TwoLineListItem
from AppBackend import AppLogic


class ListItemWithData(TwoLineListItem):
    def __init__(self, data, **kwargs):
        super(ListItemWithData,self).__init__(**kwargs)
        self.DataHolder = data


class PastebinApp(MDApp):
    def __init__(self):
        super(PastebinApp,self).__init__()
        self.Backend = AppLogic()
        self.menuList = [{"viewclass": "OneLineListItem", "text": "archive", "on_release": lambda x='archive': self.MenuLangCallback(x)},
                         {"viewclass": "OneLineListItem", "text": "Python", "on_release": lambda x="python": self.MenuLangCallback(x),},
                         {"viewclass": "OneLineListItem", "text": "C#", "on_release": lambda x='csharp': self.MenuLangCallback(x),},
                         {"viewclass": "OneLineListItem", "text": "C", "on_release": lambda x='c': self.MenuLangCallback(x),},
                         {"viewclass": "OneLineListItem", "text": "C++", "on_release": lambda x='cpp': self.MenuLangCallback(x),},
                         {"viewclass": "OneLineListItem", "text": "Java", "on_release": lambda x='java': self.MenuLangCallback(x),},
                         {"viewclass": "OneLineListItem", "text": "Lua", "on_release": lambda x='lua': self.MenuLangCallback(x),},
                         {"viewclass": "OneLineListItem", "text": "html 5", "on_release": lambda x='html5': self.MenuLangCallback(x),},
                         {"viewclass": "OneLineListItem", "text": "Json", "on_release": lambda x='json': self.MenuLangCallback(x),},
                         {"viewclass": "OneLineListItem", "text": "Bash", "on_release": lambda x='bash': self.MenuLangCallback(x),},
                         {"viewclass": "OneLineListItem", "text": "JS", "on_release": lambda x='javascript': self.MenuLangCallback(x),},
                         ]

        self.AboutList = [{"viewclass": "OneLineListItem", "text": "Reload","on_release": lambda x='Reload': self.AboutMenuItemClicked(x),},
                          #{"viewclass": "OneLineListItem", "text": "Save Text","on_release": lambda x='Save': self.AboutMenuItemClicked(x),},
                          {"viewclass": "OneLineListItem", "text": "About","on_release": lambda x='About': self.AboutMenuItemClicked(x),}]
        self.AllData = None
        self.Url = None

    def built(self):
        return

    def AboutMenuItemClicked(self, obj):
        if obj == "About":
            self.root.current = 'about'
        if obj == "Reload":
            sb = Snackbar(text="Data has been updated")
            sb.open()
            self.AllData = self.Backend.GetAllData()
        if obj == "Save":
            # TODO: save file  
            tb = self.root.ids.textbox
            print(tb.text)
        self.MenuAbout.dismiss()
    
    def MenuAboutCallback(self, widgetObj):
        self.MenuAbout = MDDropdownMenu(caller=widgetObj, items=self.AboutList, width_mult=4,)
        self.MenuAbout.open()

    def callbackItem(self, obj):
        self.root.current = 'reader'
        tmpText = self.Backend.GetRawData(obj.DataHolder['Url'])
        if tmpText == None:
            sb = Snackbar(text="Error: Could not get text for pastebin.com")
            sb.open()
        else:
            textbox = self.root.ids.textbox
            textbox.text = tmpText
    

    def NavigationBack(self, obj):
        self.root.current = 'main'

    def MenuLangCallback(self, name):
        self.MenuLang.dismiss()
        self.root.ids.myListWidget.clear_widgets()
        for itemDict in self.AllData[name]:
            self.root.ids.myListWidget.add_widget(ListItemWithData(itemDict, secondary_text=f"{itemDict['Syntax']}", text=f"{itemDict['Title']}", on_release=self.callbackItem))


    def on_start(self, **kwargs):
        self.MenuLang = MDDropdownMenu(caller=self.root.ids.drop_item, items=self.menuList, width_mult=4,ver_growth=None)
        sb = Snackbar(text="Downloaded data")
        sb.open()
        self.UpdateCallback()
        

    def UpdateCallback(self, obj=None):
        #self.Backend.Run() 
        #self.AllData = self.Backend.Data
        self.AllData = self.Backend.GetAllData()
        for itemDict in self.AllData['archive']:
            self.root.ids.myListWidget.add_widget(ListItemWithData(itemDict, secondary_text=f"{itemDict['Syntax']}", text=f"{itemDict['Title']}", on_release=self.callbackItem))


if __name__ == '__main__':
    PastebinApp().run()
                                                                                                                                                            ##typing_extensions