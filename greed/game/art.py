import turtle

def main():

    
    _t = turtle.Turtle()

    class Draw_shapes:
        def draw_circle(self, _t, _x, _y, tilt, radius, extent, fillcolor, pencolor):
            """
            This is the atomic shape circle used for the ball on the sword and the shield in various places throughout.
            _x, and _y are for coordinates
            radius is used for the circle size
            fillcolor is for the color inside of the circles
            pencolor is for the circle borders
            """
            _t.up()
            _t.goto(_x,_y)
            _t.setheading(tilt)
            _t.down()
            _t.color(pencolor, fillcolor)
            _t.begin_fill()
            _t.circle(radius, extent)
            _t.end_fill()
            _t.speed(0)

        def draw_rectangle(self, _t, _x, _y, height, width, tilt, fillcolor, pencolor):
            """
            Atomic shape used primarily for the hilt of the sword.
            _x, and _y are for coordinates
            height and width are used for the rectangle size
            tilt is for the direction that the rectangle is tilted or not.
            fillcolor is for the color inside of the circles
            pencolor is for the circle borders
            """
            _t.setheading(tilt)
            _t.up()
            _t.goto(_x, _y)
            _t.down()
            _t.color(pencolor, fillcolor)
            _t.begin_fill()
            for _i in range(2):
                _t.forward(width)
                _t.left(90)
                _t.forward(height)
                _t.left(90)

            _t.right(90)
            _t.end_fill()
            _t.up()

        def draw_line(self, _t, _x, _y, length, tilt):
            _t.setheading(tilt)
            _t.up()
            _t.goto(_x, _y)
            _t.down()
            _t.setheading(tilt)
            _t.forward(length)

    class Wires:
        def line(self, _t, x, y, length, tilt):
            """
            draws the wires to the parachute.
            """
            _t.up()
            _t.goto(x,y)
            _t.down()
            _t.setheading(tilt)
            _t.forward(length)



    class reset:
        def resets(self):
            Draw_shapes.draw_rectangle("self", _t, -200, -200, 400, 400, 0, "white", "white")
            Draw_shapes.draw_rectangle("self", _t, -800, -800, 1, 1, 0, "white", "black")

    class Draw_objects(Draw_shapes):
        def __init__(self):
            super().__init__()
        

        def draw_boulder(self):
            """
            Draws the boulder
            """
            draw_circle(self, _t, 0, 0, 0, 5, 360, "brown", "black")
            line(self, _t, 0, 0, 50, 0)
            

        def draw_gem(self):
            """
            Draws a diamond
            """
            draw_rectangle(self, _t, _x, _y, height, width, tilt, fillcolor, pencolor)
            Draw_shapes.line(self, _t, x, y, length, tilt)
            Draw_shapes.line(self, _t, x, y, length, tilt)
            
        def draw_player(self, ):
            Draw_shapes.draw_circle(self, _t, _x, _y, tilt, radius, extent, fillcolor, pencolor)
            Draw_shapes.line(self, _t, x, y, length, tilt)
            Draw_shapes.line(self, _t, x, y, length, tilt)
            Draw_shapes.line(self, _t, x, y, length, tilt)
            
    Draw_objects.draw_boulder("self")


if __name__ == "__main__":
    main()