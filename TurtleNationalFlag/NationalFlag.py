from turtle import *
up()
goto(-200,300)
length = 300
height = 60
bgpic('back.png')
speed(5)
pensize(1.5)
for j in range(3):
    if j == 0:
        color('#FF9933')
    elif j == 1:
        color('white')
    else:
        color('#138808')
    begin_fill()
    for i in range(2):
        forward(length)
        right(90)
        forward(height)
        right(90)
    end_fill()
    right(90)
    up()
    forward(height)
    left(90)
    down()
    if j == 1:
        color('#000080','white')
        begin_fill()
        forward(length/2)
        circle(height/2)
        left(90)
        for k in range(24):
            forward(height/2)
            left(165)
            backward(height/2)
        right(90)
        backward(length/2)
        end_fill()
left(90)
forward(height*3)
color('brown')
pensize(10)
begin_fill()
left(180)
backward(6)
forward(length*1.8)
end_fill()
left(90)
pensize(1)
brick = 120
color('#777777','#aaaaaa')

for j in range(3):

    if j == 0 or j == 1:
        brick *= (j + 1)
        backward(60)
    else:
        brick += 120
        backward(60)
    for i in range(2):
        begin_fill()
        forward(brick)
        right(90)
        forward(height/2.3)
        right(90)
        end_fill()
    right(90)
    up()
    forward(height/2.3)
    left(90)
    down()
for i in range(3):
    left(90)
    forward(height/2.3)
    right(90)
    forward(60)
left(30)
color('#8d5118')
pensize(3)
backward(40)
for i in range(6):
    stamp()
    left(60)
forward(40)
circle(125,120)
circle(-120,120)
circle(68,120)

done()