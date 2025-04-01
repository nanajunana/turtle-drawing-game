from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape('turtle')
screen.listen()
turtle_head = 0

def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def left():
    global turtle_head
    turtle_head += 10
    tim.setheading(turtle_head)
def right():
    global turtle_head
    turtle_head -= 10
    tim.setheading(turtle_head)

screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='d', fun=right)
screen.onkey(key='a', fun=left)

screen.exitonclick()
