import pygame as pg
class label(object):
	def __init__(self, label_color, label_size_x, label_size_y, label_location_x, label_location_y, label_text, label_fontsize):
		self.colorl = label_color
		self.sizex = label_size_x
		self.sizey = label_size_y
		self.locationx = label_location_x
		self.locationy = label_location_y
		self.fontsize = label_fontsize
		self.text = label_text
	def draw_label(self, place):
		self.label_rec = pg.Rect(self.locationx, self.locationy, self.sizex, self.sizey)
		self.label = pg.font.Font(None, self.fontsize)
		self.label = self.label.render(self.text, 1, self.colorl, (255, 255, 255))
		place.blit(self.label, self.label_rec)
	def clear_label(self, place):
		clear_label_surface = pg.Surface([self.sizex,self.sizey])
		clear_label_surface.fill((255,255,255))
		place.blit(self.label_surface, self.label_rec)




