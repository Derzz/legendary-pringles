#Date Started: December 6th 2018
#Date Finished: December 19th 2018
#Title: The Quest to find the Legendary Pringles
#Author: Michael Xie
#Summary: This book will bring the user on an extraordinary quest full of danger and adventure to find the Legendary Pringles!
#Story should only be played on a Windows device
#Shell should not be seen by user, only for developer

#All Imports Needed
from graphics import *
import time
import winsound
import random

#Playing Tobu; Return the the Wild
winsound.PlaySound("returntothewild.wav", winsound.SND_ASYNC)


#Makes a window for the story to happen on
win = GraphWin("The Quest to Find the Legendary Pringles", 700, 500)


#List of Colors
yellowList = [(color_rgb(255,255,204)),(color_rgb(255,255,153)),(color_rgb(255,255,102)),(color_rgb(255,255,51)),(color_rgb(255,255,0))]

#Flags
#Flag to get out of title page
introflag = 0
#Flag for Pringbills
pringbillflag = 0
#Page 1 flag
pg1flag = 4
#Book Flag
bookflag = 0
#Paper Flag
paperflag = 0
#Trash Flag
trashflag = 0
#Page 2 flag
pg2flag = 0
#Decides sugar or salt
sugarflag = 0
saltflag = 0
#Page 3 flag
pg3flag = 0
#Page 4 flag
pg4flag = 0
#Page 5 flag
pg5flag = 0
#Page 5a flag
pg5aflag = 0
#Artifact Flag
artifactcounter = 0
pg6flag = 0
pg7flag = 0
pg7aflag = 0
pg8flag = 0
pg8aflag = 0
pg9flag = 0


#Title Background
#Sapphire Color
win.setBackground(color_rgb(15, 82, 186))

#Image of Pringles
pimage = Image(Point(250, 250), "pringleslogo.png")
pimage.draw(win)
#Title Text
titletxt2 = Text(Point(302, 50), "The Quest to Find the Legendary Pringles")
titletxt2.setFill("White")
titletxt2.setSize(20)
titletxt2.draw(win)

titletxt = Text(Point(300, 50), "The Quest to Find the Legendary Pringles")
titletxt.setFill("Yellow")
titletxt.setSize(20)
titletxt.draw(win)

#Author
authortxt = Text(Point(400, 450), "By Michael Xie")
authortxt.setFill("White")
authortxt.setSize(18)
authortxt.draw(win)

#Exit Button
ebutton = Rectangle(Point(600, 400), Point(700, 500))
ebutton.setFill("Red")
ebutton.draw(win)

etext = Text(Point(650, 450), "Exit")
etext.setFill("White")
etext.setSize(15)
etext.draw(win)

#Instructions Button
ibutton = Rectangle(Point(600, 200), Point(700, 250))
ibutton.setFill("Yellow")
ibutton.draw(win)

#Instructions Text
itext = Text(Point(650, 225), "Instructions")
itext.setFill("black")
itext.draw(win)

#Button to Start
sButton = Rectangle(Point(600,10), Point(700, 60))
sButton.setFill("Green")
sButton.draw(win)
  
#Start Text
sText = Text(Point(650, 35),"Start")
sText.setFill("White")
sText.draw(win)

#Booker Prize Text
booker = Image(Point(75, 420), "booker.png")
booker.draw(win)

#While loop for title page 
while introflag == 0:
    clickP = win.getMouse()
    cx=clickP.getX()
    cy=clickP.getY()

    if cx >= 600 and cx <= 700 and cy >=400 and cy <= 500:
    #Closes Window
        win.close()

    elif cx >= 600 and cx <= 700 and cy >= 200 and cy <= 250:
        #Cover to cover title page
        InstructionBarrier = Rectangle(Point(0,0), Point(700,500))
        InstructionBarrier.setFill(color_rgb(15, 82, 186))
        InstructionBarrier.draw(win)
        
        #Activates Instruction Slide
        #Title for Instructions
        instructionT = Text(Point(350, 15), "Instructions")
        instructionT.setSize(25)
        instructionT.setFill("White")
        instructionT.draw(win)

        #Instructions
        instruction = Text(Point(350, 75), "This is an interactive storybook. Your main objective is to find the Legendary Pringles.")
        instruction.setFill("White")
        instruction.draw(win)

        instruction2 = Text(Point(350, 95), "Follow the instructions given on each page to advance the story!")
        instruction2.setFill("White")
        instruction2.draw(win)

        instruction3 = Text(Point(350, 115), "MAKE SURE THAT YOUR KEYS AREN'T IN CAPS LOCK!")
        instruction3.setFill("White")
        instruction3.draw(win)

        #Exit Instructions
        exitinstructionT = Text(Point(350, 250), "Press any key to return to the main title")
        exitinstructionT.setFill("White")
        exitinstructionT.setSize(20)
        exitinstructionT.draw(win)

        #Image at bottom
        chibird = Image(Point(350, 500), "chibird.png")
        chibird.draw(win)

        exitins = win.getKey()
        
        if exitins != True:
            instructionT.undraw()
            instruction.undraw()
            instruction2.undraw()
            instruction3.undraw()
            exitinstructionT.undraw()
            InstructionBarrier.undraw()
            chibird.undraw()
            
    elif cx >= 600 and cx <= 700 and cy >= 10 and cy <= 60:
        introflag += 1

#While Loop Ended, Able to advance to next page
titletxt2.undraw()
titletxt.undraw()
ebutton.undraw()
etext.undraw()
ibutton.undraw()
itext.undraw()
pimage.undraw()
sButton.undraw()
sText.undraw()

#Change Background
namebckground = Rectangle(Point(0,0), Point(700, 500))
#Sapphire Color
namebckground.setFill(color_rgb(15, 82, 186))
namebckground.draw(win)

#Text for instructions
nametxt = Text(Point(355, 50), "What's your character's name?")
nametxt.setSize(35)
nametxt.setFill("White")
nametxt.draw(win)

#Advisory for user
nametxt1 = Text(Point(355, 100), "Please don't enter more than 9 characters.")
nametxt1.setSize(15)
nametxt1.setFill("White")
nametxt1.draw(win)

namebox = Rectangle(Point(175, 250), Point(425, 350))
namebox.setFill("pink")
namebox.draw(win)

#Name Entry
#Entry Box to let user input name
nameentry = Entry(Point(300,315), 10)
nameentry.setFill("sky blue")
nameentry.draw(win)

#Sun
sun = Image(Point(625, 155), "sun.png")
sun.draw(win)

#Hill
hill = Circle(Point(300,600), 200)
hill.setFill("green")
hill.draw(win)

while win.getKey() != "Return":
    time.sleep(0.5)

name = nameentry.getText()

time.sleep(1)

nametxt.undraw()
nametxt1.undraw()
namebox.undraw()
nameentry.undraw()
hill.undraw()
sun.undraw()

#Greet User with new name
greet = Text(Point(350, 250),"Hello "+name+"! Let's start the story!")
greet.setFill("white")
greet.setSize(25)
greet.draw(win)

time.sleep(5)

greet.undraw()

#Stops the title music
winsound.PlaySound(None, winsound.SND_PURGE)

#Page 1 of Story
#Main Theme - Professor Layton vs. Phoenix Wright: Ace Attorney
winsound.PlaySound("intro.wav", winsound.SND_ASYNC)
#Background
pg1background = Rectangle(Point(0,0), Point(700, 300))
pg1background.setFill(color_rgb(210,105,30))
pg1background.draw(win)

pg1background1 = Rectangle(Point(0,300), Point(700,500))
pg1background1.setFill(color_rgb(205,133,63))
pg1background1.draw(win)

#Text
pg1txt = Text(Point(342, 20), "One day, "+name+" was doing their homework for computer studies. Then, "+name+ " has an urge to" )
pg1txt.setSize(11)
pg1txt.draw(win)

pg1txt1 = Text(Point(335, 50), "get some Pringles. Not just any type of Pringles, " +name+ " wanted the legendary Pringles.")
pg1txt1.draw(win)

pg1txt2 = Text(Point(135, 80), name+" decided to go get some.")
pg1txt2.draw(win)

#Instruction for Advance
advancepg1 = Text(Point(345, 150), "Click the screen to continue!")
advancepg1.setSize(15)
advancepg1.setStyle("bold")
advancepg1.draw(win)

#Bookshelf
bkshelf = Rectangle(Point(50, 175), Point(150, 350))
bkshelf.setFill(color_rgb(160,82,45))
bkshelf.draw(win)

#Holes in bookshelf
bkshelfhole = Rectangle(Point(55, 200), Point(145, 230))
bkshelfhole.setFill(color_rgb(139,69,19))
bkshelfhole.draw(win)

bkshelfhole1 = Rectangle(Point(55, 250), Point(145, 280))
bkshelfhole1.setFill(color_rgb(139,69,19))
bkshelfhole1.draw(win)

#Books
bbook = Rectangle(Point(60,200), Point(70, 230))
bbook.setFill("blue")
bbook.draw(win)

rbook = Rectangle(Point(80, 200), Point(90,230))
rbook.setFill("red")
rbook.draw(win)

gbook = Rectangle(Point(100, 200), Point(110, 230))
gbook.setFill("green")
gbook.draw(win)

pbook = Rectangle(Point(100, 250), Point(110, 280))
pbook.setFill("pink")
pbook.draw(win)

#Table
#Table Legs
tablelegBL = Rectangle(Point(275,400), Point(285, 425))
tablelegBL.setFill(color_rgb(222,184,135))
tablelegBL.draw(win)

tablelegBR = Rectangle(Point(365,400), Point(375, 425))
tablelegBR.setFill(color_rgb(222,184,135))
tablelegBR.draw(win)

tablelegTR = Rectangle(Point(385,355), Point(395, 400))
tablelegTR.setFill(color_rgb(222,184,135))
tablelegTR.draw(win)
#Table Top
tabletop = Polygon(Point(300, 350), Point(400, 350), Point(375, 400), Point(275, 400))
tabletop.setFill(color_rgb(222,184,135))
tabletop.draw(win)

#Paper
paper = Polygon(Point(345, 355), Point(365, 355), Point(355, 395), Point(335, 395))
paper.setFill("white")
paper.draw(win)

#Character
stickHead = Circle(Point(350, 300), 20)
stickHead.setFill("white")
stickHead.draw(win)

#Body
stickBody = Line(Point(350, 320), Point(350, 350))
stickBody.setWidth(2)
stickBody.draw(win)

#Left Arm
stickLeft = Line(Point(350, 330), Point(325, 350))
stickLeft.setWidth(2)
stickLeft.draw(win)

#Right Arm
stickRight = Line(Point(350, 330), Point(375, 350))
stickRight.setWidth(2)
stickRight.draw(win)

#Trash Can
Trash1 = Rectangle(Point(505, 385), Point(545, 440))
Trash1.setFill("Grey")
Trash1.draw(win)

Trash2 = Circle(Point(525, 390), 20)
Trash2.setFill("Black")
Trash2.draw(win)

#Page number
pg1number = Text(Point(10, 490), "1")
pg1number.draw(win)



while pg1flag == 4:
    #Resay Click Methods
    clickP = win.getMouse()
    cx2=clickP.getX()
    cy2=clickP.getY()

    #If bookshelf is clicked, plus one to Pringbill counter
    if cx2 >= 55 and cx2 <= 250 and cy2 >= 145 and cy2 <= 280:
        while bookflag != 1:
            winsound.PlaySound(None, winsound.SND_PURGE)
            winsound.PlaySound("kaching.wav", winsound.SND_ASYNC)
            winsound.PlaySound("intro.wav", winsound.SND_ASYNC)
            pringbillflag += 1
            bookflag += 1
            print(pringbillflag)
    #If paper is clicked, plus one to Pringbill counter
    elif cx2 >= 335 and cx2 <= 365 and cy2 >= 355 and cy2 <= 395:
        while paperflag != 1:
            winsound.PlaySound(None, winsound.SND_PURGE)
            winsound.PlaySound("kaching.wav", winsound.SND_ASYNC)
            winsound.PlaySound("intro.wav", winsound.SND_ASYNC)
            pringbillflag += 1
            paperflag +=1
            print(pringbillflag)
    #If trash can is clicked, plus one to Pringbill counter
    elif cx2 >= 485 and cx2 <= 545 and cy2 >= 380 and cy2 <= 445:
        while trashflag != 1:
            winsound.PlaySound(None, winsound.SND_PURGE)
            winsound.PlaySound("kaching.wav", winsound.SND_ASYNC)
            winsound.PlaySound("intro.wav", winsound.SND_ASYNC)
            pringbillflag += 1
            trashflag +=1
            print(pringbillflag)

    else:
        #Undraw Page 1
        pg1txt.undraw()
        pg1txt1.undraw()
        pg1txt2.undraw()

        bkshelf.undraw()
        bkshelfhole.undraw()
        bkshelfhole1.undraw()

        bbook.undraw()
        rbook.undraw()
        gbook.undraw()
        pbook.undraw()

        tablelegBL.undraw()
        tablelegBR.undraw()
        tablelegTR.undraw()
        tabletop.undraw()

        paper.undraw()

        stickHead.undraw()
        stickBody.undraw()
        stickLeft.undraw()
        stickRight.undraw()

        Trash1.undraw()
        Trash2.undraw()

        pg1number.undraw()
        advancepg1.undraw()

        pg1flag += 4

#Page 2 Starts
#Draw Stickman
stickHead2 = Circle(Point(350, 300), 50)
stickHead2.setFill("white")
stickHead2.draw(win)

stickBody2 = Line(Point(350,350), Point(350, 500))
stickBody2.setWidth(3)
stickBody2.draw(win)

stickArmR = Line(Point(350, 395), Point(425, 295))
stickArmR.setWidth(3)
stickArmR.draw(win)

stickArmRA = Line(Point(425,295), Point(400, 315))
stickArmRA.setWidth(3)
stickArmRA.draw(win)

stickArmL = Line(Point(350, 395), Point(290, 450))
stickArmL.setWidth(3)
stickArmL.draw(win)

#Draw Page number
pg2number = Text(Point(10, 490), "2")
pg2number.draw(win)

#Sugar
sugar = Image(Point(550, 50), "sugar.png")
sugar.draw(win)

#Salt
salt = Image(Point(550, 200), "salt.png")
salt.draw(win)

#Text for page 2
pg2txt = Text(Point(200,50), name+ " firstly needed to arm themself with a weapon. ")
pg2txt.setSize(11)
pg2txt.draw(win)

pg2txt2 = Text(Point(210, 150), name+ " needed to choose to arm themself with sugar or salt.")
pg2txt2.setSize(11)
pg2txt2.draw(win)

pg2txt3 = Text(Point(245,215), "Click the sugar or salt to advance to the next page!")
pg2txt3.setSize(15)
pg2txt3.setStyle("bold")
pg2txt3.draw(win)

#Weapon impacts ending
while pg2flag != 1:
    clickP2 = win.getMouse()
    cx3=clickP2.getX()
    cy3=clickP2.getY()
    if cx3 >= 450 and cx3 <= 650 and cy3 >= 10 and cy3 <= 100:
        #Undraw page 2 and weappon is sugar
        sugarflag += 1
        stickHead2.undraw()
        stickBody2.undraw()
        stickArmR.undraw()
        stickArmRA.undraw()
        stickArmL.undraw()

        pg2number.undraw()

        sugar.undraw()

        salt.undraw()

        pg2txt.undraw()
        pg2txt2.undraw()
        pg2txt3.undraw()

        pg2flag += 1

    elif cx3 >= 500 and cx3 <= 590 and cy3 >= 145 and cy3 <= 255:
        #Undraw page 2 and weapon is salt
        saltflag += 1
        pg2flag += 1

        stickHead2.undraw()
        stickBody2.undraw()
        stickArmR.undraw()
        stickArmRA.undraw()
        stickArmL.undraw()

        pg2number.undraw()

        sugar.undraw()

        salt.undraw()

        pg2txt.undraw()
        pg2txt2.undraw()
        pg2txt3.undraw()

   
       
        
#Page 3 Start
#Stickman Page 3
while pg3flag != 1:
    #Stickman
    stickHead3 = Circle(Point(350, 250), 100)
    stickHead3.setFill("white")
    stickHead3.draw(win)

    stickBody3 = Line(Point(350, 350), Point(350, 500))
    stickBody3.setWidth(5)
    stickBody3.draw(win)

    stickR = Line(Point(350, 350), Point(450, 400))
    stickR.setWidth(5)
    stickR.draw(win)

    stickL = Line(Point(350, 350), Point(250, 400))
    stickL.setWidth(5)
    stickL.draw(win)

    #Text
    pg3txt = Text(Point(350, 100), "With the weapon in their pocket, "+name+" went off to find the Legendary Pringles.")
    pg3txt.setSize(13)
    pg3txt.draw(win)

    #Draw page Number
    pg3number = Text(Point(10, 490), "3")
    pg3number.draw(win)
    
  #Text to Continue
    pg3txt1 = Text(Point(350, 140), "Click the screen to continue!")
    pg3txt1.setSize(15)
    pg3txt1.setStyle("bold")
    pg3txt1.draw(win)
    #Click Points
    clickP3 = win.getMouse()


    if clickP3 != True:
        pg3flag += 1

#Undraw Page 3
stickHead3.undraw()
stickBody3.undraw()
stickR.undraw()
stickL.undraw()
pg3txt.undraw()
pg1background.undraw()
pg1background1.undraw()
pg3number.undraw()

#Page 4 Start
#Stop song
winsound.PlaySound(None, winsound.SND_PURGE)
#Playing SNES Monopoly; SNES Monopoly Main Theme
winsound.PlaySound("journey.wav", winsound.SND_ASYNC)
#Sky
pg4background = Rectangle(Point(0,0), Point(700, 350))
pg4background.setFill("sky blue")
pg4background.draw(win)
#Dirt
pg4background1 = Rectangle(Point(0,350), Point(700,500))
pg4background1.setFill(color_rgb(139,69,19))
pg4background1.draw(win)

#Bushes
bush = Image(Point(100, 350), "bush.png")
bush.draw(win)

bush2 = Image(Point(500, 350), "bush.png")
bush2.draw(win)

#Stickman
stickHead4 = Circle(Point(600, 275), 20)
stickHead4.setFill("white")
stickHead4.draw(win)

stickBody4 = Line(Point(600, 295), Point(600, 400))
stickBody4.setWidth(2)
stickBody4.draw(win)

stickLegL = Line(Point(600, 395), Point(575, 450))
stickLegL.setWidth(2)
stickLegL.draw(win)

stickLegR = Line(Point(600, 395), Point(625, 450))
stickLegR.setWidth(2)
stickLegR.draw(win)

stickArmL4 = Line(Point(600, 325), Point(575, 350))
stickArmL4.setWidth(2)
stickArmL4.draw(win)

stickArmR4 = Line(Point(600,325), Point(625, 350))
stickArmR4.setWidth(2)
stickArmR4.draw(win)

page4text = Text(Point(350, 50), name+ " left home and went on the road")
page4text1 = Text(Point(350, 75), "that will lead "+name+ " to find the Legendary Pringles.")
page4text.draw(win)
page4text1.draw(win)

page4instruction = Text(Point(350, 125), "Move " +name+ " to the left with the key 'a' to continue with their journey.")
page4instruction.setSize(15)
page4instruction.setStyle("bold")
page4instruction.draw(win)

page4instructionb = Text(Point(350, 175), "Move " +name+ " to the right with the key 'd' to go back to the last page.")
page4instructionb.setSize(15)
page4instructionb.setStyle("bold")
page4instructionb.draw(win)

#Draw page Number
pg4number = Text(Point(10, 490), "4")
pg4number.draw(win)

testPoint4 = Point(600,295)
testPoint4.draw(win)


#Used to move stickman left and right
while pg4flag !=1:
    clickP4 = win.checkKey()
    cx4a = testPoint4.getX()

    if clickP4 == "a":
        stickHead4.move(-10,0)
        stickBody4.move(-10,0)
        stickLegL.move(-10,0)
        stickLegR.move(-10,0)
        stickArmL4.move(-10,0)
        stickArmR4.move(-10,0)
        testPoint4.move(-10,0)

    elif clickP4 == "d":
        stickHead4.move(10,0)
        stickBody4.move(10,0)
        stickLegL.move(10,0)
        stickLegR.move(10,0)
        stickArmL4.move(10,0)
        stickArmR4.move(10,0)
        testPoint4.move(10,0)

    

#If reach this point, move onto next page and undraw current page
    if cx4a >= 45 and cx4a <= 50:
        pg4flag +=1
        stickHead4.undraw()
        stickBody4.undraw()
        stickLegL.undraw()
        stickLegR.undraw()
        stickArmL4.undraw()
        stickArmR4.undraw()
        testPoint4.undraw()
        bush.undraw()
        bush2.undraw()
        pg4background.undraw()
        pg4background1.undraw()
        page4text.undraw()
        page4text1.undraw()
        page4instruction.undraw()
        page4instructionb.undraw()
        pg4number.undraw()
        
#If reach this point, go back to last page
    elif cx4a >= 640 and cx4a <= 650:
        stickHead4.undraw()
        stickBody4.undraw()
        stickLegL.undraw()
        stickLegR.undraw()
        stickArmL4.undraw()
        stickArmR4.undraw()
        testPoint4.undraw()
        bush.undraw()
        bush2.undraw()
        pg4background.undraw()
        pg4background1.undraw()
        page4text.undraw()
        page4text1.undraw()
        page4instruction.undraw()
        page4instructionb.undraw()
        pg4number.undraw()


        #Page 3 Restart
        #Stickman Page 3
        #Stops Happy Journey Music(For Now)
        winsound.PlaySound(None, winsound.SND_PURGE)
        pg3flag += -1
        print(pg3flag)
        while pg3flag != 1:
            pg1background.draw(win)
            pg1background1.draw(win)
            #Stickman
            stickHead3 = Circle(Point(350, 250), 100)
            stickHead3.setFill("white")
            stickHead3.draw(win)

            stickBody3 = Line(Point(350, 350), Point(350, 500))
            stickBody3.setWidth(5)
            stickBody3.draw(win)

            stickR = Line(Point(350, 350), Point(450, 400))
            stickR.setWidth(5)
            stickR.draw(win)

            stickL = Line(Point(350, 350), Point(250, 400))
            stickL.setWidth(5)
            stickL.draw(win)

            #Text
            pg3txt = Text(Point(350, 100), "With the weapon in their inventory, "+name+" went off to find the Legendary Pringles.")
            pg3txt.setSize(13)
            pg3txt.draw(win)

            #Text to Continue
            pg3txt1 = Text(Point(350, 140), "Click the screen to continue!")
            pg3txt1.setStyle("bold")
            pg3txt1.setSize(15)
            pg3txt1.draw(win)

            #Draw Page number
            pg3number = Text(Point(10, 490), "3")
            pg3number.draw(win)

            #Click Points
            clickP3a = win.getMouse()

            if clickP3a != True:
                pg3flag += 1

            #Undraw Page 3
            stickHead3.undraw()
            stickBody3.undraw()
            stickR.undraw()
            stickL.undraw()
            pg3txt.undraw()
            pg3txt1.undraw()
            pg1background.undraw()
            pg1background1.undraw()
            pg3number.undraw()

            #Page 4 Start
            #Playing SNES Monopoly; SNES Monopoly Main Theme
            winsound.PlaySound("journey.wav", winsound.SND_ASYNC)
            #Sky
            pg4background = Rectangle(Point(0,0), Point(700, 350))
            pg4background.setFill("sky blue")
            pg4background.draw(win)
            #Dirt
            pg4background1 = Rectangle(Point(0,350), Point(700,500))
            pg4background1.setFill(color_rgb(139,69,19))
            pg4background1.draw(win)

            #Bush
            bush = Image(Point(100, 350), "bush.png")
            bush.draw(win)

            bush2 = Image(Point(500, 350), "bush.png")
            bush2.draw(win)

            #Stickman
            stickHead4 = Circle(Point(600, 275), 20)
            stickHead4.setFill("white")
            stickHead4.draw(win)

            stickBody4 = Line(Point(600, 295), Point(600, 400))
            stickBody4.setWidth(2)
            stickBody4.draw(win)

            stickLegL = Line(Point(600, 395), Point(575, 450))
            stickLegL.setWidth(2)
            stickLegL.draw(win)

            stickLegR = Line(Point(600, 395), Point(625, 450))
            stickLegR.setWidth(2)
            stickLegR.draw(win)

            stickArmL4 = Line(Point(600, 325), Point(575, 350))
            stickArmL4.setWidth(2)
            stickArmL4.draw(win)

            stickArmR4 = Line(Point(600,325), Point(625, 350))
            stickArmR4.setWidth(2)
            stickArmR4.draw(win)

            testPoint4 = Point(600,295)
            testPoint4.draw(win)

            page4text = Text(Point(350, 50), name+ " left home and went on the road")
            page4text1 = Text(Point(350, 75), "that will lead "+name+ " to find the Legendary Pringles.")
            page4text.draw(win)
            page4text1.draw(win)

            page4instruction = Text(Point(350, 125), "Move " +name+ " to the left with the key 'a' to continue with their journey.")
            page4instruction.setStyle("bold")
            page4instruction.setSize(15)
            page4instruction.draw(win)

            page4instructionb = Text(Point(350, 175), "Move " +name+ " to the right with the key 'd' to go back to the last page.")
            page4instructionb.setSize(15)
            page4instructionb.setStyle("bold")
            page4instructionb.draw(win)

            #Draw page Number
            pg4number = Text(Point(10, 490), "4")
            pg4number.draw(win)

  

#Page 5 Starts
page5background = Rectangle(Point(0,0), Point(700,500))
page5background.setFill("sky blue")
page5background.draw(win)

page5background = Rectangle(Point(0, 250), Point(700,500))
page5background.setFill(color_rgb(160,82,45))
page5background.draw(win)

#Cave
cave = Image(Point(350,250), "cave.png")
cave.draw(win)

#Stickman
stickHead5 = Circle(Point(680, 400), 10)
stickHead5.setFill("white")
stickHead5.draw(win)

stickBody5 = Line(Point(680, 410), Point(680,440))
stickBody5.setWidth(2)
stickBody5.draw(win)

stickLegL5 = Line(Point(680,440), Point(670,450))
stickLegL5.setWidth(2)
stickLegL5.draw(win)

stickLegR5 = Line(Point(680,440), Point(690, 450))
stickLegR5.setWidth(2)
stickLegR5.draw(win)

stickArmL5 = Line(Point(680, 425), Point(670, 415))
stickArmL5.setWidth(2)
stickArmL5.draw(win)

stickArmR5 = Line(Point(680,425), Point(690,435))
stickArmR5.setWidth(2)
stickArmR5.draw(win)

testPoint5 = Point(680,410)
testPoint5.draw(win)

#Page 5 Text
page5txt = Text(Point(350,50),  name+" arrived at the cave that contained the Legendary Pringles and walked in to resume their journey.")
page5txt.setSize(10)
page5txt.draw(win)

#Page 5 Instructions
page5inst = Text(Point(350,150), "Move " +name+ " into the cave with the WASD keys to resume their journey!")
page5inst.setSize(12)
page5inst.setStyle("bold")
page5inst.draw(win)

#Draw page Number
pg5number = Text(Point(10, 490), "5")
pg5number.draw(win)

#Move stickman in 360 degree direction
 
while pg5flag != 1:
    clickP5 = win.checkKey()
    cx5a = testPoint5.getX()
    cy5a = testPoint5.getY()
    if clickP5 == "a":
        stickHead5.move(-10,0)
        stickBody5.move(-10,0)
        stickLegL5.move(-10,0)
        stickLegR5.move(-10,0)
        stickArmL5.move(-10,0)
        stickArmR5.move(-10,0)
        testPoint5.move(-10,0)
    elif clickP5 == "s":
        stickHead5.move(0,10)
        stickBody5.move(0,10)
        stickLegL5.move(0,10)
        stickLegR5.move(0,10)
        stickArmL5.move(0,10)
        stickArmR5.move(0,10)
        testPoint5.move(0,10)
    elif clickP5 == "d":
        stickHead5.move(10,0)
        stickBody5.move(10,0)
        stickLegL5.move(10,0)
        stickLegR5.move(10,0)
        stickArmL5.move(10,0)
        stickArmR5.move(10,0)
        testPoint5.move(10,0)
    elif clickP5 =="w":
        stickHead5.move(0,-10)
        stickBody5.move(0,-10)
        stickLegL5.move(0,-10)
        stickLegR5.move(0,-10)
        stickArmL5.move(0,-10)
        stickArmR5.move(0,-10)
        testPoint5.move(0,-10)

    elif cx5a >= 325 and cx5a <= 390 and cy5a >= 260 and cy5a <= 315:
        stickHead5.undraw()
        stickBody5.undraw()
        stickLegL5.undraw()
        stickLegR5.undraw()
        stickArmL5.undraw()
        stickArmR5.undraw()
        testPoint5.undraw()
        pg5flag += 1
    #Leads to Pringle Artifact
    elif cx5a >= 0 and cx5a <= 10 and cy5a >= 250 and cy5a <= 500:
        #Undraw Page 5
        stickHead5.undraw()
        stickBody5.undraw()
        stickLegL5.undraw()
        stickLegR5.undraw()
        stickArmL5.undraw()
        stickArmR5.undraw()
        testPoint5.undraw()
        page5txt.undraw()
        page5inst.undraw()
        cave.undraw()
        pg5number.undraw()

        #Draw page 5a
        stickHead5a = Circle(Point(680, 400), 10)
        stickHead5a.setFill("white")
        stickHead5a.draw(win)

        stickBody5a = Line(Point(680, 410), Point(680,440))
        stickBody5a.setWidth(2)
        stickBody5a.draw(win)

        stickLegL5a = Line(Point(680,440), Point(670,450))
        stickLegL5a.setWidth(2)
        stickLegL5a.draw(win)

        stickLegR5a = Line(Point(680,440), Point(690, 450))
        stickLegR5a.setWidth(2)
        stickLegR5a.draw(win)

        stickArmL5a = Line(Point(680, 425), Point(670, 415))
        stickArmL5a.setWidth(2)
        stickArmL5a.draw(win)

        stickArmR5a = Line(Point(680,425), Point(690,435))
        stickArmR5a.setWidth(2)
        stickArmR5a.draw(win)

        testPoint5a = Point(680,410)
        testPoint5a.draw(win)

        #Draw page Number
        pg5anumber = Text(Point(10, 490), "5a")
        pg5anumber.draw(win)

        artifact = Image(Point(300,315), "pringleartifact.png")
        artifact.draw(win)

        page5atxt = Text(Point(350,150), "What is that?")
        page5atxt.setSize(25)
        page5atxt.draw(win)

        #Move stick man in 360 degree direction
        while pg5aflag != 1:
            clickP5a = win.checkKey()
            cx5b = testPoint5a.getX()
            cy5b = testPoint5a.getY()
            if clickP5a == "a":
                stickHead5a.move(-10,0)
                stickBody5a.move(-10,0)
                stickLegL5a.move(-10,0)
                stickLegR5a.move(-10,0)
                stickArmL5a.move(-10,0)
                stickArmR5a.move(-10,0)
                testPoint5a.move(-10,0)
            elif clickP5a == "s":
                stickHead5a.move(0,10)
                stickBody5a.move(0,10)
                stickLegL5a.move(0,10)
                stickLegR5a.move(0,10)
                stickArmL5a.move(0,10)
                stickArmR5a.move(0,10)
                testPoint5a.move(0,10)
            elif clickP5a == "d":
                stickHead5a.move(10,0)
                stickBody5a.move(10,0)
                stickLegL5a.move(10,0)
                stickLegR5a.move(10,0)
                stickArmL5a.move(10,0)
                stickArmR5a.move(10,0)
                testPoint5a.move(10,0)
            elif clickP5a =="w":
                stickHead5a.move(0,-10)
                stickBody5a.move(0,-10)
                stickLegL5a.move(0,-10)
                stickLegR5a.move(0,-10)
                stickArmL5a.move(0,-10)
                stickArmR5a.move(0,-10)
                testPoint5a.move(0,-10)
                  
            elif cx5b >= 255 and cx5b <= 350 and cy5b >= 270 and cy5b <= 390:
                #When user reaches the Pringle Artifact, it will change the endging to the Legend Ending(Look at Endings for more details)
                artifactcounter += 1
                artifact.undraw()
                pg5aflag += 1
                pg5flag += 1

                stickHead5a.undraw()
                stickBody5a.undraw()
                stickLegL5a.undraw()
                stickLegR5a.undraw()
                stickArmL5a.undraw()
                stickArmR5a.undraw()
                testPoint5a.undraw()
                page5background.undraw()
                pg5anumber.undraw()
                page5atxt.undraw()

                artifacttext = Text(Point(350,250), "You found the Pringles Artifact!")
                artifacttext.setFill("white")
                artifacttext.setSize(30)
                artifacttext.draw(win)

                for i in range(10):
                    time.sleep(0.25)
                    artifacttext.undraw()
                    time.sleep(0.25)
                    artifacttext.draw(win)

                artifacttext.undraw()

time.sleep(1)
cave.undraw()
    
#Page 6 Starts
#Stops Happy Journey Music
winsound.PlaySound(None, winsound.SND_PURGE)
#Playing Andrew Gold - Spooky Scary Skeletons
winsound.PlaySound("spooky.wav", winsound.SND_ASYNC)
#Cave Inside
pg6background = Rectangle(Point(0,0), Point(700, 350))
pg6background.setFill(color_rgb(139,69,19))
pg6background.draw(win)
#Ground
pg6background1 = Rectangle(Point(0,350), Point(700,500))
pg6background1.setFill(color_rgb(160,82,45))
pg6background1.draw(win)

#Torches
torch1light = Circle(Point(165,170), 65)
torch1light.setFill(color_rgb(255,215,0))
torch1light.setOutline(color_rgb(255,215,0))
torch1light.draw(win)

torch2light = Circle(Point(350,170), 65)
torch2light.setFill(color_rgb(255,215,0))
torch2light.setOutline(color_rgb(255,215,0))
torch2light.draw(win)

torch3light = Circle(Point(535,170), 65)
torch3light.setFill(color_rgb(255,215,0))
torch3light.setOutline(color_rgb(255,215,0))
torch3light.draw(win)
                 
torch1 = Image(Point(165, 150), "torch.png")
torch1.draw(win)

torch2 = Image(Point(350, 150), "torch.png")
torch2.draw(win)

torch3 = Image(Point(535, 150), "torch.png")
torch3.draw(win)

#Extra Cosmetic Devices
bat = Image(Point(640, 75), "bat.png")
bat.draw(win)

skeleton = Image(Point(620, 300), "skeleton.png")
skeleton.draw(win)


#Stickman
stickHead6 = Circle(Point(250,275), 25)
stickHead6.setFill("white")
stickHead6.draw(win)

stickBody6 = Line(Point(250, 300), Point(250, 375))
stickBody6.setWidth(2)
stickBody6.draw(win)

stickLegL6 = Line(Point(250,373), Point(225, 410))
stickLegL6.setWidth(2)
stickLegL6.draw(win)

stickLegR6 = Line(Point(250,373), Point(275, 410))
stickLegR6.setWidth(2)
stickLegR6.draw(win)

stickArmL6 = Line(Point(250, 340), Point(220, 340))
stickArmL6.setWidth(2)
stickArmL6.draw(win)

stickArmR6 = Line(Point(250,340), Point(280, 330))
stickArmR6.setWidth(2)
stickArmR6.draw(win)

testPoint6 = Point(250,300)
testPoint6.draw(win)

#Draw page Number
pg6number = Text(Point(10, 490), "6")
pg6number.draw(win)

#Text
pg6txt = Text(Point(350,10), "When " +name+ " had entered the cave, the opening closed up!") 
pg6txt.draw(win)

pg6txtb = Text(Point(350,30),  name+" moved along the dark alleyway to resume their quest to find the Legendary Pringles.")
pg6txtb.draw(win)

pg6instruction = Text(Point(350, 90), "Move " +name+ " to the right with the key 'd' to continue the journey!")
pg6instruction.setStyle("bold")
pg6instruction.draw(win)

#List for movement
stickMan6 = [stickHead6, stickBody6, stickLegL6, stickLegR6, stickArmL6, stickArmR6, testPoint6]

#Move stickman left and right
while pg6flag != 1:
    clickP6 = win.checkKey()
    cx6 = testPoint6.getX()
    cy6 = testPoint6.getY()
    if clickP6 == "a":
        for i in stickMan6:
            i.move(-10,0)
    elif clickP6 == "d":
        for i in stickMan6:
            i.move(10,0)
    elif cx6 >= 680 and cx6 <= 700 and cy6 >= 0 and cy6 <= 500:
        #When rerach this certain point, undraw stickman
        pg6background.undraw()
        pg6background1.undraw()
        torch1light.undraw()
        torch2light.undraw()
        torch3light.undraw()
        torch1.undraw()
        torch2.undraw()
        torch3.undraw()
        bat.undraw()
        skeleton.undraw()
        stickHead6.undraw()
        stickBody6.undraw()
        stickLegL6.undraw()
        stickLegR6.undraw()
        stickArmL6.undraw()
        stickArmR6.undraw()
        testPoint6.undraw()
        pg6number.undraw()
        pg6txt.undraw()
        pg6txtb.undraw()
        pg6instruction.undraw()
        pg6flag += 1

#Pg 7
#Background
pg7background = Rectangle(Point(0,0), Point(700,200))
pg7background.setFill(color_rgb(139,69,19))
pg7background.draw(win)

#Cave Hole
cavehole = Circle(Point(350, 200), 100)
cavehole.setFill("black")
cavehole.draw(win)

#Cave Floor
pg7background2 = Rectangle(Point(0,200), Point(700,500))
pg7background2.setFill(color_rgb(160,82,45))
pg7background2.draw(win)

#Stickman
stickHead7 = Circle(Point(650, 400), 10)
stickHead7.setFill("white")
stickHead7.draw(win)

stickBody7 = Line(Point(650, 410), Point(650,440))
stickBody7.setWidth(2)
stickBody7.draw(win)

stickLegL7 = Line(Point(650,440), Point(640,450))
stickLegL7.setWidth(2)
stickLegL7.draw(win)

stickLegR7 = Line(Point(650,440), Point(660, 450))
stickLegR7.setWidth(2)
stickLegR7.draw(win)

stickArmL7 = Line(Point(650, 425), Point(640, 415))
stickArmL7.setWidth(2)
stickArmL7.draw(win)

stickArmR7 = Line(Point(650,425), Point(660,435))
stickArmR7.setWidth(2)
stickArmR7.draw(win)

testPoint7 = Point(650,410)
testPoint7.draw(win)

#Obstacles
rock = Image(Point(100,300), "rock.png")
rock.draw(win)

kermit = Image(Point(500, 250), "kermit.png")
kermit.draw(win)

knuckles = Image(Point(250, 425), "uknuck.png")
knuckles.draw(win)

puffle = Image(Point(300, 300), "puffle.png")
puffle.draw(win)

chicken = Image(Point(425, 300), "chicken.png")
chicken.draw(win)

#Draw page Number
pg7number = Text(Point(10, 490), "7")
pg7number.draw(win)

#Text
pg7txt = Text(Point(350, 10), name+ " found the entryway to get to the Legendary Pringles")
pg7txt.draw(win)

pg7txtb = Text(Point(350, 25),  "but there are some obstacles in their way!")
pg7txtb.draw(win)

#Instructions
instructionpg7 = Text(Point(350, 60), "Avoid the Obstacles and move " +name+ " to the entryway using the WASD keys!")
instructionpg7.setStyle("bold")
instructionpg7.draw(win)

#List for movement
stickMan7 = [stickHead7, stickBody7, stickLegL7, stickLegR7, stickArmL7, stickArmR7, testPoint7]

cx7 = testPoint7.getX()
cy7 = testPoint7.getY()

#Move stickman in page
while pg7flag != 1:
    clickP7 = win.checkKey()
    clickP7a = win.checkMouse()
    cx7 = testPoint7.getX()
    cy7 = testPoint7.getY()
    if clickP7 == "a":
        for i in stickMan7:
            i.move(-10,0)
    elif clickP7 == "d":
        for i in stickMan7:
            i.move(10,0)
    elif clickP7 == "w":
        for i in stickMan7:
            i.move(0, -10)
    elif clickP7 == "s":
        for i in stickMan7:
            i.move(0,10)

    elif cx7 >= 245 and cx7 <= 455 and cy7 >= 100 and cy7 <= 200:
        pg7flag += 1
        pg7aflag += 5

    elif cx7 >= 25 and cx7 <= 265 and cy7 >= 175 and cy7 <= 335 or cx7 >= 265 and cx7 <= 340 and cy7 >= 265 and cy7 <= 340 or cx7 >= 395 and cx7 <= 455 and cy7 >= 265 and cy7 <= 340 or cx7 >= 395 and cx7 <= 455 and cy7 >= 265 and cy7 <= 340 or cx7 >= 450 and cx7 <= 540 and cy7 >= 210 and cy7 <= 310 or cx7 >= 195 and cx7 <= 300 and cy7 >= 380 and cy7 <= 475:
    #If stickman hits obstacle, move onto death scene(Code shown below in this elif statement
        pg7aflag += 1
        pg7flag += -1
        pg7abackground = Rectangle(Point(0,0), Point(750,500))
        pg7abackground.setFill(color_rgb(160,82,45))
        pg7abackground.draw(win)

        #Playing Ludwig Van Beethoven; 5th Symphony, 1st movement
        winsound.PlaySound("death.wav", winsound.SND_ASYNC)

        #Draw Tombstone
        tombstone = Image(Point(350,250), "tombstone.png")
        tombstone.draw(win)

        #Draw Text in the page
        deathtext = Text(Point(350, 20), name+" had hit an obstacle, got severely injured and had perished in the cave alone.")
        deathtext.setSize(13)
        deathtext.draw(win)

        #Draw the tombstone text
        tombstonetxt = Text(Point(350, 200), "Here")
        tombstonetxt2 = Text(Point(350, 225), "Lies")
        tombstonetxt3 = Text(Point(350, 270), name)

        tombstonetxt.setSize(20)
        tombstonetxt2.setSize(20)
        tombstonetxt3.setSize(15)

        tombstonetxt.setFace("times roman")
        tombstonetxt.setStyle("italic")
        tombstonetxt2.setStyle("italic")
        tombstonetxt2.setFace("times roman")
        tombstonetxt3.setStyle("bold")

        tombstonetxt.draw(win)
        tombstonetxt2.draw(win)
        tombstonetxt3.draw(win)

        #Try again button
        tryagainbutton = Rectangle(Point(10, 400), Point(120, 480))
        tryagainbutton.setFill("green")
        tryagainbutton.draw(win)

        #Quit button
        quitbutton = Rectangle(Point(510, 400), Point(620, 480))
        quitbutton.setFill("red")
        quitbutton.draw(win)

    #Text to try again
        tryagaintxt = Text(Point(70, 440), "Try Again?")
        tryagaintxt.draw(win)
    #Text to quit program
        quittxt = Text(Point(570, 440), "Quit?")
        quittxt.draw(win)

        c7a = win.getMouse()
        c7ax = c7a.getX()
        c7ay = c7a.getY()

        while pg7aflag == 1:
            if c7ax >= 10 and c7ax <= 120 and c7ay >= 400 and c7ay <= 480:
                #Gives user another chance if click this button
                pg7abackground.undraw()

                tombstone.undraw()

                deathtext.undraw()

                tombstonetxt.undraw()
                tombstonetxt2.undraw()
                tombstonetxt3.undraw()

                tryagainbutton.undraw()
                quitbutton.undraw()

                tryagaintxt.undraw()

                quittxt.undraw()

                #Stickman Move into different position
                stickHead7.move(30, 30)
                stickBody7.move(30, 30)
                stickLegL7.move(30, 30)
                stickLegR7.move(30, 30)
                stickArmL7.move(30, 30)
                stickArmR7.move(30, 30)
                testPoint7.move(30, 30)

                winsound.PlaySound(None, winsound.SND_PURGE)
                #Playing music 
                winsound.PlaySound("spooky.wav", winsound.SND_ASYNC)
                

                pg7aflag += -1

            elif c7ax >= 210 and c7ax <= 620 and c7ay >= 400 and c7ay <= 480:
            #Closes window if user clicks this 
                pg7aflag += -1
                win.close()


#While Loop ended, exiting While Loop
#Undrawing page 7
pg7background.undraw()
cavehole.undraw()
pg7background2.undraw()
stickHead7.undraw()
stickBody7.undraw()
stickLegL7.undraw()
stickLegR7.undraw()
stickArmL7.undraw()
stickArmR7.undraw()
testPoint7.undraw()

rock.undraw()
kermit.undraw()
knuckles.undraw()
puffle.undraw()
chicken.undraw()

pg7number.undraw()

pg7txt.undraw()
pg7txtb.undraw()

instructionpg7.undraw()


#Page 8
#Stops Spooky Music
winsound.PlaySound(None, winsound.SND_PURGE)
#Playing Kristopher Maddigan; Die House
winsound.PlaySound("dice.wav", winsound.SND_ASYNC)
pg8background = Rectangle(Point(0,0), Point(750, 500))
pg8background.setFill(color_rgb(160,82,45))
pg8background.draw(win)

#Draw guard
guard = (Image(Point(550, 150), "monopoly.png"))
guard.draw(win)

#Draw stickman
stickHead8 = Circle(Point(100, 400), 25)
stickHead8.setFill("white")
stickHead8.draw(win)

stickBody8 = Line(Point(100, 425), Point(100, 500))
stickBody8.setWidth(2)
stickBody8.draw(win)

#Draws text for page
pg8txt = Text(Point(350, 50), name+ " encounters the Pringles Guard! “Ha ha! You had made it past the difficult journey!” said the Pringles Guard.")
pg8txt.setSize(10)
pg8txt.draw(win)

pg8txt2 = Text(Point(350,75), '"Answer this question and I will give you the Legendary Pringles!"')
pg8txt2.setSize(10)
pg8txt2.draw(win)

#Question
pg8txt3 = Text(Point(350, 100), "What is 12192018 - 1252018?")
pg8txt3.setStyle("bold")

#The Legendary Pringles beside the guard
pringles = Image(Point(650, 200), "pringle.png")
pringles.draw(win)
pg8txt3.draw(win)

pg8instruction = Text(Point(330, 340), "Enter your answer here! Please enter in numbers with no spaces or other characters.")
pg8instruction.setStyle("bold")
pg8instruction.draw(win)

#Draw page Number
pg8number = Text(Point(10, 490), "8")
pg8number.draw(win)

#Name Entry
#Entry Box to let user input name
pringentry = Entry(Point(300,315), 30)
pringentry.setFill("white")
pringentry.draw(win)



while pg8flag != 1:
    while win.getKey() != "Return":
        time.sleep(0.5)

    pringleanswer = pringentry.getText()

    time.sleep(1)


    if pringleanswer == "10940000":
        #If answer is correct, exit while loop and move onto next page
        pg8flag += 1

    else:
        pg8aflag += 1
        #Death scene due to user getting the answer wrong
        pringentry.undraw()
        pg8abackground1 = Rectangle(Point(0,0), Point(750, 500))
        pg8abackground1.setFill("black")
        pg8abackground1.draw(win)

        pg8abackground = Rectangle(Point(500,200), Point(750,500))
        pg8abackground.setFill(color_rgb(160,82,45))
        pg8abackground.draw(win)

        guard2 = Image(Point(600, 170), "monopoly.png")
        guard2.draw(win)

        #Stickman
        stickHead8a = Circle(Point(350, 400), 20)
        stickHead8a.setFill("white")
        stickHead8a.draw(win)

        stickBody8a = Line(Point(370, 400), Point(410, 350))
        stickBody8a.setFill("grey")
        stickBody8a.setWidth(2)
        stickBody8a.draw(win)

        stickArmL8a = Line(Point(375, 395), Point(375, 365))
        stickArmL8a.setFill("grey")
        stickArmL8a.setWidth(2)
        stickArmL8a.draw(win)

        stickArmR8a = Line(Point(375,395), Point(370, 360))
        stickArmR8a.setFill("grey")
        stickArmR8a.setWidth(2)
        stickArmR8a.draw(win)

        stickLegL8a = Line(Point(410, 350), Point(420, 330))
        stickLegL8a.setFill("grey")
        stickLegL8a.setWidth(2)
        stickLegL8a.draw(win)

        stickLegR8a = Line(Point(410,350), Point(400, 330))
        stickLegR8a.setFill("grey")
        stickLegR8a.setWidth(2)
        stickLegR8a.draw(win)

        #Death text
        pg8atxt = Text(Point(350, 50), "You’re wrong!” said the guard.")
        pg8atxt.setFill("white")
        pg8atxt.draw(win)

        pg8atxt2 = Text(Point(350,75), "Then, the ground crumbled away under " +name+ " and they fall to their inevitable demise.")
        pg8atxt2.setFill("white")
        pg8atxt2.draw(win)

        #Try again button and quit button below
        tryagainbutton8 = Rectangle(Point(10, 400), Point(120, 480))
        tryagainbutton8.setFill("green")
        tryagainbutton8.draw(win)

        quitbutton8 = Rectangle(Point(510, 400), Point(620, 480))
        quitbutton8.setFill("red")
        quitbutton8.draw(win)

        tryagaintxt8 = Text(Point(70, 440), "Try Again?")
        tryagaintxt8.draw(win)

        quittxt8 = Text(Point(570, 440), "Quit?")
        quittxt8.draw(win)

        c8a = win.getMouse()
        c8ax = c8a.getX()
        c8ay = c8a.getY()

        while pg8aflag == 1:
            #If user clicks try again button. undraw everything in death page and redraw everything in page 8, giving user another chance to enter the correct answer
            if c8ax >= 10 and c8ax <= 120 and c8ay >= 400 and c8ay <= 480:
                pg8abackground1.undraw()
                pg8abackground.undraw()
                guard2.undraw()
                stickHead8a.undraw()
                stickBody8a.undraw()
                stickArmL8a.undraw()
                stickArmR8a.undraw()
                stickLegL8a.undraw()
                stickLegR8a.undraw()
                pg8atxt.undraw()
                pg8atxt2.undraw()
                tryagainbutton8.undraw()
                quitbutton8.undraw()
                tryagaintxt8.undraw()
                quittxt8.undraw()

                pringentry.draw(win)
                
                pg8aflag += -1

                

            elif c8ax >= 210 and c8ax <= 620 and c8ay >= 400 and c8ay <= 480:
                #If user clicks the exit box. exits window
                pg8aflag += -1
                win.close()
#End of Page 8       
while pg8flag != 2:
    pg8background.undraw()
    guard.undraw()
    stickHead8.undraw()
    stickBody8.undraw()
    pg8txt.undraw()
    pg8txt2.undraw()
    pg8txt3.undraw()
    pringles.undraw()
    pg8instruction.undraw()
    pringentry.undraw()
    pg8number.undraw()
    winsound.PlaySound(None, winsound.SND_PURGE)
    pg8flag += 1
    

#Start of page 9
#Playing Janji; Heroes Tonight
winsound.PlaySound("heroestonight.wav", winsound.SND_ASYNC)

#Background
page9background = Rectangle(Point(0,0), Point(700,500))
page9background.setFill("sky blue")
page9background.draw(win)

page9txt = Text(Point(350, 25), ' “You’re correct! Out of all of the one million challengers, you were the only one that got this correct!') 
page9txt.draw(win)

pg9txtb = Text(Point(125,50), 'you deserve these Pringles!”')
pg9txtb.draw(win)

pg9txtc = Text(Point(350, 75), name+ " recieves the Pringles and opens the cap…")
pg9txtc.draw(win)

pg9txtd = Text(Point(350, 100), "Click the screen to advance!")
pg9txtd.setStyle("bold")
pg9txtd.draw(win)

pringle2 = Image(Point(400, 200), "pringle2.png")
pringle2.draw(win)

#Stickman
stickHead9 = Circle(Point(250, 250), 50)
stickHead9.setFill("white")
stickHead9.draw(win)

stickBody9 = Line(Point(250, 300), Point(250, 500))
stickBody9.setWidth(2)
stickBody9.draw(win)

stickArm9L = Line(Point(250, 350), Point(375, 250))
stickArm9L.setWidth(2)
stickArm9L.draw(win)

stickArm9R = Line(Point(250,350), Point(375, 260))
stickArm9R.setWidth(2)
stickArm9R.draw(win)

#Stars beside Pringles
star = Image(Point(330, 150), "star.png")
star.draw(win)

star2 = Image(Point(435, 160), "star.png")
star2.draw(win)

star3 = Image(Point(345, 200), "star.png")
star3.draw(win)

#Draw page Number
pg9number = Text(Point(10, 490), "9")
pg9number.draw(win)

while pg9flag != 1:
    clickP9 = win.getMouse()
    cx9=clickP9.getX()
    cy9=clickP9.getY()

    if cx9 >= 0 and cx9 <= 700 and cy9 >= 0 and cx9 <= 500:
        pg9flag += 1

#Undrawing Page 9
winsound.PlaySound(None, winsound.SND_PURGE)
page9background.undraw()
page9txt.undraw()
pg9txtb.undraw()
pg9txtc.undraw()
pg9txtd.undraw()
pringle2.undraw()
star.undraw()
star2.undraw()
star3.undraw()
stickHead9.undraw()
stickBody9.undraw()
stickArm9L.undraw()
stickArm9R.undraw()
pg9number.undraw()

#Endings
#In order to get Pringbills, user needs to click the 3 objects on the FIRST page:
#Bookshelf
#Paper
#Trash Can
#User should know if successful if music stops and repeats and story doesn't advance to next page

#In order to get Artifact, on page 5, move all the way to the left and then user accesses page 5a. Touch the artifact to get the artifact!

#In the if statements that has win.close() inside, if user clicks on the button, it closes the window.


#Legend Ending, Need Pringles Artifact, Doesn't matter how many Pringbills user has- Turn Pringles to gold!
if artifactcounter == 1:
    #Playing Eduard Khil; I am very glad, because I'm finally returning back home [TROLOLO]
    winsound.PlaySound("legend.wav", winsound.SND_ASYNC)

    page10Lbackground = Rectangle(Point(0,0), Point(700,500))
    page10Lbackground.setFill("white")
    page10Lbackground.draw(win)

    legend = Image(Point(350,250), "pringlelegend.png")
    legend.draw(win)

    quitbutton10L = Rectangle(Point(510, 400), Point(620, 480))
    quitbutton10L.setFill("Green")
    quitbutton10L.draw(win)

    quittxt10L = Text(Point(565, 440), "Exit")
    quittxt10L.draw(win)

    legendtxt = Text(Point(350, 25), "When "+name+" opened it, the Pringles turned to gold!")
    legendtxt.draw(win)

    legendtext2 = Text(Point(350, 50), "Maybe something to do with the Artifact?")
    legendtext2.setFill("red")
    legendtext2.draw(win)

    #Different text depending on Pringles number
    if pringbillflag == 3:

        legendtxt3 = Text(Point(350, 75), "You got the legend ending with three Pringbills!")
        legendtxt3.draw(win)

    elif pringbillflag == 2:
        legendtxt3 = Text(Point(350, 75), "You got the legend ending with two Pringbills!")
        legendtxt3.draw(win)

    elif pringbillflag == 1:
        legendtxt3 = Text(Point(350, 75), "You got the legend ending with one Pringbill!")
        legendtxt3.draw(win)

    else:
        legendtxt3 = Text(Point(350, 75), "You got the legend ending with zero Pringbills!")
        legendtxt3.draw(win)

    #Draw page Number
    pg10Lnumber = Text(Point(10, 490), "10L")
    pg10Lnumber.draw(win)

    c10L = win.getMouse()
    c10LX = c10L.getX()
    c10LY = c10L.getY()

    if c10LX >= 210 and c10LX <= 620 and c10LY >= 400 and c10LY <= 480:
        winsound.PlaySound(None, winsound.SND_PURGE)
        win.close()

#Mega Ending- Need 3 Pringbills- Make Pringbills turn into a mega size
elif pringbillflag == 3:

    #Playing Benny Goodman; SING SING SING
    winsound.PlaySound("singsing.wav", winsound.SND_ASYNC)

    pg10mbackground = Rectangle(Point(0,0), Point(700,500))
    pg10mbackground.setFill("sky blue")
    pg10mbackground.draw(win)

    #Size is 531 x 531 pixels
    mega = (Image(Point(350, 250), "MPringles.png"))
    mega.draw(win)

    megatxt = Text(Point(350, 25), "When "+name+" opened the can, the Pringles grew to a mega size!")
    megatxt.setSize(15)
    megatxt.draw(win)

    megatxt2 = Text(Point(350,50), "You got the mega ending with 3 Pringbills!")
    megatxt2.setSize(15)
    megatxt2.setStyle("bold")
    megatxt2.draw(win)

    #Stickman
    stickHead10M = Circle(Point(100, 450), 50)
    stickHead10M.setFill("white")
    stickHead10M.draw(win)

    stickEyeL10M = Circle(Point(75, 425), 7)
    stickEyeL10M.setFill("black")
    stickEyeL10M.draw(win)

    stickEyeR10M = Circle(Point(125, 425), 7)
    stickEyeR10M.setFill("black")
    stickEyeR10M.draw(win)

    stickMouth10M =Circle(Point(100, 465), 15)
    stickMouth10M.setFill("black")
    stickMouth10M.draw(win)

    quitbutton10L = Rectangle(Point(510, 400), Point(620, 480))
    quitbutton10L.setFill("Green")
    quitbutton10L.draw(win)

    quittxt10L = Text(Point(565, 440), "Exit")
    quittxt10L.draw(win)

    #Draw page Number
    pg10Mnumber = Text(Point(15, 490), "10M")
    pg10Mnumber.draw(win)

    tenM = win.getMouse()
    tenMx = tenM.getX()
    tenMy = tenM.getY()

    if tenMx >= 210 and tenMx <= 620 and tenMy >= 400 and tenMy <= 480:
        winsound.PlaySound(None, winsound.SND_PURGE)
        win.close()


    

    

#Jumbo Ending- Need 2 Pringbills, makes Pringles into jumbo size
elif pringbillflag == 2:
    #Playing Benny Goodman; SING SING SING
    winsound.PlaySound("singsing.wav", winsound.SND_ASYNC)

    pg10jbackground = Rectangle(Point(0,0), Point(700,500))
    pg10jbackground.setFill("sky blue")
    pg10jbackground.draw(win)

    #Image is 294 x 294 pixels
    jumbo = (Image(Point(400, 300), "JPringles.png"))
    jumbo.draw(win)

    jumbotxt = Text(Point(350, 25), "When "+name+" opened the can, the Pringles grew to a jumbo size!")
    jumbotxt.setSize(15)
    jumbotxt.draw(win)

    jumbotxt2 = Text(Point(350,50), "You got the jumbo ending with 2 Pringbills!")
    jumbotxt2.setSize(15)
    jumbotxt2.setStyle("bold")
    jumbotxt2.draw(win)
    
    
    stickHead10J = Circle(Point(250, 270), 50)
    stickHead10J.setFill("white")
    stickHead10J.draw(win)

    stickBody10J = Line(Point(250, 320), Point(250, 500))
    stickBody10J.setWidth(2)
    stickBody10J.draw(win)

    stickArm10J = Line(Point(250, 370), Point(375, 270))
    stickArm10J.setWidth(2)
    stickArm10J.draw(win)

    stickArm10J = Line(Point(250,370), Point(375, 280))
    stickArm10J.setWidth(2)
    stickArm10J.draw(win)

    quitbutton10J = Rectangle(Point(510, 400), Point(620, 480))
    quitbutton10J.setFill("Green")
    quitbutton10J.draw(win)

    quittxt10J = Text(Point(565, 440), "Exit")
    quittxt10J.draw(win)

    #Draw page Number
    pg10Jnumber = Text(Point(10, 490), "10J")
    pg10Jnumber.draw(win)

    c10J = win.getMouse()
    c10Jx = c10J.getX()
    c10Jy = c10J.getY()


    if c10Jx >= 510 and c10Jx <= 620 and c10Jy >= 400 and c10Jy <= 480:
        winsound.PlaySound(None, winsound.SND_PURGE)
        win.close()

    


#Large Ending- Need 1 Pringbill, makes Pringles bigger
elif pringbillflag == 1:
    #Playing Benny Goodman; SING SING SING
    winsound.PlaySound("singsing.wav", winsound.SND_ASYNC)

    pg10Lbackground = Rectangle(Point(0,0), Point(700,500))
    pg10Lbackground.setFill("sky blue")
    pg10Lbackground.draw(win)

    quitbutton10L = Rectangle(Point(510, 400), Point(620, 480))
    quitbutton10L.setFill("Green")
    quitbutton10L.draw(win)

    quittxt10L = Text(Point(565, 440), "Exit")
    quittxt10L.draw(win)

    largetxt = Text(Point(350, 25), "When "+name+" opened the can, the Pringles grew!")
    largetxt.setSize(15)
    largetxt.draw(win)

    largetxt2 = Text(Point(350,50), "You got the large ending with 1 Pringbill!")
    largetxt2.setSize(15)
    largetxt2.setStyle("bold")
    largetxt2.draw(win)

    #Draw page Number
    pg10Lnumber = Text(Point(10, 490), "10L")
    pg10Lnumber.draw(win)

    #Draw stickman
    stickHead10L = Circle(Point(250, 270), 50)
    stickHead10L.setFill("white")
    stickHead10L.draw(win)

    stickBody10L = Line(Point(250, 320), Point(250, 500))
    stickBody10L.setWidth(2)
    stickBody10L.draw(win)

    stickArm10L = Line(Point(250, 370), Point(375, 270))
    stickArm10L.setWidth(2)
    stickArm10L.draw(win)

    stickArm10L = Line(Point(250,370), Point(375, 280))
    stickArm10L.setWidth(2)
    stickArm10L.draw(win)

    #Draw Pringles
    #Size is 237 x 237 pixels
    largepringles = Image(Point(375, 250), "LPringles.png")
    largepringles.draw(win)

    c10L = win.getMouse()
    c10LX = c10L.getX()
    c10LY = c10L.getY()


    if c10LX >= 510 and c10LX <= 620 and c10LY >= 400 and c10LY <= 480:
        winsound.PlaySound(None, winsound.SND_PURGE)
        win.close()


#Sugar Ending- No Pringbills and selected "sugar" as weapon- Make Pringles sweet
elif sugarflag == 1:
    #Playing Alan Walker; Flying Dreams
    winsound.PlaySound("dreams.wav", winsound.SND_ASYNC)

    sugarbackground = Rectangle(Point(0,0), Point(750,500))
    sugarbackground.setFill("sky blue")
    sugarbackground.draw(win)

    sugartxt = Text(Point(350, 50), name+" took a bite, and the chips tasted of the perfect blend of sweet and crispy.")
    sugartxt.setFill("white")
    sugartxt.setSize(13)
    sugartxt.draw(win)

    sugartxt2 = Text(Point(350,75), "You got the sugary ending with Zero Pringbills!")
    sugartxt2.setStyle("bold")
    sugartxt2.setSize(15)
    sugartxt2.draw(win)

    sugarpringle = Image(Point(400,230), "pringlechip.png")
    sugarpringle.draw(win)

    stickHead10sug = Circle(Point(250, 270), 50)
    stickHead10sug.setFill("white")
    stickHead10sug.draw(win)

    stickBody10sug = Line(Point(250, 320), Point(250, 500))
    stickBody10sug.setWidth(2)
    stickBody10sug.draw(win)

    stickArm10sug = Line(Point(250, 370), Point(375, 270))
    stickArm10sug.setWidth(2)
    stickArm10sug.draw(win)

    stickArm10sug = Line(Point(250,370), Point(375, 280))
    stickArm10sug.setWidth(2)
    stickArm10sug.draw(win)

    quitbutton10sug = Rectangle(Point(510, 400), Point(620, 480))
    quitbutton10sug.setFill("Green")
    quitbutton10sug.draw(win)

    quittxt10sug = Text(Point(565, 440), "Exit")
    quittxt10sug.draw(win)

    #Draw page Number
    pg10sugnumber = Text(Point(25, 490), "10Sug")
    pg10sugnumber.draw(win)

    c10Sug = win.getMouse()
    c10SugX = c10Sug.getX()
    c10SugY = c10Sug.getY()


    if c10SugX >= 510 and c10SugX <= 620 and c10SugY >= 400 and c10SugY <= 480:
        winsound.PlaySound(None, winsound.SND_PURGE)
        win.close()

    

#Salt Ending- No Pringbills and selected "salt" as weapon- Make Pringles salty
else:
    #Playing Alan Walker; Flying Dreams
    winsound.PlaySound("dreams.wav", winsound.SND_ASYNC)

    saltbackground = Rectangle(Point(0,0), Point(750,500))
    saltbackground.setFill("sky blue")
    saltbackground.draw(win)

    salttxt = Text(Point(350, 50), name+" took a bite, and the chips tasted salty and filling, like the perfect Pringle.")
    salttxt.setFill("white")
    salttxt.setSize(13)
    salttxt.draw(win)

    salttxt2 = Text(Point(350,75), "You got the salty ending with Zero Pringbills!")
    salttxt2.setStyle("bold")
    salttxt2.setSize(15)
    salttxt2.draw(win)

    saltpringle = Image(Point(400,230), "pringlechip.png")
    saltpringle.draw(win)

    stickHead10sal = Circle(Point(250, 270), 50)
    stickHead10sal.setFill("white")
    stickHead10sal.draw(win)

    stickBody10sal = Line(Point(250, 320), Point(250, 500))
    stickBody10sal.setWidth(2)
    stickBody10sal.draw(win)

    stickArm10sal = Line(Point(250, 370), Point(375, 270))
    stickArm10sal.setWidth(2)
    stickArm10sal.draw(win)

    stickArm10sal = Line(Point(250,370), Point(375, 280))
    stickArm10sal.setWidth(2)
    stickArm10sal.draw(win)

    quitbutton10sal = Rectangle(Point(510, 400), Point(620, 480))
    quitbutton10sal.setFill("Green")
    quitbutton10sal.draw(win)

    quittxt10sal = Text(Point(565, 440), "Exit")
    quittxt10sal.draw(win)

    #Draw page Number
    pg10salnumber = Text(Point(25, 490), "10Sal")
    pg10salnumber.draw(win)

    c10Sal = win.getMouse()
    c10SalX = c10Sal.getX()
    c10SalY = c10Sal.getY()


    if c10SalX >= 510 and c10SalX <= 620 and c10SalY >= 400 and c10SalY <= 480:
        winsound.PlaySound(None, winsound.SND_PURGE)
        win.close()

    

    
    
    

    











    





            

        
