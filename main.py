from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

import kivy
kivy.require('1.11.1')



from kivy.lang import Builder

from kivy.uix.checkbox import CheckBox

# ...

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
            Button:
                text:'classes'
    Splitter:
        sizable_from: 'left'

        BoxLayout:

            orientation: 'vertical'
            
            BoxLayout:
                orientation: 'horizontal'
                Label:
                    text:'Images path:'
                TextInput:
                    text: 'enter path here.'
                    multiline: False
            BoxLayout:
                orientation: 'horizontal'
                Label:
                    text:'Output path:'
                TextInput:
                    text: 'enter path here.'
                    multiline: False
            Label: 
                text:'Problem:'
            BoxLayout:
                orientation: 'horizontal'
                CheckBox:
                    group: 'problem'
                Label:
                    text:'Classification'
            BoxLayout:
                orientation: 'horizontal'
                CheckBox:
                    group: 'problem'
                Label:
                    text:'Detection'

            Label:
                text: 'output format:'

            BoxLayout:
                orientation: 'horizontal'
                CheckBox:
                    active: True
                    group: 'format'
                Label:
                    text:'png'

            BoxLayout:
                orientation: 'horizontal'
                CheckBox:
                    active: True
                    group: 'format'
                Label:
                    text:'jpg'

            BoxLayout:
                orientation: 'horizontal'
                CheckBox:
                    active: True
                    group: 'format'
                Label:
                    text:'gif'
            Label:
                text: 'Reshape?'
            BoxLayout:
                orientation: 'horizontal'
                CheckBox:
                    group: 'reshape'   
                Label:
                    text:'No'
  
            BoxLayout:

                orientation: 'horizontal'
                CheckBox:
                    group: 'reshape'       
                Label:
                    text:'Yes'

                TextInput:
                    text: 'x'
                    multiline: False
                    size_hint: None, None
                    height: 50
                    padding:10

                Label: 
                    text: 'x'
                TextInput:
                    text: 'y'
                    multiline: False
                    size_hint: None, None
                    height: 50
                    padding:10
            Label:
                text: 'Label output Format:'
            BoxLayout:
                orientation: 'horizontal'
                Label:
                    text:'hdf5'
                CheckBox:
                    group: 'Label'                     


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