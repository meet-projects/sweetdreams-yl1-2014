import pygame as pg
class image(object):
                def __init__(self, xlocation_image, ylocation_image, filename_image):
                        self.xloc = xlocation_image
                        self.yloc = ylocation_image
                        self.fname = filename_image

                def draw_image(self, place):
                        image = pg.image.load(self.fname)
                        self.width = image.get_width()
                        self.height = image.get_height()
                        self.image_surface = pg.Rect(self.xloc, self.yloc,self.width, self.height)
                        place.blit(image, self.image_surface)
                def clear_images(self, place):
                        clear_image_surface = pg.Surface([self.width,self.height])
                        clear_image_surface.fill((255,255,255))
                        place.blit(clear_image_surface, self.image_surface)

		
		

