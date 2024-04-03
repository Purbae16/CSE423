from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rand
#import math

# window
width, height = 500, 500
# shooter
shooter_cx, shooter_cy, shooter_r = 250, 30, 10
shooter_shift, shooter_incr = 0, 0
# shotBubbles
shotBubble_cx, shotBubble_cy, shotBubble_r = 0, 0, 5

# bubbles
radius = []
cx = []
cy = []
bubble_decr = []
# max_rad_list = []
# controls
status = "hold"
bubble_status = []

pause = False
score = 0
life = 3
dead = False


def start_over():
    global pause, dead, score, life, cx, cy, radius, bubble_decr, bubble_status, shooter_shift, shooter_incr
    pause, dead = False, False

    score, life = 0, 3
    cx, cy, radius, bubble_decr, bubble_status = [], [], [], [], []
    shooter_shift, shooter_incr = 0, 0
    create_random_bubbles()


def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 0, 1)
    glMatrixMode(GL_MODELVIEW)


def circ_points(x, y, cx, cy):
    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)

    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)

    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)

    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)


def shooter_reset():
    global status, shooter_incr
    status = "hold"
    shooter_incr = 0


def mid_circle(cx, cy, radius):
    d = 1 - radius
    x = 0
    y = radius

    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * x - 2 * y + 5
            y = y - 1
        x = x + 1
        circ_points(x, y, cx, cy)


def draw_shooter():
    global shooter_cx, shooter_cy, shooter_r, shooter_shift
    mid_circle(shooter_cx + shooter_shift, shooter_cy, shooter_r)


def draw_bubbles():
    global cx, cy, bubble_decr, radius, bubble_status
    if len(radius) >= 0:
        for i in range(len(radius)):
            if bubble_status[i] == "fall":
                mid_circle(cx[i], cy[i] - bubble_decr[i], radius[i])
            else:
                continue

    glutPostRedisplay()


def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def draw_res():
    glColor3f(0.0, 0.5, 0.8)
    draw_line(30, 490, 5, 470)
    draw_line(5, 470, 30, 450)
    draw_line(5, 470, 60, 470)


def draw_cross():
    glColor3f(1.0, 0.0, 0.0)
    draw_line(460, 490, 490, 450)
    draw_line(460, 450, 490, 490)


def draw_pause():
    global pause
    glColor3f(1.0, 1.0, 0.0)
    if pause == True:
        draw_line(230, 490, 280, 470)
        draw_line(280, 470, 230, 450)
        draw_line(230, 450, 230, 490)
    else:
        draw_line(250, 490, 250, 450)
        draw_line(270, 490, 270, 450)


def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_res()
    draw_cross()
    draw_pause()
    glPointSize(2)
    glColor3f(1, 1, 1)
    glBegin(GL_POINTS)
    draw_shooter()
    draw_bubbles()
    animate()
    glEnd()
    glutSwapBuffers()
    glutPostRedisplay()


def mouseListener(button, state, x, y):
    global height, width, pause

    nx = x
    ny = height - y

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            # setting pause
            if nx > 230 and nx < 280 and ny > 450 and ny < 490:
                pause = not pause
            # setting reset
            elif nx > 5 and nx < 60 and ny > 450 and ny < 490:
                start_over()
                # diamond_reset()
            # setting cross
            elif nx > 460 and nx < 490 and ny > 450 and ny < 490:
                print("Goodbye")
                # print(f"Points: {point}")
                glutDestroyWindow(wind)


def specialKeyListener(key, x, y):
    global shooter_shift, pause, dead
    if not pause and not dead:
        if shooter_shift < 230:
            if key == GLUT_KEY_RIGHT:
                shooter_shift += 10
        if shooter_shift > -230:
            if key == GLUT_KEY_LEFT:
                shooter_shift -= 10


def random_bubbles():
    global radius, cx, cy, bubble_status, bubble_decr
    if bubble_status.count("fall") <= 4:
        radius.append(rand.randrange(10, 20, 5))
        cx.append(rand.randrange(20, 480, 20))
        cy.append(rand.randrange(300, 480, 20))
        bubble_status.append("fall")
        bubble_decr.append(0.1)


def keyboardListener(key, x, y):
    global shooter_cx, shotBubble_cx, shooter_shift
    global status
    if status == "hold" and key == b" ":

        status = "shoot"
        shotBubble_cx = shooter_cx + shooter_shift
        # uncomment for the random bubbles


def bubble_reset(i):
    global bubble_status
    bubble_status[i] = "pop"


def game_over():
    global life, score, dead
    global cx, cy, radius, bubble_decr, bubble_status
    if life == 0:
        print("Game Over. Score:", score)
        cx, cy, radius, bubble_decr, bubble_status = [], [], [], [], []
        dead = True


def collision(i):
    global cx, cy, shotBubble_cx, shotBubble_cy, radius, shotBubble_r
    global bubble_status, shooter_incr, bubble_decr
    global score, life
    global shooter_cx, shooter_cy, shooter_shift, shooter_r
    c1x, c1y, c2x, c2y, r1, r2, bdown, sincr = (
        cx[i],
        cy[i],
        shotBubble_cx,
        shotBubble_cy,
        radius[i],
        shotBubble_r,
        bubble_decr[i],
        shooter_incr,
    )
    bleft, bright = c1x - r1, c1x + r1
    bup, bdown = c1y + r1 - bdown, c1y - r1 - bdown

    sleft, sright = c2x - r2, c2x + r2
    sup, sdown = c2y + r2, c2y - r2

    shleft, shright = (
        shooter_cx - shooter_r + shooter_shift,
        shooter_cx + shooter_r + shooter_shift,
    )
    shup = shooter_cy + shooter_r
    if shup >= bdown and bubble_status[i] == "fall":
        if (shleft <= bright and shleft >= bleft) or (
            shright <= bright and shright >= bleft
        ):
            life = 0

    if sup >= bdown and bubble_status[i] == "fall":
        if (sleft <= bright and sleft >= bleft) or (
            sright <= bright and sright >= bleft
        ):
            bubble_reset(i)
            shooter_reset()
            score += 1
            print("Score is:", score)


def bubble_fall():
    global bubble_decr, cy

    global cx, cy, shotBubble_cx, shotBubble_cy, radius, shooter_r
    global bubble_status, shooter_incr
    global score, life

    if len(bubble_decr) >= 0:
        for i in range(len(bubble_decr)):
            collision(i)
            if -bubble_decr[i] + cy[i] + radius[i] > radius[i] * 2:
                bubble_decr[i] += 0.01

            else:
                if bubble_status[i] == "fall":
                    life -= 1
                    print("Remaining life:", life)
                bubble_reset(i)


def animate():
    global shooter_incr, shooter_shift, shotBubble_cx, shotBubble_cy, shotBubble_r
    global status, pause, dead
    global bubble_decr, cy
    if not pause and not dead:
        if status == "shoot":
            if shooter_incr <= 470:
                shooter_incr += 0.1
                shotBubble_cy = shooter_cy + shooter_incr
                shotBubble_r = shooter_r - 5
                mid_circle(shotBubble_cx, shotBubble_cy, shotBubble_r)
            else:
                shooter_reset()
        bubble_fall()
        game_over()


def create_random_bubbles(n=0):
    global pause, dead
    if not pause and not dead:
        random_bubbles()
        time_gap = rand.randrange(1000, 2000, 500)
        glutTimerFunc(time_gap, create_random_bubbles, 0)
    # glutTimerFunc(2000, create_random_bubbles, 0)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(width, height)
wind = glutCreateWindow(b"circle drawing stuff")
init()
glutIdleFunc(animate)
glutDisplayFunc(display)
create_random_bubbles()
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glEnable(GL_DEPTH_TEST)
glutMainLoop()
