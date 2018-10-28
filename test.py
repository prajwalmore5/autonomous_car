import sys
import time
import pygame
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.cleanup()

Left = 35
Right = 36
Forward = 37
Backward = 38
 
sleeptime=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

pygame.init()
gameDisplay = pygame.display.set_mode((200,200))
pygame.display.set_caption('test')

def forward(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)

def reverse(x):
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward, GPIO.LOW)

def left(x):
    GPIO.output(Left, GPIO.HIGH)
    print("Moving Left")
    time.sleep(x)
    GPIO.output(Left, GPIO.LOW)

def right(x):
    GPIO.output(Right, GPIO.HIGH)
    print("Moving Right")
    time.sleep(x)
    GPIO.output(Right, GPIO.LOW)



while True:
    '''
    direction = input("enter direction")

    if direction = 'w':
        turn = input("enter turn")
        if turn = 'd':
            right(5)
            forward(5)
        elif turn = 'a':
            left(5)
            forward(5)

    elif direction = 's':
        turn = input("enter turn")
        if turn = 'd':
            right(5)
            reverse(5)
        elif turn = 'a':
            left(5)
            reverse(5)
    '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                forward(5)
            elif event.key == pygame.K_DOWN:
                reverse(5)
            elif event.key == pygame.K_LEFT:
                left(5)
            elif event.key == pygame.K_RIGHT:
                right(5)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                reverse(0)

        GPIO.cleanup()
