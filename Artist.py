import turtle
import math

class Artist:

    def __init__(self, t):
        self.t = t
        screen = turtle.Screen()
        screen.bgcolor("black")
    
    def triangle(self, size = 50):
        self.t.backward(25)
        self.t.speed(5)
        self.t.color("maroon")
        self.t.fillcolor("maroon")
        self.t.begin_fill()
        for i in range(3):
            self.t.forward(size)
            self.t.left(120)
        self.t.end_fill()
            
    def square(self, size  = 50):
        self.t.speed(5)
        self.t.color("brown")
        self.t.fillcolor("brown")
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(size)
            self.t.left(90)
        self.t.end_fill()
            
    def circle(self, size = 1):
        self.t.setposition(-15, -25)
        self.t.pensize(2)
        self.t.speed(10)
        self.t.fillcolor("sandy brown")
        self.t.color("sandy brown")
        self.t.begin_fill()
        for i in range(360):
            self.t.forward(size)
            self.t.left(1)
        self.t.end_fill()
            
    def circle2(self, size = 60):
        self.t.penup()
        self.t.setposition(-27, 42)
        center_x = -15
        center_y = 27
        radius = 60
        self.t.pensize(2)
        self.t.speed(10)
        self.t.fillcolor("sandy brown")
        self.t.color("sandy brown")
        self.t.begin_fill()
        for i in range(360):
            r = math.radians(i)
            x = center_x + radius * math.cos(r)
            y = center_y + radius * math.sin(r)
            self.t.setposition(x, y)
            self.t.pendown()
        self.t.end_fill()
        
        self.t.penup()
        self.t.setposition(-15,-25)
        self.t.pendown()
            
    def circle3(self, size = 150):
        self.t.speed(10)
        self.t.pensize(1)
        self.t.color("sky blue")
        self.t.left(30)
        self.t.backward(25)
        for i in range(37):
            self.t.forward(size)
            self.t.left(130)
        self.t.penup()
            
    def star(self, size = 65):
        self.t.setposition(-33, 3)
        self.t.setheading(0)
        self.t.left(72)
        self.t.color("white")
        self.t.fillcolor("white")
        self.t.begin_fill()
        self.t.pendown()
        for i in range(5):
            self.t.forward(size)
            self.t.right(144)
        self.t.end_fill()
            
    def polygon(self, size = 50):
        self.t.speed(5)
        self.t.color("chocolate")
        self.t.fillcolor("black")
        a = 5
        for i in range(3):
            self.t.begin_fill()
            for i in range(a):
                self.t.forward(size)
                self.t.left(360/a)
            a = a + 1
            self.t.end_fill()

    def spiral(self, size = 67):
        self.t.pensize(3)
        self.t.penup()
        self.t.speed(8)
        self.t.setposition(-28, 124)
        self.t.setheading(0)
        self.t.pendown()
        
        for i in range(40):
            if(self.t.heading() == 0):
                self.t.color("khaki")
            elif(self.t.heading() == 90):
                self.t.color("yellow green")
            elif(self.t.heading() == 180):
                self.t.color("olive drab")
            elif(self.t.heading() == 270):
                self.t.color("olive")
            distance = 67 * (i/15+1);
            self.t.forward(distance)
            self.t.right(45)
        self.t.penup()
                
            
    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

def main():

    canvas = turtle.Screen()
    canvas.bgcolor("cyan")
    canvas.title("Turtle Example")
    t = turtle.Turtle()
    t.shape("turtle")
    art = Artist(t)
    
    art.circle2()
    art.triangle()
    art.square()
    art.polygon()
    art.circle3()
    art.star()
    art.spiral()
    


if __name__ == "__main__":
    main()
