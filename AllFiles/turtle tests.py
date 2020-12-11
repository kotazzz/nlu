from turtle import *
from enum import Enum
class Direction(Enum):
    UL = 0
    UR = 1
    DL = 2
    DR = 3
def square(size):
    fd(size)
    lt(90)
    fd(size)
    lt(90)
    fd(size)
    lt(90)
    fd(size)
    lt(90)
def square_dir(size, direction):
    if direction == Direction.UL:
       fd(size)
       lt(90)
       fd(size)
       lt(90)
       fd(size)
       lt(90)
       fd(size)
       lt(90)
    if direction == Direction.DL:
       fd(size)
       rt(90)
       fd(size)
       rt(90)
       fd(size)
       rt(90)
       fd(size)
       rt(90)
    if direction == Direction.DR:
       bk(size)
       lt(90)
       bk(size)
       lt(90)
       bk(size)
       lt(90)
       bk(size)
       lt(90)
    if direction == Direction.UR:
       bk(size)
       rt(90)
       bk(size)
       rt(90)
       bk(size)
       rt(90)
       bk(size)
       rt(90)
def line():
    fd(80)
    bk(80)
    rt(90)
    fd(1)
    lt(90)
    
def reset():
    seth(180)
    fd(255)
    seth(90)
    bk(80)
def draw_gra_lot():
    i=0
    seth(90)
    fd(320)
    while i < 255:
        pencolor(i, 0, 255-i)
        line()
        i+=1
    reset()
    i = 0
    while i < 255:
        pencolor(i, round(i/2), 255-i)
        line()
        i+=1
    reset()
    i = 0
    while i < 255:
        pencolor(i, i, i)
        line()
        i+=1
    reset()
    i = 0
    while i < 255:
        pencolor(255, round(i/2), 255-i)
        line()
        i+=1
    reset()
    i = 0
    while i < 255:
        pencolor(255, i, 255)
        line()
        i+=1
    reset()
    i = 0
    while i < 255:
        pencolor(255, round(i/2), 255-i)
        line()
        i+=1
    reset()
    i = 0
    while i < 255:
        pencolor(i,i,255-i)
        line()
        i+=1 
    reset()
    i = 0
    while i < 255:
        pencolor(255-i,round(i/2),round(i/2))
        line()
        i+=1 

if __name__== "__main__":
    Screen().screensize(1000, 1000)
    colormode(255)
    speed(1000)
    tracer(0, 0)
    up()
    down()
    draw_gra_lot() 
    up()
    update()
    #ht()
