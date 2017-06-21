#!/usr/bin/python3

#Normal imports
import random

#Pygame imports
import pygame
from pygame.locals import *

#Custom imports
from actors import *


class App:

	def __init__(self):
		self.window_width = 450
		self.window_height = 500
		self.fps = 30
		self.running = True
		self.display_surf = None
		self.clock = None
		self.grid = 32
		self.frog = None
		self.cars = []
		self.logs = []

	def init(self):
		pygame.init()
		self.display_surf = pygame.display.set_mode( [self.window_width, self.window_height], pygame.HWSURFACE )
		self.running = True
		self.clock = pygame.time.Clock()

		self.reset()
		#self.frog = Frog(self.window_height/2 - self.grid, self.window_height - 8 * self.grid, self.grid)

		for i in range(2):# LINE 1
			self.cars.append( Car(i * 250 + 30, self.window_height - 4 * self.grid, self.grid*random.randint(2,3), self.grid, 1.5) )
		for i in range(4):# LINE 2
			self.cars.append( Car(i * 160 + 70, self.window_height - 5 * self.grid, self.grid, self.grid, 2.4) )
		for i in range(3):# LINE 3
			self.cars.append( Car(i * 200 + 45, self.window_height - 6 * self.grid, self.grid, self.grid, -3.2) )
		for i in range(3):# LINE 4
			self.cars.append( Car(i * 180 + 45, self.window_height - 7 * self.grid, self.grid*random.randint(2,3), self.grid, -2) )

		for i in range(2):# LINE 5
			self.logs.append( Log(i * 270 + 20, self.window_height - 9 * self.grid, self.grid*3, self.grid, -1) )
		for i in range(4):# LINE 6
			self.logs.append( Log(i * 160 + 50, self.window_height - 10 * self.grid, self.grid*2, self.grid, 1.2) )
		for i in range(2):# LINE 7
			self.logs.append( Log(i * 300 + 0, self.window_height - 11 * self.grid, self.grid*4, self.grid, -1.2) )
		for i in range(3):# LINE 8
			self.logs.append( Log(i * 170 + 0, self.window_height - 12 * self.grid, self.grid*2, self.grid, 2) )

	def reset(self):
		self.frog = Frog(self.window_height/2 - self.grid, self.window_height - 8 * self.grid, self.grid)
		self.frog.attach(None)

	def event(self, event):
		if event.type == QUIT:
			self.running = False

		if event.type == KEYDOWN and event.key == K_ESCAPE:
			self.running = False

		if event.type == KEYDOWN and event.key == K_LEFT:
			self.frog.move(-1, 0, self.grid)
		if event.type == KEYDOWN and event.key == K_RIGHT:
			self.frog.move(1, 0, self.grid)
		if event.type == KEYDOWN and event.key == K_UP:
			self.frog.move(0, -1, self.grid)
		if event.type == KEYDOWN and event.key == K_DOWN:
			self.frog.move(0, 1, self.grid)

	def update(self):
		for car in self.cars:
			car.update(self.window_width, self.grid)
			if self.frog.intersects(car):
				self.reset()
		for log in self.logs:
			log.update(self.window_width, self.grid)
		if self.frog.y < self.window_height-self.grid*8 and self.frog.y > self.window_height-self.grid*13:
			attached = False
			for log in self.logs:
				if self.frog.intersects(log):
					attached = True
					self.frog.attach(log)
			if not attached:
				self.reset()
		else:
			self.frog.attach(None)
		self.frog.update(self.window_width, self.grid)

	def draw(self):
		self.display_surf.fill( (0, 0, 0) )
		pygame.draw.rect(self.display_surf, (100, 100, 100), Rect( [0, self.window_height-3*self.grid], [self.window_width, self.grid] ) )
		pygame.draw.rect(self.display_surf, (100, 100, 100), Rect( [0, self.window_height-8*self.grid], [self.window_width, self.grid] ) )
		pygame.draw.rect(self.display_surf, (100, 100, 100), Rect( [0, self.window_height-13*self.grid], [self.window_width, self.grid] ) )

		for car in self.cars:
			car.draw(self.display_surf)

		for log in self.logs:
			log.draw(self.display_surf)

		self.frog.draw(self.display_surf)
		print(self.frog.x)
		pygame.display.flip()

	def cleanup(self):
		pygame.quit()
		quit()

	def execute(self):
		if self.init() == False:
			self.running = False

		while self.running:
			for event in pygame.event.get():
				self.event( event )
			self.update()
			self.draw()
			self.clock.tick(self.fps)
		self.cleanup()


if __name__ == "__main__":
	gameApp = App()
	gameApp.execute()