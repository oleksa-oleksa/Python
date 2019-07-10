import turtle

def draw_square(turtle):

    # Draw 4 sides of a square
    for side in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(6)

    for squares in range(36):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()


draw_art()
