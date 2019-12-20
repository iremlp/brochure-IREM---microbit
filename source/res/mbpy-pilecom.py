from microbit import *
import random
import radio

radio.on()

f = 0
p = 0

def anim():
    tab = [Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE,
           Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW]
    display.show(tab, delay=80)

while True:
    if accelerometer.was_gesture('shake'):
        tirage = random.randint(1, 100)
        anim()
        if tirage <= 55:
            display.show("P")
            radio.send('P')
        else:
            display.show("F")
            radio.send('F')
        sleep(10)
   
    issue = radio.receive()
    if issue == 'P':
        p += 1
    if issue == 'F':
        f += 1
    if p+f > 0:
        a = p/(p+f)
        b = f/(p+f)
    else:
        a, b = 0, 0
    print((a, b))
    sleep(10)