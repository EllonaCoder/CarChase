import random
from microbit import *
import music

# Start position of the player (bottom row, middle column)
player_x = 2
player_y = 4

# Enemy starts at top row, random x
enemy_x = random.randint(0, 1)
enemy_y = 0
enemy_x2 = random.randint(2,4)
# Game speed
speed = 500
wining_counter = 0

while True:
    # Clear the screen
    
    display.clear()
    # Move enemy down
    display.set_pixel(enemy_x, enemy_y, 6)
    
    display.set_pixel(enemy_x2, enemy_y, 6)
    enemy_y += 1
    # Draw the player's car
    display.set_pixel(player_x, player_y, 9)
    # Check button presses
    if accelerometer.was_gesture('left') and player_x > 0:
        player_x = player_x - 1
    if  accelerometer.was_gesture('right')and player_x < 4:
        player_x = player_x + 1
    
    sleep(speed)
    
    # Check for crash
    if enemy_y == player_y and (enemy_x == player_x or enemy_x2 == player_x):
        
        music.play(music.BA_DING)
        display.show(Image.SAD)
        sleep(1000)
        display.scroll("Crash!")
        break
    
    # Reset enemy if it reaches bottom
    if enemy_y > 4:
        enemy_y = 0
        enemy_x = random.randint(0, 1)
        enemy_x2 = random.randint(2,4)
        wining_counter = wining_counter + 1
        if wining_counter == 5:
            display.scroll("You are the Winner!Now play next label ")
            if speed > 0:
                speed = speed -100

