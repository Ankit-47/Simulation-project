import pygame
import sys
import pymunk
import math
import pymunk.pygame_util

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))



def draw(space, window, draw_options):
    window.fill((255, 255, 255))
    space.debug_draw(draw_options)# Draw the objects in the space 
    pygame.display.update()

def create_ball(space, radius, mass):
    body = pymunk.Body() # Create a body with mass and moment of inertia
    body.position = (300, 300) # Set the position of the body
    shape = pymunk.Circle(body, radius) # Create a circle shape with the body and radius
    shape.mass = mass
    shape.color = (255, 0, 0, 100) # Set the color of the shape
    shape.add(body, shape)  # Add the shape to the body
    return shape

    
def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1.0 / fps  # delta time =  dt
    space = pymunk.Space() # Create a space for the object to move in
    space.gravity = (0, 981) # Set the gravity
    draw_options = pymunk.pygame_util.DrawOptions(window) # Draw options for the objects

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(space,window,draw_options)   
        space.step(dt) # Step the space in time   
        clock.tick(fps)
    pygame.quit() # Quit Pygame

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)
