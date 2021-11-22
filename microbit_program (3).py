# Add your Python code here. E.g.
from microbit import *

spaceship = [0,4]
#alien = [0,0]
missile =[0,0]




def draw():
    display.clear()
    if flag==True:
        display.set_pixel(missile[0], missile[1], 5)
        # Draw the players spaceship.

    display.set_pixel(spaceship[0], spaceship[1], 9)
  
    # Draw the players alien.
#    display.set_pixel(alien[0], 0, 9)

def move_entities():
    
#    alien[0]-=1
    if flag==True:
        missile[1]-=1 
    if direction == 0: 
        spaceship[0]+=1
    if direction == 1: 
        spaceship[0]-=1    
#def handle_input():
#    if button_a.was_pressed():
#        missile[0]=4
        

#def move_missiles():
    # Advance positions of missiles (upwards)
#    missile[1]-=1        
flag=False
direction = 0
while True:
#    handle_input()
   
    if button_a.was_pressed():
        flag=True
        missile[0]=spaceship[0]
        missile[1]=4
    if spaceship[0]==4:
        direction = 1
    if spaceship[0]==0:
        direction = 0    
    move_entities()
    draw()
    sleep(2000)