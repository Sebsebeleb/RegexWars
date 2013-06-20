import cocos
from cocos.director import director
import pyglet.text.document
print pyglet.text.document

director.init()

go_find = (20,40)
style = {"background_color":(255,255,0,255),"color":(50,50,50,255)}

test_text = open("lorem.txt").read()

a = test_text[:19]
b = "[background_color]"

label = cocos.text.RichLabel(test_text,width=200,multiline=True)
label.element.document.set_style(20,40,style)
label.position = (50,300)

director.run(cocos.scene.Scene(label))