import turtle
turtle.bgcolor("black")
colors = [ "pink","yellow","blue","green","white","red"]
turtle.speed(0)
for i in range (0,500):
    sketch= turtle.pencolor(colors[i%6])
    turtle.width(i/200+1)
    turtle.forward(i)
    turtle.left(i*0.5+1)
    
turtle.exitonclick()