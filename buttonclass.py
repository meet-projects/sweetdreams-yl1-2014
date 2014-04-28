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
		self.buttonlabel = pg.font.Font(None, self.txtsize)
		size = self.buttonlabel.size(self.textb)
		self.button_surface = pg.Surface(size)
		self.button_rec = pg.Rect(self.xlocb, self.ylocb, size[0], size[1])

	
	def draw_button(self, place):
		self.buttonlabel = self.buttonlabel.render(self.textb, 1, self.colorb, (44, 44, 44))
		self.button_surface.fill(self.colorb)		
		place.blit(self.button_surface, self.button_rec)
		place.blit(self.buttonlabel, self.button_rec)
	def onlyblit(self, place):
		self.button_surface = pg.Surface([self.widthb,self.heightb])
		place.blit(self.button_surface, self.button_rec)

		
	def clear_button(self, place):
		clear_button_surface = pg.Surface([self.widthb,self.heightb])
		clear_button_surface.fill((255,255,255))
		place.blit(clear_button_surface, self.button_rec)
		self.button_rec = pg.Rect(7000, 7000,1, 1)
