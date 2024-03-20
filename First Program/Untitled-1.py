from OpenGL.GL import *
from OpenGL.GLUT import *
import random 

bend = 0.0
rain_coordinates = []
color = 0.0

# Initialize raindrop coordinates
for i in range(100):
     x = random.uniform(0, 500)
     y = random.uniform(250, 500)
     rain_coordinates.append((x, y))

def draw_house():

    #roof
    glLineWidth(6)
    glBegin(GL_LINES)
    glVertex2f(250, 350)
    glVertex2f(100, 300) 
    glVertex2f(250, 350)
    glVertex2f(400, 300)
    glVertex2f(100, 300)
    glVertex2f(400, 300)
    glEnd()
    
    #body
    glLineWidth(6)
    glBegin(GL_LINES)
    glVertex2f(120, 300)
    glVertex2f(120, 100) 
    glVertex2f(380, 300)
    glVertex2f(380, 100)
    glVertex2f(120, 103)
    glVertex2f(380, 103)
    glEnd()

    #door
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(160, 210)
    glVertex2f(215, 210) 
    glVertex2f(160, 210)
    glVertex2f(160, 103)
    glVertex2f(215, 210)
    glVertex2f(215, 103)
    glEnd()

    #door_handle
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(203, 157)
    glEnd()

    #window
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(340, 250)
    glVertex2f(285, 250) 
    glVertex2f(340, 195)
    glVertex2f(285, 195)
    glVertex2f(340, 250)
    glVertex2f(340, 195)
    glVertex2f(285, 250)
    glVertex2f(285, 195)
    glVertex2f(312.5, 250)
    glVertex2f(312.5, 195)
    glVertex2f(340, 222.5)
    glVertex2f(285, 222.5) 
    glEnd()


def raindrop(x1, y1):
    global color
    glColor3f(1.0 - color, 1.0 - color, 1.0 - color)
    glLineWidth(1.2)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x1, y1 + 8)
    glEnd()

def animate_rain():
    global bend 
    for i in range(len(rain_coordinates)):
        x_new, y_new = rain_coordinates[i] 
        
        # Update raindrop coordinates
        x_new += bend 
        y_new -= 1

        # Check if raindrop hits the roof or goes outside the limit
        if (y_new < 0) or (x_new < 0) or (x_new > 500) or \
           ((100 < x_new < 250) and (y_new <= ((1/3) * x_new) + (800/3))) or \
           ((250 < x_new < 400) and (y_new <= ((-1/3) * x_new) + (1300/3))):
            # Reset raindrop position if it hits the roof or goes outside the limit
            x_new = random.uniform(0, 500)
            y_new = random.uniform(250, 500)
        
        rain_coordinates[i] = (x_new, y_new)

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global bend 
    #For bending rain
    if key == GLUT_KEY_RIGHT:
        bend += 0.5
        print("bend right")
    if key == GLUT_KEY_LEFT:		
        bend -= 0.5
        print("bend left")
    
    glutPostRedisplay()

def keyboardListener(key, x, y):
    global color
    #For day and night
    if key == b'd' and color >= 0.0: 
        color -= 0.3
        print("dark")
    if key == b'l' and color <= 1.0:
        color += 0.3
        print("light")
    
    glutPostRedisplay()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global color
    bg = (0.0 + color, 0.0 + color, 0.0 + color, 0.0 + color)
    glClearColor(*bg)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_house()

    for c in rain_coordinates:
        raindrop(c[0], c[1])
    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutIdleFunc(animate_rain)

glutMainLoop()
