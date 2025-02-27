#!/usr/bin/env python3

import sys
import pygame
from constants import * # load pygame library and constants module
from player import Player # load player module
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # screen object
    clock = pygame.time.Clock() # clock object

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0 # establish counter
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()