import math
def setup():
    size(1200,1200)
    stroke(255)
    noFill()

def draw():
    background(0)
    for i in range(0, width, 30):
        if i < mouseX or i < mouseY:
            rect(width-i,height-i,i,i)
        if i < width/2:
            line(0,i, mouseX, mouseY)
            line(i, 0, mouseX, mouseY)
