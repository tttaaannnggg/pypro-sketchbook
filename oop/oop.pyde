class Car:
    # __init__ is part of the spec for classes
    # it doesn't matter what you call the first arg- it's always getting passed "self"
    # which is kinda similar to JS "this"
    def __init__(s):
        s.c = color(255)
        s.x = 100
        s.y = 100
        s.xs = 1

    def display(s):
        rectMode(CENTER)
        fill(s.c)
        rect(s.x, s.y, 20, 10)

    def drive(self):
        self.x += self.xs
        if self.x > width:
            self.x = 0

    #even with a rest style param, it takes self as arg 0
    def test(*s):
        args = list(s)
        print(args)
        

thisCar = Car()

def setup():
    size(200, 200)
    global thisCar

def draw():
    global thisCar
    background(255)
    if mousePressed:
        # when you call a method, you're passing it a second arg
        # thisCar.test('asdf') is basically thisCar.test(thisCar, 'asdf')
        thisCar.test('asdf')
