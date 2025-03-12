import time, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit

print('Rainbow, by ogwel emmanuel')
print('press Ctrl-c to stop the.')
time.sleep(3)

indent = 0
indentIncreasing = True

try:
    while True:
        print('' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if indentIncreasing:
            #increase the number of spaces.
            indent = indent + 1
            if indent == 60: #(!) change this to 10 or 30.
                #change direction.
                indentIncreasing = False
        else:
            #decrease the number of spaces.
            indent =indent - 1
            if indent == 0:
                #change direction.
                indentIncreasing = True

        time.sleep(0.02) #Add a slight pause.
except KeyboardInterrupt:
    sys.exit() #when ctrl-c is pressed, end the programe.
    