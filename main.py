import pygame
import sys
import pymunk
import math
import pymunk.pygame_util

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def calculate_angle(p1, p2):    
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def draw(space, window, draw_options):
    window.fill((255, 255, 255))
    space.debug_draw(draw_options)# Draw the objects in the space 
    pygame.display.update()

def create_boundaries(space, width, height):
    rects =[
        [(width/2, height - 10), (width, 20)], # Bottom rectangle
        [(width/2,  10), (width, 20)], 
        [(10, height/2), (20, height)], 
        [(width - 10, height/2), (20, height)] 
    ]
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC) # Create a static body
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)


def create_ball(space, radius, mass, pos):
    body = pymunk.Body() # Create a body with mass and moment of inertia
    body.position = pos  # Set the position of the body
    shape = pymunk.Circle(body, radius) # Create a circle shape with the body and radius
    shape.mass = mass
    shape.elasticity = 0.95 # Set the elasticity of the shape
    shape.friction = 0.9 # Set the friction of the shape
    shape.color = (255, 0, 0, 100) # Set the color of the shape
    space.add(body, shape)  # Add the shape to the body
    return shape

    
def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1.0 / fps  # delta time =  dt

    space = pymunk.Space() # Create a space for the object to move in
    space.gravity = (0, 981) # Set the gravity

    pressed_pos = None
    ball = None

    create_boundaries(space, width, height) # Create the boundaries
    draw_options = pymunk.pygame_util.DrawOptions(window) # Draw options for the objects

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ball:
                    pressed_pos = pygame.mouse.get_pos()
                    ball = create_ball(space, 30, 10, pressed_pos)
                elif pressed_pos:
                    ball.body.apply_impulse_at_local_point((10000, 0), (0, 0))
                    pressed_pos = None
                else:
                    space.remove(ball.body, ball)
                    ball = None
                


        draw(space,window,draw_options)   
        space.step(dt) # Step the space in time   
        clock.tick(fps)
    pygame.quit() # Quit Pygame

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT) # Run the game
