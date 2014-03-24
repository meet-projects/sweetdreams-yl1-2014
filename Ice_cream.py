import pygame as pg
class icecream(object):
	def __init__(self, name="", price=0, quantity=0, file_name=""):
		self.name= name
		self.price= price
		self.quantity= quantity
		self.file_name= file_name
	
	def draw_pic (self, place):
		self.button_rec = pg.Rect(100, 100, 20, 20)
		self.buttonimg = pg.image.load(self.file_name)
   		place.blit(self.buttonimg, self.button_rec)

