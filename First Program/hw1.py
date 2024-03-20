from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_house():
    glLineWidth(6) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(250, 350)
    glVertex2f(100, 300) 
    glVertex2f(250, 350)
    glVertex2f(400, 300)
    glVertex2f(100, 300)
    glVertex2f(400, 300)
    #jekhane show korbe pixel
    glEnd()

    glLineWidth(6) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(120, 300)
    glVertex2f(120, 100) 
    glVertex2f(380, 300)
    glVertex2f(380, 100)
    glVertex2f(120, 103)
    glVertex2f(380, 103)
    #jekhane show korbe pixel
    glEnd()

    glLineWidth(2) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(160, 210)
    glVertex2f(215, 210) 
    glVertex2f(160, 210)
    glVertex2f(160, 103)
    glVertex2f(215, 210)
    glVertex2f(215, 103)
    #jekhane show korbe pixel
    glEnd()

    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(203, 157)
    glEnd()

    glLineWidth(2) #pixel size. by default 1 thake
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
    #jekhane show korbe pixel
    glEnd()


def rain():
    x1, y1 = 95, 500
    x2, y2 = 105, 507

    for i in range(25):
        for i in range(10):
            if y1-15<300 and 120<x1<380:
                break
            glLineWidth(2) #pixel size. by default 1 thake
            glBegin(GL_LINES)
            glVertex2f(x1, y1)
            glVertex2f(x1, y1-15)
            glEnd()

            y1 -= 24
        x1 += 12.9
        y1 = 500

#def fill():
    #glBegin(GL_TRIANGLES)
    #glColor3f(0, 0.0, 0.0)
    #glVertex2f(250, 346)
    #glVertex2f(110, 302) 
    #glVertex2f(390, 302)
    #glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_house()
    rain()
    #fill()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()