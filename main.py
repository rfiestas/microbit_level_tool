from microbit import *
granularity = [20, 100, 500]


def position(reading):
    ''' position, calculate the position on the display '''

    res = 0
    modification = 1
    if reading < 0:
        reading = abs(reading)
        modification = -1
    for pos, value in enumerate(granularity):
        res = 2 + (pos * modification)
        if min(value, reading) == reading:
            break
    return res


def replace_char_position(string, position, char):
    ''' replace_char_position, replace a certain position of string '''

    res = string[0:position] + char + string[position+1:]
    return res


def draw(x, y):
    ''' draw, return a image to print in the display '''
    res = ['0' * 5]*5
    if y-1 > -1:
        res[y-1] = replace_char_position(res[y-1], x, '7')
    if y+1 < 5:
        res[y+1] = replace_char_position(res[y+1], x, '7')
    if x-1 > -1:
        res[y] = replace_char_position(res[y], x-1, '7')
    if x+1 < 5:
        res[y] = replace_char_position(res[y], x+1, '7')
    res[y] = replace_char_position(res[y], x, '9')
    
    return Image(''+':'.join(res))


while True:
    x = position(accelerometer.get_x())
    y = position(accelerometer.get_y())
    display.show(draw(x, y))
