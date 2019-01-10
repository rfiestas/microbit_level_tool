from microbit import *
granularity = [20, 100, 500]

def position(reading):
    modification = 1
    if reading < 0:
        reading = abs(reading)
        modification = -1
    for pos, value in enumerate(granularity):
        res = 2 + (pos * modification)
        if min(value, reading) == reading:
            break
    return res

def replaceCharPosition(string, poition, char):
    res = string[0:poition] + char + string[poition+1:]
    return res
    
def draw(x, y):
    res = ['0' * 5]*5
    if y-1 > -1:
        res[y-1] = replaceCharPosition(res[y-1], x, '7')
    if y+1 < 5:
        res[y+1] = replaceCharPosition(res[y+1], x, '7')
    if x-1 > -1:
        res[y] = replaceCharPosition(res[y], x-1, '7')
    if x+1 < 5:
        res[y] = replaceCharPosition(res[y], x+1, '7')
    res[y] = replaceCharPosition(res[y], x, '9')
    
    return Image(''+':'.join(res))

while True:
    x = position(accelerometer.get_x())
    y = position(accelerometer.get_y())
    display.show(draw(x, y))
