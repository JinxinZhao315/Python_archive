import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Set up the screen.
wn = turtle.Screen() # CAPITALIZE S!
wn.title('Snake Game')
wn.bgcolor('white')
wn.setup(width=600,height=600)
wn.tracer(0) # Turns off the screen updates

# Revise: Class, instance and class methods. wn is an instance of turtle class
# Take note of the instance_name.method() way to invoke class methods
# Familiarize ppl with turtle(and others) class & method first

# Snake head
head = turtle.Turtle() # CAPITALIZE !
head.speed(0) # fastest animation speed
head.shape('square')
head.color('black')
head.penup() # does not draw anything
head.goto(0,0)
head.direction = 'stop'
# 'stop' means nothing happends until you press. If it's up the head will automatically go up before you press.


# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(random.randint(-280,280),random.randint(-280,280))

segments = []

# Pen
pen= turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Score:0 High Score:0',align='center',font=('Courier',24,'normal'))
#parenthesis!

# Functions

def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
# All these are to prevent the head from running into itself when you suddenly reverse the direction
# of the head. e.g. You can only go down if you are not going up. Nothing happens if you press down when going up.

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

def reset_score(pen,score,high_score):
        pen.clear() # If you don't clear the screen, it will write on top of itself
        pen.write('Score: {} High Score: {}'.format(score,high_score), align='center',font=('Courier',24,'normal'))


#Keyboard bindings
# bind keyboard with functions
wn.listen()
wn.onkeypress(go_up,'w') #no parenthesis here
wn.onkeypress(go_down,'s')
wn.onkeypress(go_left,'a')
wn.onkeypress(go_right,'d')


# Main game loop
while True:
    wn.update() # Keep updating the screen
    # Note that this loop runs SUPER fast i.e. computer processing speed. If you call
    # the move() function without delaying it, the turtle shoots out of the screen before u can see.


    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        # Hide the segments
        for segment in segments:
            segment.hideturtle()

        # Clear the segments list
        segments.clear()

        # Reset score
        score = 0
        reset_score(pen,score,high_score)

        # Reset delay
        delay = 0.1

    # Check for head collision with segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'
            for segment in segments:
                segment.hideturtle()
            segments.clear()

            #Reset score
            score = 0
            reset_score(pen,score,high_score)

            # Reset delay
            delay = 0.1


    if head.distance(food) < 20: # Built-in function to find the distance between two turtles. 20 because each turtle object by default is 20pix wide by 20pix tall, so the distance between two centers is 20
        # so they have collided. Move food to a random spot. IMPORT RANDOM
        x = random.randint(-280,280) # screen is 600*600 so each border is 300pix from (0,0)
        y = random.randint(-280,280)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('purple')
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -=0.001

        # Increase score
        score += 10

        if score > high_score:
            high_score = score

        reset_score(pen,score,high_score)

    # Move the end segments to the tail of the last one, in reverse order
    for index in range(len(segments)-1,0,-1):
        # This iteration actually does not include index 0 cuz the range function ends at stop_number+1!
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        '''Kind of like a recursion'''

    # Move segment 0 to where the head is
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        '''Kind of like the base case of recursion'''
        

    move()
    # Move() is behind the entire adding segment thing, so the head moves forward first. However, since we do not update
    # the screen until the start of the loop, we don't see it. And when the loop starts, it runs super fast so you don't see
    # the segments catching up. 


    


    
    time.sleep(delay)
    # IMPORT TIME






wn.mainloop() # Keep the window open
