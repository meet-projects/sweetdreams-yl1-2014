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
    button1=buttonclass.button(200, 300, 200, 60, " Enter ", 90, (0, 191, 255))
    buttonclass.button.draw_button(button1, main_screen)
    label1 = labels.label((0,0,0), 200, 200, 175, 100, "Welcome To Sweet Dreams", 25)
    label1.draw_label(main_screen)

    button_cmain=buttonclass.button(50000, 35000, 200, 100, "Cakes", 94, (0, 191, 255))
    buttonclass.button.draw_button(button_cmain, main_screen)
    button_icmain=buttonclass.button(5000, 35000, 200, 100, "Cakes", 94, (0, 191, 255))
    buttonclass.button.draw_button(button_icmain, main_screen)

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


            elif button_cmain.button_rec.collidepoint(x, y):
                button_cmain.clear_button(main_screen)
                button_icmain.clear_button(main_screen)
                clear()
                

                button_finc=buttonclass.button(450, 50, 59, 20, "Finish", 30, (238, 130, 238))
                buttonclass.button.draw_button(button_finc, main_screen)

                button_cc=buttonclass.button(50, 150, 300, 100, "Chocolate Cake", 55, (210, 105, 30))
                buttonclass.button.draw_button(button_cc, main_screen)
###############

                button_ccplu=buttonclass.button(350, 150, 50, 50, " + ", 50, (210, 105, 30))
                buttonclass.button.draw_button(button_ccplu, main_screen)

                button_ccmin=buttonclass.button(350, 200, 50, 50, "  -  ", 50, (210, 105, 30))
                buttonclass.button.draw_button(button_ccmin, main_screen)

                button_cc_num=buttonclass.button(400, 150, 50, 50, " " + str(numcc) + " ", 70, (210, 105, 30))
                buttonclass.button.draw_button(button_cc_num, main_screen)


                button_vc=buttonclass.button(50, 300, 300, 100, "Vanilla Cake", 70, (225,225,240))
                buttonclass.button.draw_button(button_vc, main_screen)

                button_vcplu=buttonclass.button(350, 300, 50, 50, " + ", 50, (225,225,240))
                buttonclass.button.draw_button(button_vcplu, main_screen)

                button_vcmin=buttonclass.button(350, 350, 50, 50, "  -  ", 50, (225,225,240))
                buttonclass.button.draw_button(button_vcmin, main_screen)

                button_vc_num=buttonclass.button(400, 300, 50, 50, " " + str(numvc) + " ", 70, (225,225,240))
                buttonclass.button.draw_button(button_vc_num, main_screen)

                button_sc=buttonclass.button(50, 450, 300, 100, "Strawberry Cake", 53, (219,112,147))
                buttonclass.button.draw_button(button_sc, main_screen)

                button_scplu=buttonclass.button(350, 450, 50, 50, " + ", 50, (219,112,147))
                buttonclass.button.draw_button(button_scplu, main_screen)

                button_scmin=buttonclass.button(350, 500, 50, 50, "  -  ", 50, (219,112,147))
                buttonclass.button.draw_button(button_scmin, main_screen)

                button_sc_num=buttonclass.button(400, 450, 50, 50, " " + str(numsc) + " ", 70, (219,112,147))
                buttonclass.button.draw_button(button_sc_num, main_screen)
                
            elif button_cc.button_rec.collidepoint(x, y):
                image4=imagesclass.image(50, 500, "cc.png")
                image4.draw_image(main_screen)

            elif button_ccplu.button_rec.collidepoint(x, y):
                numcc+=1
                button_cc_num=buttonclass.button(400, 150, 50, 50, " " + str(numcc) + " ", 70, (210, 105, 30))
                buttonclass.button.draw_button(button_cc_num, main_screen)

            elif button_ccmin.button_rec.collidepoint(x, y):
                numcc-=1
                print "sss"
                button_cc_num=buttonclass.button(400, 150, 50, 50, " " + str(numcc) + " " , 70, (210, 105, 30))
                buttonclass.button.onlyblit(button_cc_num, main_screen)

                
                
            elif button_vc.button_rec.collidepoint(x, y):
                image5=imagesclass.image(50, 500, "vc.png")
                image5.draw_image(main_screen)

            elif button_vcplu.button_rec.collidepoint(x, y):
                numvc+=1
                button_vc_num=buttonclass.button(400, 300, 50, 50, " " + str(numvc) + " ", 70, (225,225,240))
                buttonclass.button.draw_button(button_vc_num, main_screen)

            elif button_vcmin.button_rec.collidepoint(x, y):
                numvc-=1
                button_vc_num=buttonclass.button(400, 300, 50, 50, " " + str(numvc) + " ", 70, (225,225,240))
                buttonclass.button.draw_button(button_vc_num, main_screen)

                
                
            elif button_sc.button_rec.collidepoint(x, y):
                image6=imagesclass.image(50, 500, "sc.png")
                image6.draw_image(main_screen)

            elif button_scplu.button_rec.collidepoint(x, y):
                numsc+=1
                button_sc_num=buttonclass.button(400, 450, 50, 50, " " + str(numsc) + " ", 70, (219,112,147))
                buttonclass.button.draw_button(button_sc_num, main_screen)

            elif button_scmin.button_rec.collidepoint(x, y):
                numsc-=1
                button_sc_num=buttonclass.button(400, 450, 50, 50, " " + str(numsc) + " ", 70, (219,112,147))
                buttonclass.button.draw_button(button_sc_num, main_screen)
            
            

            elif button_finc.button_rec.collidepoint(x, y):
                clear()
                                                                                                                                                                            ###
                                                                                                                                                                        ######
          ##                                                                                                                                                    ######   ##       #   #
            ##                                      ########                                                  ##########                 ###########       ###
                #################################################################################
                             #######                                             #########                                                    ###########
                                                                                                                                                                   ########                



            elif button_icmain.button_rec.collidepoint(x, y):
                button_icmain.clear_button(main_screen)
                button_cmain.clear_button(main_screen)
                clear()

                button_cic=buttonclass.button(50, 150, 300, 100, "Chocolate Ice Cream", 40, (210, 105, 30))
                buttonclass.button.draw_button(button_cic, main_screen)

                button_cicplu=buttonclass.button(350, 150, 50, 50, " + ", 50, (210, 105, 30))
                buttonclass.button.draw_button(button_cicplu, main_screen)

                button_cicmin=buttonclass.button(350, 200, 50, 50, "  -  ", 50, (210, 105, 30))
                buttonclass.button.draw_button(button_cicmin, main_screen)

                button_cic_num=buttonclass.button(400, 150, 50, 50, " " + str(numcic) + " ", 70, (210, 105, 30))
                buttonclass.button.draw_button(button_cic_num, main_screen)
                
                if button_cic.button_rec.collidepoint(x, y):
                    image_cic=imagesclass.image(500, 500, "cic.png")
                    image_cic.draw_image(main_screen)
#########
                if button_cicplu.button_rec.collidepoint(x, y):
                    numcic+=1
                    button_cic_num=buttonclass.button(400, 150, 50, 50, " " + str(numcic) + " ", 70, (210, 105, 30))
                    buttonclass.button.draw_button(button_cic_num, main_screen)

                if button_cicmin.button_rec.collidepoint(x, y):
                    numcic-=1
                    button_cic_num=buttonclass.button(400, 150, 50, 50, " " + str(numcic) + " ", 70, (210, 105, 30))
                    buttonclass.button.draw_button(button_cic_num, main_screen)
#########
                button_vic=buttonclass.button(50, 300, 300, 100, "Vanilla Ice Cream", 50, (225,225,240))
                buttonclass.button.draw_button(button_vic, main_screen)

                button_vicplu=buttonclass.button(350, 300, 50, 50, " + ", 50, (225,225,240))
                buttonclass.button.draw_button(button_vicplu, main_screen)

                button_vicmin=buttonclass.button(350, 350, 50, 50, "  -  ", 50, (225,225,240))
                buttonclass.button.draw_button(button_vicmin, main_screen)

                button_vic_num=buttonclass.button(400, 300, 50, 50, " " + str(numvic) + " ", 70, (225,225,240))
                buttonclass.button.draw_button(button_vic_num, main_screen)

                if button_vic.button_rec.collidepoint(x, y):
                    image14=imagesclass.image(500, 500, "vic.png")
                    image14.draw_image(main_screen)

                if button_vicplu.button_rec.collidepoint(x, y):
                    numvic+=1
                    button_vic_num=buttonclass.button(400, 300, 50, 50, " " + str(numvic) + " ", 70, (225,225,240))
                    buttonclass.button.draw_button(button_vic_num, main_screen)

                if button_vicmin.button_rec.collidepoint(x, y):
                    numvic-=1
                    button_vic_num=buttonclass.button(400, 300, 50, 50, " " + str(numvic) + " ", 70, (225,225,240))
                    buttonclass.button.draw_button(button_vic_num, main_screen)
                
                button_sic=buttonclass.button(50, 450, 300, 100, "Strawberry Ice Cream", 40, (219,112,147))
                buttonclass.button.draw_button(button_sic, main_screen)

                button_sicplu=buttonclass.button(350, 450, 50, 50, " + ", 50, (219,112,147))
                buttonclass.button.draw_button(button_sicplu, main_screen)

                button_sicmin=buttonclass.button(350, 500, 50, 50, "  -  ", 50, (219,112,147))
                buttonclass.button.draw_button(button_sicmin, main_screen)

                button_sic_num=buttonclass.button(400, 450, 50, 50, " " + str(numsic) + " ", 70, (219,112,147))
                buttonclass.button.draw_button(button_sic_num, main_screen)
                
                if button_sic.button_rec.collidepoint(x, y):
                    image15=imagesclass.image(500, 500, "sic.png")
                    image15.draw_image(main_screen)

                if button_sicplu.button_rec.collidepoint(x, y):
                    numcic+=1
                    button_sic_num=buttonclass.button(400, 450, 50, 50, " "+ str(numsic) + " ", 70, (219,112,147))
                    buttonclass.button.draw_button(button_sic_num, main_screen)

                if button_sicmin.button_rec.collidepoint(x, y):
                    numcic-=1
                    button_sic_num=buttonclass.button(400, 450, 50, 50, " " + str(numsic) + " ", 70, (219,112,147))
                    buttonclass.button.draw_button(button_sic_num, main_screen)

                
        pg.display.flip()


