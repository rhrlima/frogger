#!/usr/bin/python3

import pygame
from pygame.locals import *

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
		self.x += xdir * grid#(self.x + (xdir * grid)) // grid * grid
		self.y += ydir * grid

	def attach(self, log):	
		self.attached = log

	def update(self, window_w, grid):
		if self.attached is not None:
			self.x += self.attached.speed
		if self.x + self.w > window_w:
			self.x = window_w - self.w
		elif self.x < 0:
			self.x = 0

	def draw(self, surface):
		rect = Rect( [self.x, self.y], [self.w, self.h] )
		pygame.draw.rect( surface, self.color, rect )


class Car(Rectangle):

	def __init__(self, x, y, w, h, s):
		super(Car, self).__init__(x, y, w, h)
		self.color = (255, 255, 255)
		self.speed = s

	def update(self, window_w, grid):
		self.x += self.speed
		if self.speed > 0 and self.x > window_w + grid:
			self.x = -self.w
		elif self.speed < 0 and self.x < -self.w:
			self.x = window_w

	def draw(self, surface):
		rect = Rect( [self.x, self.y], [self.w, self.h] )
		pygame.draw.rect( surface, self.color, rect )


class Log(Rectangle):

	def __init__(self, x, y, w, h, s):
		super(Log, self).__init__(x, y, w, h)
		self.color = (255, 255, 255)
		self.speed = s

	def update(self, window_w, grid):
		self.x += self.speed
		if self.speed > 0 and self.x > window_w + grid:
			self.x = -self.w
		elif self.speed < 0 and self.x < -self.w:
			self.x = window_w

	def draw(self, surface):
		rect = Rect( [self.x, self.y], [self.w, self.h] )
		pygame.draw.rect( surface, self.color, rect )