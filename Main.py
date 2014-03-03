import pygame as pg
import imagesclass
if __name__=="__main__":
	pg.init()
	main_screen = pg.display.set_mode((400, 400))
	main_screen.fill((255,255,255))
	image1=imagesclass.image(100, 100, "pygame_tiny.png")
	image1.draw_image(main_screen)
	while True: 
        	ev = pg.event.poll()
        	if ev.type == pg.QUIT: 
            		sys.exit()
        	if ev.type == pg.MOUSEBUTTONDOWN:
            		x, y = ev.pos
           		if image1.image_surface.collidepoint(x, y):
				image1.clear_images(main_screen)
		pg.display.flip()
 
