'''
05/17/2021

Pygame Intro

Pygame
- A Set of Python Modules Designed for Designing video Games

Coordinates in Pygame Window
- The Top Left Corner of the Screen is (0,0) and Bottom Right is (width, height).
- Positive x-Direction is to the Right and Negative x-Direction is to the Left.
- Positive y-Direction is Downwards and Negative y-Direction is Upwards.

Important Pygame Functions
1. Import the Pygame Library
import pygame

2. Initialize the Pygame
pygame.init()

3. Create a Pygame Window with Size (width, height)
variable1 = pygame.display.set_mode((W, H))

4. Accepting Key Inputs From the User
pygame.key.get_presses()

5. Setup Delay Time (## in ms, (1s == 1000ms))
pygame.time.delay(##)

6. Update Frames 
pygame.display.update()

7. Terminate the Pygame at the End
pygame.quit()
'''

# 1.Import the Pygame Library
import pygame

# 2. Initialize the Pygame
pygame.init()

# 3. Make a Pygame Window (width, height)
window = pygame.display.set_mode((500, 500))

# 4. Setup a Caption(Game Name) on Window to "First Game"
pygame.display.set_caption("First PyGame")

# 5. Set Variables and Values (Starting Coordinates)
# Assign 10 to 'x'
# Assign 10 to 'y'
x = 10
y = 10

# 6. Create an Object (width and height) and Speed
# Assign 10 to 'width'
# Assign 15 to 'height'
# Assign 5 to 'speed'
width = 10
height = 15
speed = 5

# 7. Create a Control Variable
# Assign True to 'run'
run = True

# 8. Launching a Game with the Control Variable
while(run):

	# 9. Set Delay Time to 100ms
	pygame.time.delay(100)

	# 10. Function the Button
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			# 11. Terminate Game When the Button is Pressed
			# Reassign False to 'run'
			run = False

	# 12. Activate Keys
	keys = pygame.key.get_pressed()

	# 13. Left Arrow Key Pressds, Then Decrease Value of x
	if keys[pygame.K_LEFT]:
		x -= speed

	# 14. Right Arrow Key Pressed, Then Increase Value of x
	if keys[pygame.K_RIGHT]:
		x += speed

	# 15. Up Arrow Key Pressed, Then Decrease Value of y
	if keys[pygame.K_UP]:
		y -= speed

	# 16. Down Arrow Key Pressed, Then Increase Value of y
	if keys[pygame.K_DOWN]:
		y += speed

	# 19. As the Object Moves, the Background Update
	window.fill((0, 0, 0))

	# 17. Setup a Rectangle as a Moving Object
	pygame.draw.rect(window, (50, 150, 23), (x, y, width, height))

	# 18. Update the Game 
	pygame.display.update()

# 11. Quit Out of the Game
pygame.quit()
