from turtle import *

speed(10)
shape("turtle")

for count in range(5):
    forward(50)
    right(72)

penup()
forward(100)
pendown()
for count in range(6):
    forward(50)
    right(60)

penup()
left(90)
forward(100)
pendown()   

for count in range(360):
    forward(1)  
    right(1) 
    
hideturtle()
    
done()
