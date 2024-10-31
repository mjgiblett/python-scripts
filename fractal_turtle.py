import turtle
from random import randint
import random

lsystem_rules = {
    'Binary Tree': {'1': '11', '0': '1[+0]-0'},
    'Koch Curve': {'F': 'F+F-F-F+F'},
    'Sierpinski Triangle': {'F': 'F-G+F+G-F', 'G': 'GG'},
    'Sierpinski Arrowhead': {'F': 'G-F-G', 'G': 'F+G+F'},
    'Dragon Curve': {'F': 'F+G', 'G': 'F-G'},
    'Fractal Plant': {'X': 'F+[[X]-X]-F[-FX]+X', 'F': 'FF'},
    'Tree': {'F': 'G[@[-F]+F]'} #{'X': 'F[@[-X]+X]'}
    }

lsystem_axioms = {
    'Binary Tree': '0',
    'Koch Curve': 'F',
    'Sierpinski Triangle': 'F-G-G',
    'Sierpinski Arrowhead': 'F',
    'Dragon Curve': 'F',
    'Fractal Plant': 'X',
    'Tree': 'FY'
    }

lsystem_angles = {
    'Binary Tree': 45.0,
    'Koch Curve': 90.0,
    'Sierpinski Triangle': 120.0,
    'Sierpinski Arrowhead': 60.0,
    'Dragon Curve': 90.0,
    'Fractal Plant': 25.0,
    'Tree': lambda: randint(0, 45)
    }

lsystem_colours = {
    'Binary Tree': [0.35, 0.2, 0.0],
    'Koch Curve': [1, 0.3, 0.0],
    'Sierpinski Triangle': [1, 0.3, 0.0],
    'Sierpinski Arrowhead': [1, 0.3, 0.0],
    'Dragon Curve': [1, 0.3, 0.0],
    'Fractal Plant': [0.3, 0.5, 0.0],
    'Tree': [0.35, 0.2, 0.0]
    }

lsystem_steps = {
    'Binary Tree': 20,
    'Koch Curve': 20,
    'Sierpinski Triangle': 50,
    'Sierpinski Arrowhead': 50,
    'Dragon Curve': 40,
    'Fractal Plant': 10,
    'Tree': 85
    }

class App:
    def __init__(self):
        self.system = self.get_system()
        self.width, self.height = 1600, 900
        self.screen = turtle.Screen()
        self.screen.setup(self.width, self.height)
        self.screen.screensize(3 * self.width, 3 * self.height)
        self.screen.bgcolor('black')
        self.screen.delay(0)
        
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.penup()
        self.pen.setpos(self.width // 6, -self.height // 4 - 25)
        self.pen.pendown()
            
        self.ls = LindenmayerSystem(self.pen, self.system)

    def get_system(self):
        systems = list(lsystem_rules.keys())
        for i, system in enumerate(systems):
            print(f'{i}: {system}')
        while True:
            try:
                system = systems[int(input('\nWhich Lindenmayer system do you want to see? '))]                
                return system
            except Exception as e:
                print(e)

    def run(self):
        self.ls.draw()
        self.screen.exitonclick()

class LindenmayerSystem:
    def __init__(self, turtle, system):
        self.rules = lsystem_rules[system]
        self.axiom = lsystem_axioms[system]
        self.angle = lsystem_angles[system]
        self.colour = lsystem_colours[system]
        self.thickness = 3
        self.step = lsystem_steps[system]
        self.gens = 5

        self.stack = []

        self.pen = turtle
        self.pen.left(90)
        self.pen.pensize(self.thickness)
        self.pen.hideturtle()

    def get_result(self):
        for gen in range(self.gens):
            self.axiom = ''.join([self.rules[char] if char in self.rules.keys() else char for char in self.axiom])
            
    def draw(self):
        self.get_result()
        for char in self.axiom:
            self.pen.color(self.colour)
            if char == 'F' or char == 'G' or char == '1':
                self.pen.forward(self.step)
            elif char == '0':
                self.pen.forward(self.step // 2)
            elif char == '@':
                self.step -= 6
                self.colour[1] += 0.04
                self.thickness -= 2
                self.thickness = max(1, self.thickness)
                self.pen.pensize(self.thickness)
            elif char == '+':
                self.pen.left(self.angle if type(self.angle) is float else self.angle())
            elif char == '-':
                self.pen.right(self.angle if type(self.angle) is float else self.angle())
            elif char == '[':
                angle, pos = self.pen.heading(), self.pen.pos()
                self.stack.append((angle, pos, self.thickness, self.step, self.colour[1]))
            elif char == ']':
                angle, pos, self.thickness, self.step, self.colour[1] = self.stack.pop()
                self.pen.pensize(self.thickness)
                self.pen.setheading(angle)
                self.pen.penup()
                self.pen.goto(pos)
                self.pen.pendown()

def BarnsleyFern():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("green")
    pen.penup()

    x = 0
    y = 0
    for n in range(11000):
        pen.goto(65 * x, 37 * y - 252)  # scale the fern to fit nicely inside the window
        pen.pendown()
        pen.dot(3)
        pen.penup()
        r = random.random()
        if r < 0.01:
            x, y =  0.00 * x + 0.00 * y,  0.00 * x + 0.16 * y + 0.00
        elif r < 0.86:
            x, y =  0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.60
        elif r < 0.93:
            x, y =  0.20 * x - 0.26 * y,  0.23 * x + 0.22 * y + 1.60
        else:
            x, y = -0.15 * x + 0.28 * y,  0.26 * x + 0.24 * y + 0.44

if __name__ == '__main__':
    app = App()
    app.run()