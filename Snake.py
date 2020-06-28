import turtle
import time
import random

# Score
score = 0
high_score = 0

delay = 0.1

window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('green')
window.setup(width=600, height=600)
window.tracer(0) # Turns off screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('red')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('black')
food.penup()
food.goto(0,100)

# Snake body
body = []

# Create scoring for the game
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0 High Score: 0', align='center', font=('courier', 24, 'normal'))

def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

# Movement
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

# keyboard bindings
window.listen()
window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_left, 'Left')
window.onkeypress(go_right, 'Right')

while True:
    window.update()

    # Check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = 'stop'

        # moving them off the screen because not sure how to delete
        for element in body:
            element.goto(1000,1000)

        body.clear()

        score = 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Check for collision with the food
    if head.distance(food) < 20: # Each turtle head is 20 pixels wide by 20 pixels tall.
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add body to head
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape('square')
        new_part.color('grey')
        new_part.penup()
        body.append(new_part)

        # Speed up game as the body gets larger
        delay -= 0.005

        # Increase score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write('Score: {} High Score: {}'.format(score, high_score), align='center', font=('courier', 24, 'normal'))

    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)

    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    move()

    # Check if head collided with body
    for element in body:
        if element.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = 'stop'

            # moving them off the screen because not sure how to delete
            for element in body:
                element.goto(1000, 1000)

            body.clear()

            score = 0

            pen.clear()
            pen.write('Score: {} High Score: {}'.format(score, high_score), align='center', font=('courier', 24, 'normal'))

    time.sleep(0.1)

window.mainloop()




