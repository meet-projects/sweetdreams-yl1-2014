import pygame as pg
class button(object):
	def __init__(self, xlocation_button, ylocation_button, widht_button, height_button, text_button, onclickaction, color):
        	self.xlocb = xlocation_button
        	self.ylocb = ylocation_button
        	self.widthb = widht_button
        	self.heightb = height_button
		self.textb = text_button
		self.action = onclickaction
		self.colorb = color
	
	def draw_button(self, place):
		self.button_rec = pg.Rect(self.xlocb, self.ylocb,self.widthb, self.heightb)
		self.button_surface = pg.Surface([self.widthb,self.heightb])
		self.button_surface.fill(self.colorb)		
		place.blit(self.button_surface, self.button_rec)
		buttonlabel = pg.font.Font(None, 30)
		self.buttonlabel = buttonlabel.render(self.textb, 1, (0, 0, 0))
		place.blit(self.buttonlabel, self.button_rec)
		
	def clear_button(self, place):
		clear_button_surface = pg.Surface([self.widthb,self.heightb])
		clear_button_surface.fill((255,255,255))
		place.blit(clear_button_surface, self.button_rec)