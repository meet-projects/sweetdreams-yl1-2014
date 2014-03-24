import pygame as pg
import imagesclass
import buttonclass
import labels


if __name__=="__main__":
    pg.init()
    main_screen = pg.display.set_mode((600, 600))
    main_screen.fill((255,255,255))
    image1=imagesclass.image(100, 100, "pygame_tiny.png")
    image1.draw_image(main_screen)
    button1=buttonclass.button(300, 100, 50, 50, "Butsdasdfsdfton1", 1, (255, 0, 0))
    button1.draw_button(main_screen)
    label1 = labels.label((255,0,0), 200, 200, 100, 300, "label", 25)
    label1.draw_label(main_screen)

    while True: 
        ev = pg.event.poll()
        if ev.type == pg.QUIT: 
                sys.exit()
        if ev.type == pg.MOUSEBUTTONDOWN:
            x, y = ev.pos
            print ev.pos
            if image1.image_surface.collidepoint(x, y):
                image1.clear_images(main_screen)    
            if button1.button_rec.collidepoint(x, y):
                button1.clear_button(main_screen)
        pg.display.flip()
 
