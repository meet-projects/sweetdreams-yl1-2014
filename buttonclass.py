import pygame as pg
class button(object):
	def __init__(self, xlocation_button, ylocation_button, widht_button, height_button, text_button, text_size, color):
		self.xlocb = xlocation_button
		self.ylocb = ylocation_button
		self.widthb = widht_button
		self.heightb = height_button
		self.textb = text_button
		self.txtsize = text_size
		self.colorb = color

	
	def draw_button(self, place):
		buttonlabel = pg.font.Font(None, self.txtsize)
		self.buttonlabel = buttonlabel.render(self.textb, 1, self.colorb, (44, 44, 44))
		self.button_rec = pg.Rect(self.xlocb, self.ylocb,self.widthb, self.heightb)
		print [self.buttonlabel.get_width(), self.buttonlabel.get_height()]
		self.button_surface = pg.Surface([self.buttonlabel.get_width(), self.buttonlabel.get_height()])
		self.button_surface.fill(self.colorb)		
		place.blit(self.button_surface, self.button_rec)
		place.blit(self.buttonlabel, self.button_rec)
		
	def clear_button(self, place):
		clear_button_surface = pg.Surface([self.widthb,self.heightb])
		clear_button_surface.fill((255,255,255))
		place.blit(clear_button_surface, self.button_rec)
