import cairo
import math

WIDTH = 256
HEIGHT= 256

frame = 0

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT) #Normalization of Canvas


ctx.move_to(0, 0)

def convertToCairoUnits(number):
    return number/WIDTH

def filenames(num):
    num = str(num)
    while len(num)<4:
        num = "0"+num
    return num


class Rectangle:
    def __init__(self,x1,y1,x2,y2,border_radius):
        #Make sure that x2 is always bigger than x1 and for y respectively
        if x1>x2:
            x1, x2 = x2, x1
        if y1>y2:
            y1, y2 = y2, y1
        #Check that border isnt too thik
        if border_radius > (x2-x1 or y2-y1):
            raise "Border Radius to THIK"
    
        self.x1 = convertToCairoUnits(x1)
        self.y1 = convertToCairoUnits(y1)
        self.x2 = convertToCairoUnits(x2)
        self.y2 = convertToCairoUnits(y2)
        self.border_radius = convertToCairoUnits(border_radius)
        self.r = 0 #Red Value of col
        self.g = 0 #Green Value of col
        self.b = 0 #Blue Value of col

    def translate(self,x,y):
        x = convertToCairoUnits(x)
        y = convertToCairoUnits(y)
        self.x1 = self.x1+x
        self.x2 = self.x2+x
        self.y1 = self.y1+y
        self.y2 = self.y2+y

    def draw(self):
        #Draw the Rectangle
        ctx.set_source_rgba(0,0,255,1)
        ctx.rectangle(self.x1,self.y1,self.x2-self.x1,self.y2-self.y1)
        ctx.fill()
        ctx.set_source_rgba(self.r,self.g,self.b)
        ctx.rectangle(self.x1+self.border_radius,self.y1+self.border_radius, self.x2-self.x1-2*self.border_radius, self.y2-self.y1-2*self.border_radius, )
        ctx.fill()
    
    def animate(self, x, y, time=1):
        global frame
        time = time*30
        dx = x/time
        dy = y/time
        for i in range(time):
            self.translate(dx,dy)
            self.draw()
            surface.write_to_png(f"out/{filenames(frame)}.png")
            #Clear the Surface
            bg.draw()
            frame+=1


x = Rectangle(10,10,200,200,5)
bg = Rectangle(0,0,WIDTH,HEIGHT,0)
bg.draw()
x.animate(100,50)
"""
for i in range(10):
    x.draw()
    x.translate(5,10)
    surface.write_to_png(f"out/0{i}.png")
    #Clear the Surface
    bg.draw()
for i in range(10):
    x.draw()
    x.translate(-5,-10)
    surface.write_to_png(f"out/{i+10}.png")
    #Clear the Surface
    bg.draw()
"""