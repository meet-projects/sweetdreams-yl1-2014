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
    button1=buttonclass.button(200, 300, 200, 60, "Enter", 90, (0, 191, 255))
    buttonclass.button.draw_button(button1, main_screen)
    print ""
    label1 = labels.label((123,43,200), 200, 200, 40, 100, "Welcome To Sweet Dreams", 60)
    label1.draw_label(main_screen)

    numcc = 0
    numvc = 0
    numsc = 0
    numcic = 0
    numvic = 0
    numsic = 0
    

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


                button_cmain=buttonclass.button(50, 350, 200, 100, "Cakes", 94, (0, 191, 255))
                buttonclass.button.draw_button(button_cmain, main_screen)
                

                button_icmain=buttonclass.button(350, 350, 200, 100, " Ice cream", 59, (0, 191, 255))
                buttonclass.button.draw_button(button_icmain, main_screen)

                label2 = labels.label((255,0,0), 200, 200, 200, 100, "Choose Your Fate", 33)
                label2.draw_label(main_screen)


            if button_cmain.button_rec.collidepoint(x, y):
                button_cmain.clear_button(main_screen)
                clear()
                

                button_finc=buttonclass.button(450, 50, 59, 20, "Finish", 30, (238, 130, 238))
                buttonclass.button.draw_button(button_finc, main_screen)

                button4=buttonclass.button(50, 150, 300, 100, "Chocolate Cake", 55, (210, 105, 30))
                buttonclass.button.draw_button(button4, main_screen)
###############

                button7=buttonclass.button(350, 150, 50, 50, " + ", 50, (210, 105, 30))
                buttonclass.button.draw_button(button7, main_screen)

                button8=buttonclass.button(350, 200, 50, 50, "  -  ", 50, (210, 105, 30))
                buttonclass.button.draw_button(button8, main_screen)

                button4_1=buttonclass.button(400, 150, 50, 50, " " + str(numcc) + " ", 70, (210, 105, 30))
                buttonclass.button.draw_button(button4_1, main_screen)
                
                if button4.button_rec.collidepoint(x, y):
                    image4=imagesclass.image(50, 500, "cc.png")
                    image4.draw_image(main_screen)

                if button7.button_rec.collidepoint(x, y):
                    numcc+=1
                    button4_1=buttonclass.button(400, 150, 50, 50, " " + str(numcc) + " ", 70, (210, 105, 30))
                    buttonclass.button.draw_button(button4_1, main_screen)

                if button8.button_rec.collidepoint(x, y):
                    numcc-=1
                    button4_1=buttonclass.button(400, 150, 50, 50, " " + str(numcc) + " " , 70, (210, 105, 30))
                    buttonclass.button.draw_button(button4_1, main_screen)

                button5=buttonclass.button(50, 300, 300, 100, "Vanilla Cake", 70, (225,225,240))
                buttonclass.button.draw_button(button5, main_screen)

                button9=buttonclass.button(350, 300, 50, 50, " + ", 50, (225,225,240))
                buttonclass.button.draw_button(button9, main_screen)

                button10=buttonclass.button(350, 350, 50, 50, "  -  ", 50, (225,225,240))
                buttonclass.button.draw_button(button10, main_screen)

                button5_1=buttonclass.button(400, 300, 50, 50, " " + str(numvc) + " ", 70, (225,225,240))
                buttonclass.button.draw_button(button5_1, main_screen)
                
                if button5.button_rec.collidepoint(x, y):
                    image5=imagesclass.image(50, 500, "vc.png")
                    image5.draw_image(main_screen)

                if button9.button_rec.collidepoint(x, y):
                    numvc+=1
                    button5_1=buttonclass.button(400, 300, 50, 50, " " + str(numvc) + " ", 70, (225,225,240))
                    buttonclass.button.draw_button(button5_1, main_screen)

                if button10.button_rec.collidepoint(x, y):
                    numvc-=1
                    button5_1=buttonclass.button(400, 300, 50, 50, " " + str(numvc) + " ", 70, (225,225,240))
                    buttonclass.button.draw_button(button5_1, main_screen)

                button6=buttonclass.button(50, 450, 300, 100, "Strawberry Cake", 53, (219,112,147))
                buttonclass.button.draw_button(button6, main_screen)

                button11=buttonclass.button(350, 450, 50, 50, " + ", 50, (219,112,147))
                buttonclass.button.draw_button(button11, main_screen)

                button12=buttonclass.button(350, 500, 50, 50, "  -  ", 50, (219,112,147))
                buttonclass.button.draw_button(button12, main_screen)

                button6_1=buttonclass.button(400, 450, 50, 50, " " + str(numsc) + " ", 70, (219,112,147))
                buttonclass.button.draw_button(button6_1, main_screen)
                
                if button6.button_rec.collidepoint(x, y):
                    image6=imagesclass.image(50, 500, "sc.png")
                    image6.draw_image(main_screen)

                if button11.button_rec.collidepoint(x, y):
                    numsc+=1
                    button6_1=buttonclass.button(400, 450, 50, 50, " " + str(numsc) + " ", 70, (219,112,147))
                    buttonclass.button.draw_button(button6_1, main_screen)

                if button12.button_rec.collidepoint(x, y):
                    numsc-=1
                    button6_1=buttonclass.button(400, 450, 50, 50, " " + str(numsc) + " ", 70, (219,112,147))
                    buttonclass.button.draw_button(button6_1, main_screen)
                
                

                if button_finc.button_rec.collidepoint(x, y):
                    clear()
                                                                                                                                                                            ###
                                                                                                                                                                        ######
          ##                                                                                                                                                    ######   ##       #   #
            ##                                      ########                                                  ##########                 ###########       ###
                #################################################################################
                             #######                                             #########                                                    ###########
                                                                                                                                                                   ########                



            if button_icmain.button_rec.collidepoint(x, y):
                button_icmain.clear_button(main_screen)
                clear()

                button13=buttonclass.button(50, 150, 300, 100, "Chocolate Ice Cream", 40, (210, 105, 30))
                buttonclass.button.draw_button(button13, main_screen)

                button16=buttonclass.button(350, 150, 50, 50, " + ", 50, (210, 105, 30))
                buttonclass.button.draw_button(button16, main_screen)

                button17=buttonclass.button(350, 200, 50, 50, "  -  ", 50, (210, 105, 30))
                buttonclass.button.draw_button(button17, main_screen)

                button13_1=buttonclass.button(400, 150, 50, 50, " " + str(numcic) + " ", 70, (210, 105, 30))
                buttonclass.button.draw_button(button13_1, main_screen)
                
                if button13.button_rec.collidepoint(x, y):
                    image13=imagesclass.image(500, 500, "cic.png")
                    image13.draw_image(main_screen)
#########
                if button16.button_rec.collidepoint(x, y):
                    numcic+=1
                    button13_1=buttonclass.button(400, 150, 50, 50, " " + str(numcic) + " ", 70, (210, 105, 30))
                    buttonclass.button.draw_button(button13_1, main_screen)

                if button17.button_rec.collidepoint(x, y):
                    numcic-=1
                    button13_1=buttonclass.button(400, 150, 50, 50, " " + str(numcic) + " ", 70, (210, 105, 30))
                    buttonclass.button.draw_button(button13_1, main_screen)
#########
                button14=buttonclass.button(50, 300, 300, 100, "Vanilla Ice Cream", 50, (225,225,240))
                buttonclass.button.draw_button(button14, main_screen)

                button18=buttonclass.button(350, 300, 50, 50, " + ", 50, (225,225,240))
                buttonclass.button.draw_button(button18, main_screen)

                button19=buttonclass.button(350, 350, 50, 50, "  -  ", 50, (225,225,240))
                buttonclass.button.draw_button(button19, main_screen)

                button14_1=buttonclass.button(400, 300, 50, 50, " " + str(numvic) + " ", 70, (225,225,240))
                buttonclass.button.draw_button(button14_1, main_screen)

                if button14.button_rec.collidepoint(x, y):
                    image14=imagesclass.image(500, 500, "vic.png")
                    image14.draw_image(main_screen)

                if button18.button_rec.collidepoint(x, y):
                    numvic+=1
                    button14_1=buttonclass.button(400, 300, 50, 50, " " + str(numvic) + " ", 70, (225,225,240))
                    buttonclass.button.draw_button(button14_1, main_screen)

                if button19.button_rec.collidepoint(x, y):
                    numvic-=1
                    button14_1=buttonclass.button(400, 300, 50, 50, " " + str(numvic) + " ", 70, (225,225,240))
                    buttonclass.button.draw_button(button14_1, main_screen)
                
                button15=buttonclass.button(50, 450, 300, 100, "Strawberry Ice Cream", 40, (219,112,147))
                buttonclass.button.draw_button(button15, main_screen)

                button20=buttonclass.button(350, 450, 50, 50, " + ", 50, (219,112,147))
                buttonclass.button.draw_button(button20, main_screen)

                button21=buttonclass.button(350, 500, 50, 50, "  -  ", 50, (219,112,147))
                buttonclass.button.draw_button(button21, main_screen)

                button15_1=buttonclass.button(400, 450, 50, 50, " " + str(numsic) + " ", 70, (219,112,147))
                buttonclass.button.draw_button(button15_1, main_screen)
                
                if button15.button_rec.collidepoint(x, y):
                    image15=imagesclass.image(500, 500, "sic.png")
                    image15.draw_image(main_screen)

                if button20.button_rec.collidepoint(x, y):
                    numcic+=1
                    button15_1=buttonclass.button(400, 450, 50, 50, " "+ str(numsic) + " ", 70, (219,112,147))
                    buttonclass.button.draw_button(button15_1, main_screen)

                if button21.button_rec.collidepoint(x, y):
                    numcic-=1
                    button15_1=buttonclass.button(400, 450, 50, 50, " " + str(numsic) + " ", 70, (219,112,147))
                    buttonclass.button.draw_button(button15_1, main_screen)

                
        pg.display.flip()


