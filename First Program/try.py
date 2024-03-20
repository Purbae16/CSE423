from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Function to draw a point
def drawPoint(x, y):
    glBegin(GL_POINTS)
    print(x,y)
    glVertex2f(x, y)
    glEnd()

# Function to handle window resizing
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, 0.0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Function to plot a point in any zone
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

# Function to convert a point from any zone to zone 0
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

# Midpoint Line Drawing Algorithm
def midpointLine(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    print(zone)
    x0, y0 = convertToZone0(x0, y0, zone)
    x1, y1 = convertToZone0(x1, y1, zone)

    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    deltaE = 2 * dy
    deltaNE = 2 * (dy - dx)
    x = x0
    y = y0
    print(x, y)
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

# Function to find the zone of a line
def findZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) >= abs(dy):
        if dx >= 0:
            if dy >= 0:
                return 0
            else:
                return 7
        else:
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
        else:
            if dx >= 0:
                return 2
            else:
                return 5

# Function to draw the line
def drawLine(x0, y0, x1, y1):
    midpointLine(x0, y0, x1, y1)

# Function to display the result
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    
    # Drawing the line
    #drawLine(300, 200, 100, 400)
    drawLine(190, 540, 200, 520)
    #drawLine(210, 540, 200, 560)

    glFlush()

# Main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 600)
    glutCreateWindow(b"Midpoint Line Drawing Algorithm")
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()


