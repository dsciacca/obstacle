import RPi.GPIO as G
import time, datetime
import telepot
from telepot.loop import MessageLoop

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

G.output(led, 1)

time.sleep(5)

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

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].lower()
    print 'Received: %s' % command
    
    if command == '/right':
        right()
    elif command == '/left':
        left()
    elif command == '/forward':
        forward()
    elif command == '/back' or command == '/backward':
        back()
    elif command == '/stop':
        stop()
    else:
        print 'ERROR: Invalid syntax. Valid options include: /forward, /back, /left, /right, /stop'
        telegram_bot.sendMessage(chat_id, str("ERROR: Invalid command, valid options include:\n /forward \n /back \n /right \n /left \n /stop"))

    
stop()
count = 0

telegram_bot = telepot.Bot('656285412:AAHyiw8T9ybTJJMTnDak21uYFMkgXfw-FCw')
print(telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running.....'

while True:
    time.sleep(2)
'''while True:
    i = 0
    avgDistance = 0
    for i in range(5):
        G.output(TRIG, False)
        time.sleep(0.1)
        G.output(TRIG, True)
        time.sleep(0.00001)
        G.output(TRIG, False)
        while G.intput(ECHO) == 0:
            G.output(led, False)
        pulse_start = time.time()
        while G.input(ECHO) == 1:
            G.output(led, True)
        pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        avgDistance = avgDistance + distance
    avgDistance = avgDistance / 5
    print avgDistance
    flag = 0
    if avgDistance < 15:
        count = count + 1
        stop()
        time.sleep(1)
        back()
        time.sleep(1.5)
        if (count % 3 == 1) and (flag == 0):
            right()
            flag = 1
        else:
            left()
            flag = 0
        time.sleep(1.5)
        stop()
        time.sleep(1)
    else:
        forward()
        flag = 0
'''
