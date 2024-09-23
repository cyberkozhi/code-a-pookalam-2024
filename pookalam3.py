import random





def generate_number():
    global num
    num = random.choice([1, 2, 3])
    print(num)

generate_number()



if num ==1:
    import turtle
    import math
    import random
    turtle.speed(0)
    turtle.home()
    def circ(cl,r): 
        turtle.begin_fill()
        turtle.fillcolor(cl)
        turtle.speed(0)
        turtle.pen(pencolor=cl,pensize="1")
        turtle.pu()
        turtle.rt(90)
        turtle.fd(r)
        turtle.left(90)
        turtle.down()
        turtle.circle(r)
        turtle.end_fill()
        turtle.pu()
        turtle.home()
        turtle.down()
    def square(size):
        for i in range(4):
            turtle.fd(size)
            turtle.lt(90)
    def big_flower(shade):
        for i in range(13):
            turtle.up()
            turtle.goto(0,0)
            turtle.down()
            turtle.fillcolor(shade)
            turtle.pen(pencolor=shade,pensize="1")
            turtle.begin_fill()
            turtle.circle(305,70)
            turtle.left(110)
            turtle.circle(305,70)
            turtle.end_fill()
            turtle.right(1)
    def draw_square(square,lll,cll):
        for i in range(0,2):
            square.begin_fill()
            square.fillcolor(cll)
            square.forward(lll)
            square.right(30)
            square.forward(lll)
            square.right(150)
            square.end_fill()


    def draw_flower(coll,sizz):
        window = turtle.Screen()
        window.bgcolor("white")

        hello = turtle.Turtle()
        hello.speed(0)
        hello.shape("triangle")
        #turtle.pen(pencolor="99FF00",pensize="1")
        hello.color(coll)

        for i in range(0,36):
            draw_square(hello,sizz,coll)
            hello.right(10)
    def petal(t, r, angle):
        """Use the Turtle (t) to draw a petal using two arcs
        with the radius (r) and angle.
        """
        for i in range(2):
            t.circle(r,angle)
            t.left(180-angle)

    def flower(t, n, r, angle):
        """Use the Turtle (t) to draw a flower with (n) petals,
        each with the radius (r) and angle.
        """
        for i in range(n):
            petal(t, r, angle)
            t.left(360.0/n)
    turtle.pen(pencolor="#770E13",pensize="1")
    circ("#770E13",400)
    turtle.pen(pencolor="#E67B47",pensize="1")
    circ("#E67B47",390)
    turtle.pen(pencolor="#ECE19F",pensize="1")
    circ("#ECE19F",380)
    turtle.begin_fill()
    turtle.pen(pencolor="red",pensize="1")
    turtle.fillcolor("red")
    turtle.speed(0)
    turtle.pen(pencolor="red",pensize="1")
    for k in range(40):
        square(270)
        turtle.rt(10)
    turtle.end_fill()
    turtle.pen(pencolor="orange",pensize="1")
    circ("orange",350)
    turtle.pen(pencolor="#383629",pensize="1")
    big_flower("#383629")
    turtle.right(60)
    turtle.pen(pencolor="#EFE19A",pensize="1")
    big_flower("#EFE19A")
    turtle.pen(pencolor="#C8520A",pensize="1")
    turtle.right(60)
    big_flower("#C8520A")
    turtle.pen(pencolor="red",pensize="1")
    circ("red",280)


    t = turtle.Turtle()
    t.speed(0)
    ####draw_flower("#ECE19F",150)##################################
    turtle.begin_fill()
    turtle.pen(pencolor="#ECE19F",pensize="1")
    turtle.fillcolor("#ECE19F")
    turtle.speed(0)
    turtle.pen(pencolor="#ECE19F",pensize="1")
    for k in range(12):
        square(197)
        turtle.rt(30)  
    turtle.end_fill()
    turtle.pen(pencolor="#FFD504",pensize="1")
    t.begin_fill()
    #turtle.pen(pencolor="#FFD504",pensize="1")
    t.fillcolor("#FFD504")
    for k in range(12):
        for i in range(6):
            t.forward(140)
            t.right(60) 
        t.rt(30)
    t.end_fill()
    #draw_flower()
    turtle.pen(pencolor="#F4E389",pensize="1")
    circ("#F4E389",250)
    draw_flower("orange",129)
    turtle.pen(pencolor="#E67B47",pensize="1")
    circ("#E67B47",220)
    turtle.pen(pencolor="#2E7644",pensize="1")
    circ("#2E7644",210)

    turtle.begin_fill()
    turtle.pen(pencolor="orange",pensize="1")
    turtle.fillcolor("orange")
    #draw_flower()
    for k in range(40):
        square(148)
        turtle.rt(10)
    turtle.end_fill()
    turtle.speed(0)
    turtle.pen(pencolor="#F4E389",pensize="1")
    circ("#F4E389",160)
    turtle.speed(0)
    turtle.begin_fill()
    turtle.pen(pencolor="red",pensize="1")
    turtle.fillcolor("red")
    #draw_flower()
    for k in range(9):
        for i in range(6):
            turtle.forward(100) #Assuming the side of a hexagon is 100 units
            turtle.right(60) #Turning the turtle by 60 degree
        turtle.rt(40)
    turtle.end_fill()
    turtle.pen(pencolor="#C8520A",pensize="1")#ECE19F
    circ("#C8520A",172)
    turtle.pen(pencolor="#770E13",pensize="1")
    circ("#770E13",162)
    turtle.pen(pencolor="#E67B47",pensize="1")
    circ("#E67B47",152)
    turtle.pen(pencolor="orange",pensize="1")
    circ("orange",142)
    turtle.begin_fill()
    turtle.fillcolor("#383629")
    turtle.pen(pencolor="#383629",pensize="1")
    flower(turtle, 9, 140.0, 60.0)
    turtle.end_fill()
    turtle.lt(30)
    turtle.begin_fill()
    turtle.fillcolor("#EFE19A")
    turtle.pen(pencolor="#EFE19A",pensize="1")
    flower(turtle, 9, 140.0, 60.0)
    turtle.end_fill()
    turtle.lt(30)
    turtle.begin_fill()
    turtle.fillcolor("#C8520A")
    turtle.pen(pencolor="#C8520A",pensize="1")
    flower(turtle, 9, 140.0, 60.0)
    turtle.end_fill()
    turtle.lt(30)
    turtle.pen(pencolor="orange",pensize="1")
    for k in range(6):
        turtle.begin_fill()
        if k%2==0:
            turtle.pen(pencolor="yellow",pensize="1")
            turtle.fillcolor("yellow")
        else:
            turtle.pen(pencolor="orange",pensize="1")
            turtle.fillcolor("orange")
        square(40)
        turtle.rt(60)
        turtle.end_fill()
    turtle.exitonclick()

if num == 2:
    import turtle
    import math

    t = turtle.Turtle()
    t.speed(20)
    t.shape("turtle")
    t.getscreen().bgcolor("yellow")
    outer_radius = 300
    inner_radius = 250


    def petals(num, length):
        t.pu()
        t.home()
        t.pd()
        t.setheading(0)
        angle = 360 / num
        theta = 0
        t.begin_fill()
        for i in range(num):
            t.setheading(theta)
            t.circle(length)
            theta += angle
        t.end_fill()

    # petals(5,small_radius)

    t.color("darkgreen", "green")
    t.begin_fill()
    t.pu()
    t.goto(outer_radius, 0)
    t.left(90)
    t.pd()
    t.circle(outer_radius)
    t.end_fill()


    t.goto(inner_radius, 0)
    t.color("white", "orange")
    t.begin_fill()
    t.circle(inner_radius)
    t.end_fill()
    t.color("blue")

    print(t.pos())
    t.left(45)
    t.pu()
    t.pd()
    t.begin_fill()
    c = inner_radius * math.sqrt(2)
    for i in range(4):
        t.forward(c)
        t.left(90)
    t.end_fill()

    y = inner_radius/2+60
    # y=c
    t.setheading(90)
    t.circle(inner_radius,90/3)
    t.color("red")
    t.pd()
    t.begin_fill()
    t.left(45)
    for i in range(4):
        t.forward(c)
        t.left(90)
    t.end_fill()

    t.color("magenta")
    t.pu()
    t.goto(inner_radius,0)
    t.setheading(90)
    t.circle(inner_radius,60)
    t.pd()
    t.begin_fill()
    t.left(45)
    for i in range(4):
        t.forward(c)
        t.left(90)
    t.end_fill()

    t.setheading(90)
    t.color("yellow")
    n = 6  # no.of petals
    petals(n, inner_radius)
    t.color("brown")
    petals(6,inner_radius-143.5)

    t.color("blue")
    t.pu()
    z = outer_radius-15 #for filling
    t.goto(z, 0)
    t.setheading(90)
    t.width(30)
    t.pd()
    t.circle(z)
    t.width(5)

    t.color("lightgreen")
    small_radius = y/2
    t.pu()
    t.setpos(small_radius,0)
    t.setheading(90)
    t.width(25)
    t.pd()
    t.circle(small_radius)
    t.pu()
    t.goto(30,0)
    t.color("brown")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.setpos(10,0)
    t.color("khaki")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.pu()
    t.color("yellow")
    t.goto(310,0)
    turtle.done()

if num ==3:
    import turtle
    a=turtle.Turtle()

    a.up()
    a.goto(-180,235)
    a.down()

    def square(length,angle):
        for i in range(4):
            a.forward(length)
            a.right(angle)

    for i in range(10):
        a.color('black','yellow')
        a.speed(200)
        a.pensize(2)
        a.begin_fill()
        square(280, 60)
        a.right(12)
        a.end_fill()
    a.up()
    a.goto(0,0)
    a.down()

    for i in range(8):
        a.speed(100)
        a.color("black","orange")
        a.begin_fill()
        a.circle(140)
        a.left(45)
        a.end_fill()

    a.penup()
    a.goto(0,-250)
    a.pendown()
    a.pensize(22)
    a.color("#dbffc5")
    a.begin_fill()
    a.circle(250)
    a.end_fill()

    a.penup()
    a.goto(0,-230)
    a.pendown()
    a.pensize(21)
    a.color("green")
    a.circle(230)

    a.speed(100)
    a.up()
    a.goto(0,-218)
    a.pensize(10)
    a.color("brown","yellow")
    a.begin_fill()
    a.circle(220)
    a.end_fill()
    a.goto(0,0)

    for i in range(8):
        a.pensize(10)
        a.color("black","red")
        a.begin_fill()
        a.circle(100)
        a.right(60)
        a.end_fill()

    for i in range(12):
        a.pensize(3)
        a.color("red","orange")
        a.begin_fill()
        a.circle(80)
        a.right(45)
        a.end_fill()

    def square(length,angle):
        for i in range(4):
            a.forward(length)
            a.right(angle)

    for i in range(6):
        for colours in{"red","violet","blue","yellow","cyan","green"}:
            a.speed(200)
            a.pensize(2)
            a.begin_fill()
            a.color(colours)
            square(100, 90)
            a.right(12)
            a.end_fill()

    turtle.done()
 



            

            
            
            