import pygame as pg
import math

class Cardioid:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()        
        self.lines = 200
        self.counter, self.inc = 0, 0.01

    def get_colour(self):
        self.counter += self.inc
        self.counter, self.inc = (self.counter, self.inc) if 0 < self.counter < 1 else (max(min(self.counter, 1), 0), -self.inc)

        return pg.Color('red').lerp('green', self.counter)

    def draw(self):
        self.screen.fill('black')
        time = pg.time.get_ticks()
        self.radius = 350 + 50 * abs(math.sin(time * 0.004) - 0.5)
        factor = 1 + 0.0001 * time

        for i in range(self.lines):
            theta = (2 * math.pi / self.lines) * i
            
            x1 = int(self.radius * math.cos(theta)) + self.H_WIDTH
            x2 = int(self.radius * math.cos(factor * theta)) + self.H_WIDTH
            y1 = int(self.radius * math.sin(theta)) + self.H_HEIGHT
            y2 = int(self.radius * math.sin(factor * theta)) + self.H_HEIGHT

            pg.draw.aaline(self.screen, self.get_colour(), (x1, y1), (x2, y2))

        pg.display.flip()

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = Cardioid()
    app.run()