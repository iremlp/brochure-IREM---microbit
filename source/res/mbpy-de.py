from microbit import *
from random import randint

### création des images (pour niveau 1 , 2 et 3)
un = Image("00000:00000:00900:00000:00000")
deux = Image("00009:00000:00000:00000:90000")
trois = Image("90000:00000:00900:00000:00009")
quatre = Image("90009:00000:00000:00000:90009")
cinq = Image("90009:00000:00900:00000:90009")
six = Image("90009:00000:90009:00000:90009")

### niveau 0

while True:
    if button_a.get_presses():
        display.show(str(randint(1, 6)))
        sleep(800)
        display.clear()


####### niveau 1 ####### 

issues = [un, deux, trois, quatre, cinq, six]

while True:
    if button_a.get_presses():
        i = randint(0, 5)
        display.show(issues[i])
        sleep(800)
        display.clear()
        
        
####### niveau 2 ####### 

data = [0, 0, 0, 0, 0, 0]

while True:
    if button_a.get_presses():
        i = randint(0, 5)        
        display.show(issues[i])
        data[i] = data[i] + 1
        sleep(1000)
        display.clear()
        
    if button_b.get_presses():
        for effectif in data :
            display.scroll(str(effectif)+" /")
            

####### niveau 3 ####### 

N = 0
data = [0, 0, 0, 0, 0, 0]
def frequence(e,N):
    freq = e / N
    return round(freq,2)

while True:
    if button_a.get_presses():
        for n in range(30):
            N = N + 1
            i = randint(0, 5)        
            display.show(issues[i])
            data[i] += 1
            sleep(1000)
            display.clear()
        
    if button_b.get_presses():
        for effectif in data :
            f = frequence(effectif,N)
            display.scroll(str(f)+" /")

