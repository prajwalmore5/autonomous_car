# import curses and GPIO
import curses
import RPi.GPIO as GPIO

en = 22
bn = 24

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
p=GPIO.PWM(en,1000)
GPIO.setup(bn,GPIO.OUT)
q=GPIO.PWM(bn,1000)
p.start(100)
q.start(100)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                GPIO.output(38,False)
                GPIO.output(37,True)
                GPIO.output(36,False)
                GPIO.output(35,True)
            elif char == curses.KEY_DOWN:
                GPIO.output(38,True)
                GPIO.output(37,False)
                GPIO.output(36,True)
                GPIO.output(35,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(38,True)
                GPIO.output(37,False)
                GPIO.output(36,False)
                GPIO.output(35,True)
            elif char == curses.KEY_LEFT:
                GPIO.output(38,False)
                GPIO.output(37,True)
                GPIO.output(36,True)
                GPIO.output(35,False)
            elif char == 10:
                GPIO.output(38,False)
                GPIO.output(37,False)
                GPIO.output(36,False)
                GPIO.output(35,False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    

