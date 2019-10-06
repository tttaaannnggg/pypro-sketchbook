from collections import deque
cycle = 0
colors = deque([])
state = 0

def setup():
    colorMode(HSB, 100)
    noStroke()
    global colors
    size(1800,500)
    for i in range (0, width/100):
        colors.append([0,255,0])

def draw():
    global cycle
    global state
    global colors

    if mousePressed:
        state = (state+1) % 3
    colors[-1][state] = int(float(mouseX)/float(width) *100)
    cycle = (cycle+1) %2
    if cycle == 0:
        colors.append(colors[-1][:])
        colors.popleft()

    print(colors)
    for i, col in enumerate(colors):
        fill(*col)
        rect(i*100, 0, 100, 500)
