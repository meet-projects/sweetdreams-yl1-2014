import pygame as pg
import imagesclass
import buttonclass
import labels
import sys

def clear():
    main_screen.fill((255, 255, 255))




if __name__=="__main__":
    pg.init()
    main_screen = pg.display.set_mode((600, 600))
    main_screen.fill((255,255,255))
    image1=imagesclass.image(50, 500, "pygame_tiny.png")
    image1.draw_image(main_screen)
    button1=buttonclass.button(275, 400, 55, 50, "Enter", 20, (0, 0, 255))
    buttonclass.button.draw_button(button1, main_screen)
    label1 = labels.label((0,0,0), 200, 200, 175, 100, "Welcome To Sweet Dreams", 25)
    label1.draw_label(main_screen)

    

    while True: 
        ev = pg.event.poll()
        if ev.type == pg.QUIT: 
                sys.exit()
        if ev.type == pg.MOUSEBUTTONDOWN:
            x, y = ev.pos
            print ev.pos
            if button1.button_rec.collidepoint(x, y):
                button1.clear_button(main_screen)
                clear()

                button2=buttonclass.button(50, 300, 200, 200, "Cakes", 100, (0, 0, 255))
                buttonclass.button.draw_button(button2, main_screen)

                button3=buttonclass.button(350, 300, 200, 200, "Ice cream", 63, (0, 0, 255))
                buttonclass.button.draw_button(button3, main_screen)

                label2 = labels.label((0,0,0), 200, 200, 175, 100, "Choose Your Fate", 25)
                label2.draw_label(main_screen)

            if button2.button_rec.collidepoint(x, y):
                button2.clear_button(main_screen)
                clear()

                button4=buttonclass.button(50, 150, 300, 100, "Chocolate Cake", 30, (100, 0, 255))
                buttonclass.button.draw_button(button4, main_screen)

                button5=buttonclass.button(50, 300, 300, 100, "Vanilla Cake", 30, (100, 0, 255))
                buttonclass.button.draw_button(button5, main_screen)

                button6=buttonclass.button(50, 450, 300, 100, "Strawberry Cake", 30, (100, 0, 255))
                buttonclass.button.draw_button(button6, main_screen)

                button7=buttonclass.button(350, 150, 50, 50, "+", 50, (100, 0, 255))
                buttonclass.button.draw_button(button7, main_screen)

                button8=buttonclass.button(350, 200, 50, 50, "-", 50, (100, 0, 255))
                buttonclass.button.draw_button(button8, main_screen)

                button9=buttonclass.button(350, 300, 50, 50, "+", 50, (100, 0, 255))
                buttonclass.button.draw_button(button9, main_screen)

                button10=buttonclass.button(350, 350, 50, 50, "-", 50, (100, 0, 255))
                buttonclass.button.draw_button(button10, main_screen)

                button11=buttonclass.button(350, 450, 50, 50, "+", 50, (100, 0, 255))
                buttonclass.button.draw_button(button11, main_screen)

                button12=buttonclass.button(350, 500, 50, 50, "-", 50, (100, 0, 255))
                buttonclass.button.draw_button(button12, main_screen)

            if button3.button_rec.collidepoint(x, y):
                button3.clear_button(main_screen)
                clear()


                button13=buttonclass.button(50, 150, 300, 100, "Chocolate Ice Cream", 50, (142, 255, 61))
                buttonclass.button.draw_button(button13, main_screen)

                button14=buttonclass.button(50, 300, 300, 100, "Vanilla Ice Cream", 50, (142, 255, 61))
                buttonclass.button.draw_button(button14, main_screen)

                button15=buttonclass.button(50, 450, 300, 100, "Strawberry Ice Cream", 50, (142, 255, 61))
                buttonclass.button.draw_button(button15, main_screen)

                button16=buttonclass.button(350, 150, 50, 50, "+", 50, (142, 255, 61))
                buttonclass.button.draw_button(button16, main_screen)

                button17=buttonclass.button(350, 200, 50, 50, "-", 50, (142, 255, 61))
                buttonclass.button.draw_button(button17, main_screen)

                button18=buttonclass.button(350, 300, 50, 50, "+", 50, (142, 255, 61))
                buttonclass.button.draw_button(button18, main_screen)

                button19=buttonclass.button(350, 350, 50, 50, "-", 50, (142, 255, 61))
                buttonclass.button.draw_button(button19, main_screen)

                button20=buttonclass.button(350, 450, 50, 50, "+", 50, (142, 255, 61))
                buttonclass.button.draw_button(button20, main_screen)

                button21=buttonclass.button(350, 500, 50, 50, "-", 50, (142, 255, 61))
                buttonclass.button.draw_button(button21, main_screen)


        pg.display.flip()


