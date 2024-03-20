from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500,500

ballx = [] 
bally = []
speed = 2
ball_size = 7
col1 = []
col2 = []
col3 = []
rando = []
count = 0
counter = 0
blink = False
blink_counter = 0


def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b

def draw_points(x, y, s, col1, col2, col3):
    glColor3f(col1, col2, col3)
    glPointSize(s)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def keyboardListener(key, x, y):

    global ball_size, speed, count
    if count%2 == 0:
        if key==b'b':
            ball_size+=1
            print("Size Increased")
        if key==b's':
            ball_size-=1
            print("Size Decreased")
    if key == b' ':
        if count%2 == 0:
            speed = 0
        else:
            speed = 2
        count+=1

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed, count
    if count%2 == 0:
        if key == GLUT_KEY_UP:
            speed *= 2
            print("Speed Increased")
        if key == GLUT_KEY_DOWN:	
            speed /= 2
            print("Speed Decreased")

    glutPostRedisplay()

def mouseListener(button, state, x, y):	
    global ballx, bally, rando, count, blink, counter
    print(x, y)
    if count%2 == 0:
        if button==GLUT_LEFT_BUTTON:
            if(state == GLUT_DOWN):   
                if counter%2 == 0:
                    blink = True
                else:
                    blink = False
                counter+=1
            
        if button==GLUT_RIGHT_BUTTON:
            if state == GLUT_DOWN: 	
                print(x,y)
                c_X, c_y = convert_coordinate(x,y)
                ballx.append(c_X)
                bally.append(c_y)
                col1.append(random.random())
                col2.append(random.random())
                col3.append(random.random())
                rando.append(random.randrange(1,5))

    glutPostRedisplay()

def animate():
    global ballx, bally, speed
    for i in range(len(ballx)):
        if rando[i] == 1:
            glutPostRedisplay()
            ballx[i] = ballx[i] + (speed)/100
            bally[i] = bally[i] -  (speed)/100

        elif rando[i] == 2:
            glutPostRedisplay()
            ballx[i] = ballx[i] + (speed)/100
            bally[i] = bally[i] +  (speed)/100

        elif rando[i] == 3:
            glutPostRedisplay()
            ballx[i] = ballx[i] - (speed)/100
            bally[i] = bally[i] +  (speed)/100

        elif rando[i] == 4:
            glutPostRedisplay()
            ballx[i] = ballx[i] - (speed)/100
            bally[i] = bally[i] -  (speed)/100


def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    global ballx, bally, ball_size, col1, col2, col3, blink, blink_counter
    for i in range(len(ballx)):
        if blink == True:
            if blink_counter%20 == 0:
                draw_points(ballx[i], bally[i], ball_size, c1, col2[i], col3[i])
            else: 
                draw_points(ballx[i], bally[i], ball_size, 0.0, 0.0, 0.0)
            blink_counter += 1
        else:
            draw_points(ballx[i], bally[i], ball_size, c1, col2[i], col3[i])
    animate()
   
    glutSwapBuffers()


def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)	#display callback function
#glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL
            