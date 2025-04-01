from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape('turtle')
screen.listen()
tim.speed('fastest')

def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def left():
    tim.left(10)
def right():
    tim.right(10)
def forward_right():
    tim.right(10)
    tim.forward(10)

def forward_left():
    tim.left(10)
    tim.forward(10)

def clear_drawing():
    tim.reset()

screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='d', fun=right)
screen.onkey(key='a', fun=left)
screen.onkey(key='e', fun=forward_right)
screen.onkey(key='q', fun=forward_left)
screen.onkey(key='c', fun=clear_drawing)

screen.exitonclick()
