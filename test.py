from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.filechooser import FileChooser
from kivy.uix.image import Image

from obrabot import *



Window.clearcolor = (1, 1, 1, 1)
sm = ScreenManager()
Builder.load_string("""
<ScreenMain>

    AnchorLayout:
        anchor_x: "right"
        anchor_y: "bottom"
        padding: 10
        
        Button:
            id: num
            multiline: False
            text: "дальше"
            background_color: 0, 1.5, 3, 1
            size_hint: .1, 0.1
            on_press: 
                root.manager.current = 'config2'
                root.calling()
            
    AnchorLayout:
        anchor_x: "center"
        anchor_y: "bottom"
        padding: 10
        
        Button:
            id: file    
            multiline: False
            text: "Выберите файл \\nдля визуализации"
            background_color: 0, 1.5, 3, 1
            size_hint: .2, 0.1
            on_press: 
                root.manager.current = 'config2'
                   
                      
    BoxLayout:
        orientation: "vertical"
        
        Label:
            text: 'Настройка использования '
            size_hint: [1, .01]
            color: [0, 0, 0, 1]
        
        GridLayout:
            cols: 3
            size_hint: [1, .02]
            spacing: [25]
            
            Label:
                text: ('Введите название \\nвизуализации  ')
                size_hint: [1, .04]
                color: [0, 0, 0, 1]
            
            TextInput:
                id: name
                multiline: False
                font_size: 17
                size_hint: [1, .04]
                background_color: [1, 1, 1, .7]
                input_filter: 'int'
            
            Label:
                text: ''
                size_hint: [1, .04]
                
            Label:
                text: ('Введите количество \\nблоков визуализации  ')
                size_hint: [1, .04]
                color: [0, 0, 0, 1]
            
            TextInput:
                id: inpt
                multiline: False
                font_size: 17
                size_hint: [1, .04]
                background_color: [1, 1, 1, .7]
                input_filter: 'int'
            
            Label:
                text: ''
                size_hint: [1, .04]
                
        Label:
            text: ''
            size_hint: [1, .1]
            

""")
class ScreenMain(Screen):
    def pars(self, text):
        print(sm.get_screen('config2').ada)

        sm.get_screen('config2').ada = text

        print(sm.get_screen('config2').ada)
    def calling(self):
        sm.get_screen('config2').output_()
class ScreenConfig(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        al = AnchorLayout(anchor_x = "left", anchor_y = "bottom", padding = [10])
        print(get_event())
        self.btn = Button(
                text= "назад",
                background_color= [0, 1.5, 3, 1],
                size_hint= [.1, 0.1],
                on_press = self.back,)
        ad = self.btn.text
        al.add_widget(self.btn)
        al1 = AnchorLayout(anchor_x="right", anchor_y="bottom", padding=[10])
        self.btn = Button(
            text="Далее",
            background_color=[0, 1.5, 3, 1],
            size_hint=[.1, 0.1],
            on_press=self.next, )
        ad = self.btn.text
        al1.add_widget(self.btn)
        self.bl = BoxLayout(orientation = 'vertical' )

        kol = Label(text='Напишите название блоков', color=[0, 0, 0, 1], size_hint = [1, .1])
        self.bl.add_widget(kol)
        self.gl = GridLayout(cols = 3, size_hint = [1, .5],padding = [50])


        self.add_widget(self.bl)
        self.add_widget(al)
        self.add_widget(al1)
        self.what_visual = []
    def back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'config1'
    def next(self, *args):
        self.manager.current = 'config3'
        sm.get_screen('config3').visual()
    def determine_visual(self, what_visual, num, event):
        if what_visual[num][event] == False:
            what_visual[num][event] = True
        else:
            what_visual[num][event] = False
        print(what_visual)
        return what_visual


    def output_(self):

        for i in range(int(sm.get_screen('config1').ids.inpt.text)):

            opr_dict = {}
            for ev in get_event():
                opr_dict[ev] = False
            self.what_visual.append(opr_dict)
            kol = Label(text='Напишите название блоков', color=[0, 0, 0, 1], size_hint=[1, .1], )
            self.gl.add_widget(kol)
            self.kol = TextInput(
                multiline=False,
                font_size=17, size_hint=[1, .12],
                background_color=[1, 1, 1, .7])
            self.gl.add_widget(self.kol)
            dropdown = DropDown()
            mas = []

            for index in get_event():
                btn1 = ToggleButton(text=f'{index}', group=f'{index}-{i}', size_hint_y=None, height=23, )
                btn1.bind(on_release=lambda btn1: dropdown.select([int(btn1.group[-1]), btn1.text]))
                dropdown.add_widget(btn1)
            mainbutton = Button(text='Выберете элемент визуализации', size_hint=(1, 1),  background_color=[0, 1.5, 3, 1], )
            mainbutton.bind(on_release=dropdown.open)
            dropdown.bind(on_select=lambda instance, x: self.determine_visual(self.what_visual, x[0], x[1]))
            # dropdown.bind(on_select=lambda instance, x: print(self.gl.children[::-1][(x[0] * 3) + 1].text, x[1]))
            # dropdown.select(int(btn1.group[-1]))
            self.gl.add_widget(mainbutton)
        print(self.gl.children)

        self.bl.add_widget(self.gl)
        kol = Label(text=f'', color=[0, 0, 0, 1])
        # self.determine_visual(what_visual)
        self.bl.add_widget(kol)

    def calling(self):
        sm.get_screen('config3')

    def get_data(self, ind):
        mas = []
        mas.append(ind)
        print(mas)

class Screenvisual(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        al = AnchorLayout(anchor_x="left", anchor_y="bottom", padding=[10])
        print(get_event())
        self.btn = Button(
            text="назад",
            background_color=[0, 1.5, 3, 1],
            size_hint=[.1, 0.1],
             )
        al.add_widget(self.btn)
        self.add_widget(al)

    def click(self, mainbutton1):
        mainbutton1 = [mainbutton1]
        a = sm.get_screen('config2').what_visual
        print(mainbutton1, 'ada')
        for block_visual in range(int(sm.get_screen('config1').ids.inpt.text)):
            b = []
            for i in a[block_visual]:
                if a[block_visual][i] == False:
                    b.append(i)
            for i in b:
                a[block_visual].pop(i)
            work(mainbutton1[:1], a[block_visual], block_visual)
            print(a)
            self.gl = GridLayout(cols=4, padding=[50])
            kol = Label(text='название ', color=[0, 0, 0, 1], size_hint=[.05, .1])
            self.gl.add_widget(kol)
            for img in range(3, 6):
                im = Image(source=f"source/img_{mainbutton1[0]}-{img}-{block_visual}.png", )
                self.gl.add_widget(im)
            self.bl.add_widget(self.gl)
        self.add_widget(self.bl)
    def visual(self):
        self.al = AnchorLayout(anchor_x="center", anchor_y="top", padding=[10])
        self.bl = BoxLayout(orientation='vertical')
        self.gl_vis = GridLayout(cols=2, size_hint=[1, .2], padding=[50])

        dropdown1 = DropDown()

        kol = Label(text='выберите студента ', color=[0, 0, 0, 1], size=[700, 80])
        self.gl_vis.add_widget(kol)

        for index in get_user():
            btn = Button(text=f'{index}', size_hint_y=None, height=23)
            btn.bind(on_release=lambda btn: dropdown1.select(btn.text))
            dropdown1.add_widget(btn)
        mainbutton1 = Button(text='Выберите студента',  size_hint=(None, None), background_color=[0, 1.5, 3, 1], size = [180, 40])
        mainbutton1.bind(on_release=dropdown1.open)
        dropdown1.bind(on_select=lambda instance, x: self.click(x))
        self.gl_vis.add_widget(mainbutton1)
        self.al.add_widget(self.gl_vis)
        self.add_widget(self.al)



        print(sm.get_screen('config2').what_visual)



class PaswordingApp(App):
    def build(self):
        sm.add_widget(ScreenMain(name='config1'))
        sm.add_widget(ScreenConfig(name='config2'))
        sm.add_widget(Screenvisual(name='config3'))
        return sm

if __name__ == "__main__":
    PaswordingApp().run()


