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
            # on_press=self.back,
            )
        ad = self.btn.text
        al1.add_widget(self.btn)
        self.bl = BoxLayout(orientation = 'vertical' )

        kol = Label(text='Напишите название блоков', color=[0, 0, 0, 1], size_hint = [1, .1])
        self.bl.add_widget(kol)
        self.gl = GridLayout(cols = 3, size_hint = [1, .5],padding = [50])


        self.add_widget(self.bl)
        self.add_widget(al)
        self.add_widget(al1)
    def back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'config1'
    def output_ (self):
        for i in range(int(sm.get_screen('config1').ids.inpt.text)):
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
                btn1.bind(on_release=lambda btn1: dropdown.select(int(btn1.group[-1])))
                dropdown.add_widget(btn1)
            mainbutton = Button(text='Hello', size_hint=(1, 1),  background_color=[0, 1.5, 3, 1], )
            mainbutton.bind(on_release=dropdown.open)
            dropdown.bind(on_select=lambda instance, x: print(self.gl.children[::-1][(x * 3) + 1].text))

            self.gl.add_widget(mainbutton)
        print(self.gl.children)
        self.bl.add_widget(self.gl)
        kol = Label(text=f'', color=[0, 0, 0, 1])
        self.bl.add_widget(kol)


    def get_data(self, ind):
        mas = []
        mas.append(ind)
        print(mas)
class PaswordingApp(App):
    def build(self):

        sm.add_widget(ScreenMain(name='config1'))
        sm.add_widget(ScreenConfig(name='config2'))
        return sm

if __name__ == "__main__":
    PaswordingApp().run()


