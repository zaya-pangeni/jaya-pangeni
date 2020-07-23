#Snake game

import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

#set up the screen
wn = turtle.Screen()
wn.title("snake game by @zaaya & @Sandhya")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)   #turns off the screen updates


#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


pen1 = turtle.Turtle()
pen1.speed(0)
pen1.shape("square")
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(150, 150)



#function
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"
food.penup()
food.shapesize(0.75, 0.75)
food.goto(0, 100)

def move():
    if head.direction == "up":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y + 20)
 
    if head.direction == "down":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y - 20)
 
    if head.direction == "right":
        x = head.xcor() #x coordinate of the turtle
        head.setx(x + 20)
 
    if head.direction == "left":
        x = head.xcor() #x coordinate of the turtle
        head.setx(x - 20)
 

        # keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")


        #Main game loop
while True:
    wn.update()

   # Check for collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        pen1.write("GAME OVER",align="center",font=("Courier", 24, "normal"))
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
           segment.goto(1000, 1000)
 
        # clear segment list
        segments.clear()
  
        # Reset the score
        score = 0

        pen.clear()
        pen1.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal" ))

    # check for collision with food
    if head.distance(food)< 20:
        # Move the food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)


        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)


    # Move segment to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            pen1.write("GAME OVER",align="center",font=("Courier",24,"normal"))
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segment
            for segment in segments:
                segment.goto(1000, 1000)

         #Clear the segments list
            segments.clear()

          #Reset the score
            score = 0

           #Update the score display
            pen.clear()
            pen1.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()



        
 