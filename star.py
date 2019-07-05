import os 
import math
import turtle
import random


#set up the screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("space invaders")


#Draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()        #the turthle is created at the centre and if we move it without penup() then it willl make a line from centre to that position
border_pen.setposition(-300,-300)
border_pen.pensize(3)    # it decides the width of the line drawn
border_pen.shapesize(1,1)  #decides the size of the turtle
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()     #it will hide the turtle 

#set the score as 0
score=0

###draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring="Score: %s"  %score
score_pen.write(scorestring,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()


#create the player turtle
player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.lt(90)

playerspeed=15    #moves player to 15 coordinates left or right

####choose the no of eneimies
number_of_enemies=5
####create an empty list of enemies
enemies=[]

#####add enemies to list
for i in range(number_of_enemies):
    #####create the enemies
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)
    enemy.shapesize(1,1)

enemyspeed=10

#create the players bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.lt(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=50

#define the stte of the bullet
#ready-ready to fire
#fire-billet is firing
bulletstate="ready"



#move player to left
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x<-280:
        x=-280
    player.setx(x)

#move player to right
def move_right():
    x=player.xcor()
    x+=playerspeed
    if x>280:
        x=280
    player.setx(x)   

def fire_bullet():

    #declare bulletstate as global as it is to be changed
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        #move the bullet to just above the player
        x=player.xcor()
        y=player.ycor()
        bullet.setposition(x,y+10)
        bullet.showturtle()    

def isCollosion(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 30:
        return True
    else:  
        return False



#player keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")             #this is case sensitive so "L" "R"  should be capital
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")           #here for space bar "s"  is lower case
#main game loop

while True:
    for enemy in enemies:
        #move the enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
        
        #reverse if it reaches the borders
        if enemy.xcor()>280:
            #########move all of the enemies down
            for e in enemies:
                
                y=e.ycor()
                y-=40
                e.sety(y)
            #change the direction    
            enemyspeed *=-1

        if enemy.xcor()<-280:
            #########move all of the enemies down
            for e in enemies: 
                y=e.ycor()
                y-=40
                e.sety(y)
            #change the direction 
            enemyspeed *=-1  
        #collision between the bullet and the enemy
        if isCollosion(bullet,enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            ##reset the enemy
            x=random.randint(-200,200)
            y=random.randint(100,250)
            enemy.setposition(x,y)
            #update the score
            score+=10
            scorestring="Score: %s"  %score
            score_pen.clear()                 #####clear that the pen contains
            score_pen.write(scorestring,align="left",font=("Arial",14,"normal"))

        #####check whether the enemy and player have collided
        if isCollosion(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break
        

  
    #move the bullet
    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)
    #check to see the bullet has reaches the top or not
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"   
#####check whether the enemy and player have collided
    if isCollosion(player,enemy):
        player.hideturtle()
        enemy.hideturtle()
        pcore_pen=turtle.Turtle()
        pcore_pen.speed(0)
        pcore_pen.color("white")
        pcore_pen.penup()
        pcore_pen.setposition(0,120)
        pcorestring="GAME OVER"
        pcore_pen.write(pcorestring,align="left",font=("Arial",30,"normal"))
        pcore_pen.hideturtle()
        break
    if enemy.ycor in range(-270,-280):
        print("Game Over")
        break





delattr=raw_input("press enter to finish.")