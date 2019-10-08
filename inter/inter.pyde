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
            r = (255/(posX or 1) * i)
            g = (255/(posY or 1) * j)
            if i > posX:
                r = 255/(width/scale - posX) * (width/scale - i)
            if j > posY:
                g = 255/(height/scale - posY) * (width/scale -j)


            fill(r, g, j*scale*255/height)
            rect(i*scale, j*scale, scale, scale)
