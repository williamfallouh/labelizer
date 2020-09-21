from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.config import Config
from kivy.uix.checkbox import CheckBox
import kivy




# kivy.require('1.11.1')
Config.set('graphics', 'fullscreen', False)
Config.set('graphics', 'window_state', 'visible')
Config.write()

Window.maximize()

def on_checkbox_active(checkbox, value):
    if value:
        print('The checkbox', checkbox, 'is active')
    else:
        print('The checkbox', checkbox, 'is inactive')

checkbox = CheckBox()
checkbox.bind(active=on_checkbox_active)


root = Builder.load_string(
'''
BoxLayout:
    orientation: 'horizontal'
    BoxLayout:
        orientation: 'vertical'
        canvas:
            Color: 
                rgba: 1,1,1,0.5
            Rectangle:
                size: self.size
        Image:
            source: 'bigSample.png'
            size: self.size
        Splitter:
            sizable_from:'top'
            max_size: 2000
            Button:
                text:'classes'
    Splitter:
        sizable_from: 'left'
        max_size: 4000

        BoxLayout:
            canvas:
                Color: 
                    rgba: 1,1,1,0.2
                Rectangle:
                    size: self.size
                    pos:self.pos    
            orientation: 'vertical'
            Label: 
                text:'   Dataset:'
                bold:'True'
                font_size: 25
                size_hint_x: None
                size: self.texture_size 
                size_hint_y: None
                height:100
                padding: 30,30    
            BoxLayout:
                size_hint_y: None
                height:50
                orientation: 'horizontal'
                Label:
                    text:'   Images path:   '
                    size_hint_x: None
                    size: self.texture_size
                TextInput:
                    text: 'enter path here.'
                    size_hint_y: None
                    multiline: False
                    height:40
                Button:
                    text: 'Parcourir'
                    size_hint_x: None
                    size_hint_y: None
                    multiline: False
                    height:39    
                    width:100                 
            BoxLayout: 
                size_hint_y: None
                height:50     
                orientation: 'horizontal'
                Label:
                    text:'   Output path:   '
                    size_hint_x: None
                    size: self.texture_size
                TextInput:
                    text: 'enter path here.'
                    size_hint_y: None
                    multiline: False
                    height:40
                Button:
                    text: 'Parcourir'
                    size_hint_x: None
                    size_hint_y: None
                    multiline: False
                    height:39    
                    width:100    
            Label: 
                text:'   Problem:'
                bold:'True'
                font_size: 25
                size_hint_x: None
                size: self.texture_size     
                size_hint_y: None
                height:100
                padding:30,30  

            BoxLayout:
                size_hint_y: None
                height:50
                orientation: 'horizontal'
                CheckBox:
                    group: 'problem'
                    size_hint_x: None
                Label:
                    text:'Classification'
                    size_hint_x: None                    
                    size: self.texture_size
            BoxLayout:
                size_hint_y: None
                height:50
                orientation: 'horizontal'
                CheckBox:
                    group: 'problem'
                    size_hint_x: None
                       
                Label:
                    text:'Detection'
                    size_hint_x: None
                    size: self.texture_size   
            Label:
                text: '   output format:'
                bold:'True'
                font_size: 25
                size_hint_x: None
                size: self.texture_size
                size_hint_y: None
                height:100
                padding:30,30  

            BoxLayout:
                size_hint_y: None
                height:50
                orientation: 'horizontal'
                CheckBox:
                    active: True
                    group: 'format'
                    size_hint_x: None
                Label:
                    text:'rgba'
                    size_hint_x: None
                    size: self.texture_size                       

            BoxLayout:
                size_hint_y: None
                height:50
                orientation: 'horizontal'
                CheckBox:
                    size_hint_x: None
                    group: 'format'
                Label:
                    size_hint_x: None
                    size: self.texture_size                   
                    text:'rgb'
                     
            Label:
                text: '   Reshape?'
                bold:'True'
                font_size: 25
                size_hint_x: None
                size: self.texture_size
                size_hint_y: None
                height:100
                padding:30,30  
            BoxLayout:
                size_hint_y: None
                height:50
                orientation: 'horizontal'
                CheckBox:
                    size_hint_x: None
                    group: 'reshape'
                    active: True
                    id:reshapeYes
                Label:
                    text:'No'
                    size_hint_x: None
                    size: self.texture_size                       
  
            BoxLayout:

                orientation: 'horizontal'
                size_hint_y: None
                height:50

                CheckBox:
                    size_hint_x: None
                    group: 'reshape'
                Label:
                    text:'Yes    '
                    size_hint_x: None
                    size: self.texture_size                       

                TextInput:
                    text: 'x'
                    multiline: False
                    size_hint: None, None
                    height: 40
                    width: 60
                    disabled: reshapeYes.active

                Label: 
                    text: '*'
                    height: 40
                    width: 30
                    size_hint_x: None
                    size_hint_y: None

                TextInput:
                    text: 'y'
                    multiline: False
                    size_hint: None, None
                    height: 40
                    width:60
                    disabled: reshapeYes.active
            Label:
                text: '   Label output Format:'
                size_hint_y: None
                height:100
                padding:30,30
                bold:'True'
                font_size: 25
                size_hint_x: None
                size: self.texture_size     
            BoxLayout:
                size_hint_y: None
                height:50
                orientation: 'horizontal'
                CheckBox:
                    group: 'Label'
                    size_hint_x: None
                Label:
                    text:'hdf5'
                    size_hint_x: None
                    size: self.texture_size  
            BoxLayout:
                size_hint_y: None
                height:50
                orientation: 'horizontal'
                CheckBox:
                    group: 'Label'
                    size_hint_x: None
                Label:
                    text:'txt'
                    size_hint_x: None
                    size: self.texture_size  
            BoxLayout:
                size_hint_y: None
                height:50
                orientation: 'horizontal'
                CheckBox:
                    group: 'Label'
                    size_hint_x: None
                Label:
                    text:'json'
                    size_hint_x: None
                    size: self.texture_size                   
            Widget



''')
'''
class Root(Widget):
	pass
'''	
class MainApp(App):
    def build(self):
#        return Root()
        return root
if __name__ == '__main__':
    MainApp().run()