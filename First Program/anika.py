from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

points = 0
d_color =[0.5, 0.5, 0.5]
c_color = [1.0, 1.0, 1.0]
incre_d = [random.randrange(-200, 200, 10),0]
incre_c = 0
last_score = 0
status = True
speed = 0

def drawPoint(x, y):
    glPointSize(1.5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def findZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) >= abs(dy):
        if dx >= 0:
            if dy >= 0:
                return 0
            else:
                return 7
        elif dx <= 0:
            if dy >= 0:
                return 3
            else:
                return 4
    else:
        if dy >= 0:
            if dx >= 0:
                return 1
            else:
                return 6
        elif dy <= 0 :
            if dx >= 0:
                return 2
            else:
                return 5

def convertToZone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y
    
def plotPoint(x, y, zone):
    if zone == 0:
        drawPoint(x, y)
    elif zone == 1:
        drawPoint(y, x)
    elif zone == 2:
        drawPoint(y, -x)
    elif zone == 3:
        drawPoint(-x, y)
    elif zone == 4:
        drawPoint(-x, -y)
    elif zone == 5:
        drawPoint(-y, -x)
    elif zone == 6:
        drawPoint(-y, x)
    elif zone == 7:
        drawPoint(x, -y)

def drawLine(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    x0, y0 = convertToZone0(x0, y0, zone)
    x1, y1 = convertToZone0(x1, y1, zone)

    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    deltaE = 2 * dy
    deltaNE = 2 * (dy - dx)
    x = x0
    y = y0
    plotPoint(x, y, zone)

    while x < x1:
        if d <= 0:
            d += deltaE
            x += 1
        else:
            d += deltaNE
            x += 1
            y += 1
        plotPoint(x, y, zone)



def diamond():
    global d_color, incre_d
    glColor3f(d_color[0], d_color[1], d_color[2])
    drawLine(200+incre_d[0], 560+incre_d[1], 190+incre_d[0], 540+incre_d[1])
    drawLine(200+incre_d[0], 560+incre_d[1], 210+incre_d[0], 540+incre_d[1])
    drawLine(190+incre_d[0], 540+incre_d[1], 200+incre_d[0], 520+incre_d[1])
    drawLine(200+incre_d[0], 520+incre_d[1], 210+incre_d[0], 540+incre_d[1])

def catcher():
    global incre_c, c_color
    glColor3f(c_color[0], c_color[1], c_color[2])
    drawLine(140+incre_c, 25, 260+incre_c, 25)
    drawLine(250+incre_c, 5, 260+incre_c, 25)
    drawLine(150+incre_c, 5, 140+incre_c, 25)
    drawLine(250+incre_c, 5, 150+incre_c, 5)

def backbtn():
    glColor3f(0.239, 0.929, 0.851)
    drawLine(10, 580, 50, 580)
    drawLine(30, 560, 10, 580)
    drawLine(10, 580, 30, 600)

def cross():
    glColor3f(1, 0, 0)
    drawLine(390, 600, 350, 560)
    drawLine(390, 560, 350, 600)

def pausebtn():
    glColor3f(0.902, 0.702, 0.051)
    drawLine(190, 560, 190, 600)
    drawLine(210, 560, 210, 600)

def playbtn():
    glColor3f(0.902, 0.702, 0.051)
    drawLine(210, 580, 190, 600)
    drawLine(190, 560, 210, 580)
    drawLine(190, 560, 190, 600)

def specialKeyListener(key, x, y):
    global incre_c, status
    if status == True:
        if 140+incre_c > 0:
            if key == GLUT_KEY_LEFT:
                incre_c -= 20
        if 260+incre_c < 400:
            if key == GLUT_KEY_RIGHT:	
                incre_c += 20

    glutPostRedisplay()

def animate():
    global incre_d, speed
    if status == True:  
        if incre_d[1] > -560:
            incre_d[1] -= (speed + 10)

def collision_check():
    global status, incre_d, incre_c, points, d_color, c_color, speed, last_score
    d_left = 190 + incre_d[0]
    d_right = 210 + incre_d[0]
    d_bottom = 520 + incre_d[1]
    c_left = 140 + incre_c
    c_right = 260 + incre_c
    c_top = 25
    if status == True:
        pausebtn()
        if d_bottom <= c_top:
            if d_left >= c_right or d_right <= c_left:
                status = False
                incre_d[0] = 0
                incre_d[1] = 0
                incre_c = 0
                print("Game Over!")
                print("Final Score:",points)
                c_color = [1.0, 0.0, 0.0]
                d_color = [0.0,0.0,0.0]
                last_score = points
                points = 0
                speed = 0
            else:
                incre_d[1] = 0
                incre_d[0] = random.randrange(-190, 190, 10 )  
                points += 1
                d_color =[random.random(), random.random(), random.random()]
                print("Score:",points) 
                speed += 1      
    else:
        playbtn()

def mouseListener(button, state, x, y):	
    global status, points, d_color, c_color, incre_d, incre_c, speed, last_score
    y = 600 - y
    if 180 < x < 220 and 540 < y < 600: 
        if button==GLUT_LEFT_BUTTON:
            if(state == GLUT_DOWN):
                if status == True:
                    status = False
                    c_color = [1.0, 0.0, 0.0]
                    print('paused')
                else:
                    c_color = [1.0, 1.0, 1.0]
                    if incre_d[1] == 0:
                        d_color =[random.random(), random.random(), random.random()]
                    status = True
    
    if 0 < x < 55 and 540 < y < 600:
        if button==GLUT_LEFT_BUTTON:
            if(state == GLUT_DOWN):
                print('Starting Over')
                status = True
                incre_d[0] = random.randrange(-190, 190, 10)
                incre_d[1] = 0
                incre_c = 0
                points = 0
                speed = 0
    glutPostRedisplay()

    if x > 330 and x < 400 and y < 600 and y > 540:
        if button==GLUT_LEFT_BUTTON:
            if(state == GLUT_DOWN):
                print('Goodbye')
                print("Final Score:", last_score)
                glutDestroyWindow(wind)


def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    backbtn()
    cross()
    diamond()
    catcher()
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
glutInitWindowSize(400, 600)
wind = glutCreateWindow(b"Diamond Catcher")
init()
glutDisplayFunc(display)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glEnable(GL_DEPTH_TEST)
glutMainLoop()