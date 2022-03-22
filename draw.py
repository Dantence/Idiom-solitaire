#!python3
#coding=utf8
#名称：雪中送炭，本意为雪中送炭指下雪天给人送炭取暖，现指在困难或危急时，给人物质或精神上的帮助，本图即描绘该成语本意的场景
import turtle as t
import math
import random
#初始化
def init():
    t.speed(1000)
    t.screensize(800, 800, "#F5DEB3")
    t.Screen().setup(800, 800)

#终止绘图
def end():
    t.done()

#设置笔的颜色和大小
def setPenInfo(size, color):
    t.pensize(size)
    t.pencolor(color)

#画背景房子
def drawHouse():
    t.penup()
    t.goto(-400, 150)
    t.pendown()
    t.forward(200)

    t.right(90)
    t.forward(100)
    t.left(180)
    t.forward(150)
    t.right(45)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(135)
    dis = math.sqrt(100*100 + 100*100)
    t.forward(dis)
    t.backward(dis)
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(dis)
    t.backward(dis)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(450)

#画人物,给出头顶坐标
def drawPerson(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(20, 360)
    t.right(90)
    t.forward(8)
    t.left(60)
    t.forward(30)
    t.backward(30)
    t.right(120)
    t.forward(30)
    t.backward(30)
    t.left(60)
    t.forward(26)
    t.left(60)
    t.forward(30)
    t.backward(30)
    t.right(120)
    t.forward(30)
    t.backward(30)
    t.left(150)

#画煤车
def drawCart(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.right(90)
    t.forward(80)
    t.left(90)
    t.forward(120)
    t.backward(90)
    t.circle(-10, 360)
    t.forward(60)
    t.circle(-10, 360)
    t.forward(30)
    t.left(90)
    t.forward(80)
    t.right(90)

#画煤炭
def drawCoal(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    t.forward(10)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.end_fill()

#画枯树
def drawTree(len):
    len = int(len)
    if(len > 4):
        t.forward(len)
        t.right(30)
        drawTree(len - 10)
        t.left(60)
        drawTree(len - 10)
        t.right(30)
        t.backward(len)

#画雪
def drawSnow(x, y):
    t.seth(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor("white")
    t.circle(5, 360)
    t.end_fill()

def drawAll():
    init()
    setPenInfo(3, "black")
    drawHouse()
    drawPerson(-100, 100)
    drawPerson(0, -100)
    drawPerson(200, -100)
    drawCart(40, -80)

    for i in range(50, 145, 15):
        drawCoal(i, -80)

    t.seth(90)
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    setPenInfo(4, "#9C6B30")
    drawTree(60)
    setPenInfo(3, "white")
    t.hideturtle()

    for i in range(50):
        x = random.randint(-400, 450)
        y = random.randint(-400, 400)
        drawSnow(x, y)

def drawWords(words, posx, posy):
    t.penup()
    t.goto(posx, posy)
    t.pencolor("black")
    t.pendown()
    i = 0
    while i < len(words):
        t.write(words[i], align="center", font=("宋体", 30, "normal"))
        i += 1
        t.penup()
        t.goto(posx, posy - 40 * i)
        t.pendown()





