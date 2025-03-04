from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.config import Config
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import AliasProperty, StringProperty, ListProperty, BooleanProperty


import kivy

from subprocess import Popen, PIPE
from kivy.uix.screenmanager import Screen


#from myCheckBox import MyCheckBox


# kivy.require('1.11.1')
Config.set('graphics', 'fullscreen', False)
Config.set('graphics', 'window_state', 'visible')
Config.write()

Window.maximize()

class MyCheckBox(CheckBox):
    allow_no_selection = BooleanProperty(False)



'''

checkbox.bind(active=on_checkbox_active)
'''


root = Builder.load_file('main.kv')
"""
root = Builder.load_string(
'''
BoxLayout:
    orientation: 'horizontal'
    BoxLayout:	
        orientation: 'vertical'
        canvas:
            Color: 
                rgba: 1,1,1,0.3
            Rectangle:
                size: self.size
        Image:
            source: 'bigSample.png'
            size: self.size

        Splitter:
            sizable_from:'top'
            max_size: 1000
            BoxLayout:
                orientation: 'horizontal'

                Button:
                    text:'+ add class'
                    size_hint_x: None
                    on_press: app.addClassCallback()
                ScrollView:
                    do_scroll_y: False
                    GridLayout:
                        width: self.minimum_width
                        size_hint: None, None
                        id:classesGrid
                        rows: 4
                        cols: None
                        row_force_default: True
                        row_default_height: 100
                        col_force_default: True
                        col_default_width: 400


    Splitter:
        sizable_from: 'left'
        max_size: 4000
        _parent_proportion: .5
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
                MyCheckBox:
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

                MyCheckBox:
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

"""
'''
class Root(Widget):
	pass
'''	

class Draw(Widget):
    def on_touch_down(self,touch):
        with self.canvas:
            touch.ud["line"]=Line(points=(touch.x,touch.y))
    def on_touch_move(self,touch):
        with self.canvas:
            touch.ud["line"].points +=(touch.x,touch.y)
    def on_touch_up(self,touch):
        print("released mouse",touch)

        
class MainApp(App):
    classNumber = 0

    def build(self):
#        return Root()
        classNumber = 0
        return root

    def setInputPath(self):
        self.inputPath = root.ids.inputPathTI.text
        print("input path set to " + self.inputPath )

    def setOutputPath(self):
        self.outputPath = root.ids.outputPathTI.text
        print("output path set to " + self.outputPath )

    def setOutputPath(self):
        self.outputPath = root.ids.outputPathTI.text
        print("output path set to " + self.outputPath )

    def addClassCallback(self):

        process = Popen(['python3', 'classAdd.py'],stdin = PIPE, stdout=PIPE, stderr=PIPE)

        output, err = process.communicate(b"input data that is passed to subprocess' stdin")
        print(output)
        if output!=b"":
            output =(output).decode("utf-8").split(";")
            print(output)
            name = output[0] + "("+ str(self.classNumber)+")"
            color = get_color_from_hex(output[1])
            box = BoxLayout(orientation= 'horizontal')
            root.ids.classesGrid.add_widget(box)
            box.add_widget(CheckBox(group= 'class', size_hint_x = None))  
            box.add_widget(Label(text = name, size_hint_x = None))
            box.add_widget(Button(size = (50,50), size_hint_x = None, size_hint_y = None, pos_hint = {'x':.23, 'y':.23}, background_normal= '',  background_color = color ))
            self.classNumber+=1

    
 


if __name__ == '__main__':
    MainApp().run()


