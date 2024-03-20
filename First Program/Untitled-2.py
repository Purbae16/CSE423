from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

s_height, s_width = 500, 500

point_coordinates = []
color = []
point_size = 6
speed = 2
pause = False
rd = []

def draw_points(x, y, size, col1, col2, col3):
    glColor3f(col1, col2, col3)
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def animate():
    global point_coordinates, speed, rd
    for i in range(len(point_coordinates)):
        #rd = random.randrange(1,5)
        pnt_x, pnt_y = point_coordinates[i]
        if rd[i] == 1:
            glutPostRedisplay()
            pnt_x = pnt_x + (speed)/100
            pnt_y = pnt_y -  (speed)/100

        elif rd[i] == 2:
            glutPostRedisplay()
            pnt_x = pnt_x + (speed)/100
            pnt_y = pnt_y +  (speed)/100

        elif rd[i] == 3:
            glutPostRedisplay()
            pnt_x = pnt_x - (speed)/100
            pnt_y = pnt_y +  (speed)/100

        elif rd[i] == 4:
            glutPostRedisplay()
            pnt_x = pnt_x - (speed)/100
            pnt_y = pnt_y -  (speed)/100

def convert_coordinate(x,y):
    global s_width, s_height
    a = x - (s_width/2)
    b = (s_height/2) - y 
    return a,b

def mouseListener(button, state, x, y):	
    global point_coordinates, pause #, blink, counter
    print(x, y)
    if pause == False:
        #if button==GLUT_LEFT_BUTTON:
            #if(state == GLUT_DOWN):   
                #if counter%2 == 0:
                   # blink = True
                #else:
                    #blink = False
                #counter+=1
            
        if button==GLUT_RIGHT_BUTTON:
            if state == GLUT_DOWN: 	
                print(x,y)
                c_x, c_y = convert_coordinate(x,y)
                point_coordinates.append((c_x,c_y))
                color.append((random.random(), random.random(), random.random()))
                rd.append(random.randrange(1,5))

    glutPostRedisplay()


def showscreen():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    global point_coordinates, color, point_size#ballx, bally, ball_size, col1, col2, col3, blink, blink_counter
    for i in range(len(point_coordinates)):
            pnt_x, pnt_y = point_coordinates[i]
            col1, col2, col3 = color[i]
        #if blink == True:
            #if blink_counter%20 == 0:
                #draw_points(pnt_x, pnt_y, ball_size, c1, col2[i], col3[i])
            #else: 
                #draw_points(pnt_x, pnt_y, ball_size, 0.0, 0.0, 0.0)
            #blink_counter += 1
        #else:
            draw_points(pnt_x, pnt_y, point_size, col1, col2, col3)
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
glutInitWindowSize(s_width, s_height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(showscreen)	#display callback function
#glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

#glutKeyboardFunc(keyboardListener)
#glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()