def setup():
    background(0)
    noFill()
    stroke(255)
    size(800,800)

def draw():
    for i in range(0, 100):
        line (8*i, 0, 8*i, 300)
        line(8*i,300,800,800)
        if i%10 == 0:
            rect(100,200,5*i, 5*i)
