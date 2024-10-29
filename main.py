import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatables, drawables)

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatables, drawables)

    AsteroidField.containers = (updatables)
    asteroidfield = AsteroidField()


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()