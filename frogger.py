#!/usr/bin/python3

import random

import pygame
from pygame.locals import *

from actors import *


g_vars = {}
g_vars['width'] = 448
g_vars['height'] = 448
g_vars['fps'] = 30
g_vars['grid'] = 32
g_vars['window'] = pygame.display.set_mode( [g_vars['width'], g_vars['height']], pygame.HWSURFACE)


class App:

	def __init__(self):
		self.running = True
		self.display_surf = None
		self.clock = None
		self.frog = None
		self.lanes = []

	def init(self):
		pygame.init()
		self.running = True
		self.clock = pygame.time.Clock()
		self.reset()

		self.lanes.append( Lane( 2, (100, 100, 100) ) )

		self.lanes.append( Lane( 3, t='log', n=2, l=6, spc=350, spd=1.2) )
		self.lanes.append( Lane( 4, t='log', n=3, l=2, spc=230, spd=-1.6) )
		self.lanes.append( Lane( 5, t='log', n=4, l=2, spc=140, spd=1.6) )
		self.lanes.append( Lane( 6, t='log', n=2, l=3, spc=230, spd=-2) )

		self.lanes.append( Lane( 7, (100, 100, 100) ) )

		self.lanes.append( Lane( 8, t='car', n=3, l=2, spc=100, spd=-2) )
		self.lanes.append( Lane( 9, t='car', n=3, l=4, spc=240, spd=-1) )
		self.lanes.append( Lane( 10, t='car', n=4, l=2, spc=130, spd=3) )
		self.lanes.append( Lane( 11, t='car', n=4, l=3, spc=350, spd=2) )

		self.lanes.append( Lane( 12, (100, 100, 100) ) )
		
	def reset(self):
		self.frog = Frog(g_vars['height']/2 - g_vars['grid'], 12 * g_vars['grid'], g_vars['grid'])
		self.frog.attach(None)

	def event(self, event):
		if event.type == QUIT:
			self.running = False

		if event.type == KEYDOWN and event.key == K_ESCAPE:
			self.running = False

		if event.type == KEYDOWN and event.key == K_LEFT:
			self.frog.move(-1, 0, g_vars['grid'])
		if event.type == KEYDOWN and event.key == K_RIGHT:
			self.frog.move(1, 0, g_vars['grid'])
		if event.type == KEYDOWN and event.key == K_UP:
			self.frog.move(0, -1, g_vars['grid'])
		if event.type == KEYDOWN and event.key == K_DOWN:
			self.frog.move(0, 1, g_vars['grid'])

	def update(self):
		for lane in self.lanes:
			lane.update()
			if self.frog.intersects(lane) and lane.check(self.frog):
				self.reset()
		self.frog.update()

	def draw(self):
		g_vars['window'].fill( (0, 0, 0) )
		for lane in self.lanes:
			lane.draw()
		self.frog.draw()
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
			self.clock.tick(g_vars['fps'])
		self.cleanup()


if __name__ == "__main__":
	gameApp = App()
	gameApp.execute()