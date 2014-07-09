Michele's group project feedback
---

Good job getting your project to work like you wanted with the extra features of the add and subtract buttons. I had a few comments about your project in general: 

* Your team could have improved it's communication between yourselves before starting work every day. One way to improve this is to, before you start coding, go around in the group and split up the work. 
* On your quantity map for Cakes, only the Vanilla cake buttons work correctly - the others do not work. The same problem happens with the ice cream (only the vanilla works properly.)
* The "Finish" button on the Cakes and Ice Cream menu does not work
* In addition to making the Finish button work correctly, it would have been nice to be able to buy both Cakes and Ice Cream with a back button.
* Good job calling your entry function `Main.py` - it makes it very easy for anyone using your program to see what file to write and what file to look at. 
* The structure of your main program is good. In general, however, you should not be creating buttons or labels or objects inside the main `while` loop. Instead, you should create all the objects together outside of the main loop, and just use the `draw_button` and `draw_label` functions to actually draw the buttons inside the loop. Creating and re-creating the buttons inside the `while` loop makes the program ues a lot of computer memory. 
* Good job making `clear` and `clear_button` functions work properly.
* You can improve making your variable names more clear - for example, instead of naming your button `button1`, you can name it `enterbutton`. 