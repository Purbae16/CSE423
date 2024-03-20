from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

s_width, s_height = 400,600
score = 0
d_color = [0.5, 0.5, 0.5]
c_color = [1.0,1.0,1.0]

def drawPixel(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def draw8way(x, y, slope):
    if slope == 0:
        drawPixel(x, y)
    elif slope == 1:
        drawPixel(y, x)
    elif slope == 2:
        drawPixel(-y, x)
    elif slope == 3:
        drawPixel(-x, y)
    elif slope == 4:
        drawPixel(-x, -y)
    elif slope == 5:
        drawPixel(-y, -x)
    elif slope == 6:
        drawPixel(y, -x)
    elif slope == 7:
        drawPixel(x, -y)


def MidpointLine(x0, y0, x1, y1, slope):
    dx = x1 - x0
    dy = y1 - y0
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)
    d = 2 * dy - dx
    x = x0
    y = y0
    while x < x1:
        draw8way(x, y, slope)
        if d < 0:
            d += incrE
            x += 1
        else:
            d += incrNE
            x += 1
            y += 1


def drawLine(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) >= abs(dy): # zone 0, 3, 4, and 7
        if dx >= 0:
            if dy >= 0:
                MidpointLine(x0, y0, x1, y1, 0)
            else:
                MidpointLine(x0, y0, -x1, -y1, 7)

        else:
            if dy >= 0:
                MidpointLine(-x0, y0, -x1, y1, 3)
            else:
                MidpointLine(-x0, -y0, -x1, -y1, 4)
    else: # zone 1, 2, 5, and 6
        if dx >= 0:
            if dy >= 0:
                MidpointLine(y0, x0, y1, x1, 1)
            else:
                MidpointLine(-y0, x0, -y1, x1, 6)

        else:
            if dy >= 0:
                MidpointLine(y0, -x0, y1, -x1, 2)
            else:
                MidpointLine(-y0, -x0, -y1, -x1, 5)

a = random.randrange(-400, 400, 10)
b = 0
dcol1 = 0.0
dcol2 = 1.0
dcol3 = 1.0
def diamond():
    global a, b, dcol1, dcol2, dcol3
    glColor3f(dcol1, dcol2, dcol3)
    drawLine(200 + a, 560 + b, 190 + a, 540 + b)
    drawLine(190 + a, 540 + b, 200 + a, 520 + b)
    drawLine(200 + a, 520 + b, 210 + a, 540 + b)
    drawLine(210 + a, 540 + b, 200 + a, 560 + b)


c = 0
ccol1 = 1
ccol2 = 1
ccol3 = 1
def catcher():
    glColor3f(ccol1, ccol2, ccol3)
    drawLine(140 + c, 30, 260 + c, 30)
    drawLine(260 + c, 30, 250 + c, 3)
    drawLine(250 + c, 3, 150 + c, 3)
    drawLine(150 + c, 3, 140 + c, 30)


def backbtn():
    glColor3f(0.0465, 0.930, 0.724)
    drawLine(10, 580, 50, 580)
    drawLine(30, 560, 10, 580)
    drawLine(10, 580, 30, 600)


def cross():
    glColor3f(1, 0, 0)
    drawLine(390, 600, 350, 560)
    drawLine(390, 560, 350, 600)


def pausebtn():
    glColor3f(0.980, 0.765, 0.0588)
    drawLine(190, 600, 190, 560)
    drawLine(210, 560, 210, 600)


def playbtn():
    glColor3f(0.980, 0.765, 0.0588)
    drawLine(210, 580, 190, 600)
    drawLine(190, 560, 210, 580)
    drawLine(190, 600, 190, 560)


def specialKeyListener(key, x, y):
    global c, status
    if status == "playing":
        if c > -140:
            if key == GLUT_KEY_LEFT:
                c -= 25
        if c < 140:
            if key == GLUT_KEY_RIGHT:	
                c += 25

    glutPostRedisplay()

count = 0 
speed = 0 
status = "playing" #or "paused"
def mouseListener(button, state, x, y):	
    y = s_height - y
    global status, b, score, a, c, ccol1, ccol2, ccol3, dcol1, dcol2, dcol3, speed, count
    if x > 180 and x < 220 and y < 600 and y > 540: #buffer pixels are added for ease of clicking
        if button==GLUT_LEFT_BUTTON:
            if(state == GLUT_DOWN):
                if status == "playing":
                    status = "paused"
                    print('paused')
                else:
                    ccol1 = 1
                    ccol2 = 1
                    ccol3 = 1
                    if b == 0:
                        dcol1 = random.random()
                        dcol2 = random.random()
                        dcol3 = random.random()
                    status = "playing"
    
    if x > 0 and x < 55 and y < 600 and y > 540:
        if button==GLUT_LEFT_BUTTON:
            if(state == GLUT_DOWN):
                print('Starting Over')
                status = "playing"
                a = random.randrange(-190, 190, 10)
                b = 0
                c = 0
                score = 0
                speed = 0
                count = 0
    
    glutPostRedisplay()

    if 330<x<400 and 540<y<600:
        if button==GLUT_LEFT_BUTTON:
            if(state == GLUT_DOWN):
                print("Goodbye :(")
                print("Final Score:", score)
                glutDestroyWindow(wind)

  
def animate():
    global b, count, speed
    if status == "playing":
        ran = random.randrange(-190, 190, 10 )  
        if b > -560:
            b -= (speed + 10)  #speed basically


def collision_check():
    global status, a, b, c, score, dcol1, dcol2, dcol3, ccol1, ccol2, ccol3, count, speed
    catcher_leftx = 140 + c
    catcher_rightx = 260 + c
    catcher_topy = 30
    diamond_leftx = 190 + a
    diamond_rightx = 210 + a
    diamond_bottomy = 520 + b
    if status == "playing":
        pausebtn()
        if diamond_bottomy <= catcher_topy:
            if diamond_leftx >= catcher_rightx or diamond_rightx <= catcher_leftx:
                status = "paused"
                a = 0
                b = 0
                c = 0
                print("Game Over!")
                print("Final Score:",score)
                dcol1 = 0
                dcol2 = 0
                dcol3 = 0
                ccol1 = 1
                ccol2 = 0
                ccol3 = 0
                score = 0
                speed = 0
                count = 0
            else:
                b = 0
                a = random.randrange(-190, 190, 10 )  
                score += 1
                dcol1 = random.random()
                dcol2 = random.random()
                dcol3 = random.random()
                print("Score:",score) 
                count += 1   
                if count == 2:
                    speed += 4
                    count = 0       
    else:
        playbtn()


def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    catcher()
    backbtn()
    cross()
    diamond()
    animate()
    collision_check()

    glutSwapBuffers()
    glutPostRedisplay()

def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,400,0,600,0,1)
    glMatrixMode(GL_MODELVIEW)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
glutInitWindowSize(s_width, s_height)
wind = glutCreateWindow(b"Catch the Diamonds")
init()
glutDisplayFunc(display)
#glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glEnable(GL_DEPTH_TEST)
glutMainLoop()