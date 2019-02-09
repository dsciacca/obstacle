import RPi.GPIO as G
import time

G.setwarnings(False)
G.setmode(G.BCM)

TRIG = 17
ECHO = 27
led = 19
m11 = 16
m12 = 12
m21 = 21
m22 = 20

G.setup(TRIG, G.OUT)
G.setup(ECHO, G.IN)
G.setup(led, G.OUT)
G.setup(m11, G.OUT)
G.setup(m12, G.OUT)
G.setup(m21, G.OUT)
G.setup(m22, G.OUT)

G.output(led, 0)

time.sleep(1)

def stop():
    print "stop"
    G.output(m11, 0)
    G.output(m12, 0)
    G.output(m21, 0)
    G.output(m22, 0)

def forward():
    G.output(m11, 1)
    G.output(m12, 0)
    G.output(m21, 1)
    G.output(m22, 0)
    print "forward"

def back():
    G.output(m11, 0)
    G.output(m12, 1)
    G.output(m21, 0)
    G.output(m22, 1)
    print "back"

def left():
    G.output(m11, 0)
    G.output(m12, 0)
    G.output(m21, 1)
    G.output(m22, 0)
    print "left"

def right():
    G.output(m11, 1)
    G.output(m12, 0)
    G.output(m21, 0)
    G.output(m22, 0)
    print "right"

stop()

