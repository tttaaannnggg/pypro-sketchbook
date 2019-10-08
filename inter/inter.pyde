import math
scale

def setup():
    global scale
    scale = 100
    size(1400,1400)
    stroke(255)

def draw():
    global scale
    posX = math.floor(mouseX/scale)
    posY = math.floor(mouseY/scale)
    for i in range(0, width/scale):
        for j in range(0, width/scale):
            fill((mouseX*255)/width, mouseY*255/width, j*scale*255/height)
            rect(i*scale, j*scale, scale, scale)
