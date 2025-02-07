import turtle
turtle.shape('turtle')
turtle.penup()
turtle.backward(100)
turtle.left(90)
turtle.forward(100)
turtle.pendown()
n = 3
for i in range(n):
    turtle.forward(50)
    turtle.right(360/n)
turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.pendown()
j = 4
for k in range(j):
    turtle.forward(50)
    turtle.left(360/j)
turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.pendown()
m = 5
for a in range(m):
    turtle.forward(40)
    turtle.left(360/m)
turtle.penup()
turtle.right(90)
turtle.forward(80)
turtle.pendown()
b = 6
for c in range(b):
    turtle.forward(30)
    turtle.left(360/b)
turtle.mainloop()