#!/usr/bin/python3

import random

import pygame

from pygame.locals import *

from frogger import *


class Rectangle:

	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def intersects(self, other):
		left = self.x
		top = self.y
		right = self.x + self.w
		bottom = self.y + self.h

		oleft = other.x
		otop = other.y
		oright = other.x + other.w
		obottom = other.y + other.h

		return not (left >= oright or right <= oleft or top >= obottom or bottom <= otop)


class Frog(Rectangle):

	def __init__(self, x, y, w):
		super(Frog, self).__init__(x, y, w, w)
		self.color = (0, 255, 0)
		self.attached = None

	def move(self, xdir, ydir, grid):
		self.x += xdir * grid
		self.y += ydir * grid

	def attach(self, obstacle):	
		self.attached = obstacle

	def update(self):
		if self.attached is not None:
			self.x += self.attached.speed

		if self.x + self.w > g_vars['width']:
			self.x = g_vars['width'] - self.w
		
		if self.x < 0:
			self.x = 0
		if self.y + self.h > g_vars['width']:
			self.y = g_vars['width'] - self.w
		if self.y < 0:
			self.y = 0

	def draw(self):
		rect = Rect( [self.x, self.y], [self.w, self.h] )
		pygame.draw.rect( g_vars['window'], self.color, rect )


class Obstacle(Rectangle):

	def __init__(self, x, y, w, h, s):
		super(Obstacle, self).__init__(x, y, w, h)
		self.color = (255, 255, 255)
		self.speed = s

	def update(self):
		self.x += self.speed
		if self.speed > 0 and self.x > g_vars['width'] + g_vars['grid']:
			self.x = -self.w
		elif self.speed < 0 and self.x < -self.w:
			self.x = g_vars['width']

	def draw(self):
		rect = Rect( [self.x, self.y], [self.w, self.h] )
		pygame.draw.rect( g_vars['window'], self.color, rect )


class Lane(Rectangle):

	def __init__(self, y, c=None, t='safety', n=0, l=0, spc=0, spd=0):
		super(Lane, self).__init__(0, y * g_vars['grid'], g_vars['width'], g_vars['grid'])
		self.type = t
		self.color = c
		self.obstacles = []
		if c is None:
			offset = random.uniform(0, 200)
			for i in range(n):
				self.obstacles.append(Obstacle(offset + spc * i, y * g_vars['grid'], l * g_vars['grid'], g_vars['grid'], spd))

	def check(self, frog):
		attached = False
		frog.attach(None)
		for obstacle in self.obstacles:
			if frog.intersects(obstacle):
				if self.type == 'car':
					return True
				if self.type == 'log':
					attached = True
					frog.attach(obstacle)
		if not attached and self.type == 'log':
			return True
		return False

	def update(self):
		for obstacle in self.obstacles:
			obstacle.update()

	def draw(self):
		if self.color is not None:
			pygame.draw.rect( g_vars['window'], self.color, Rect( [self.x, self.y], [self.w, self.h] ) )
		for obstacle in self.obstacles:
			obstacle.draw()
