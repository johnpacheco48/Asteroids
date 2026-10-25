import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shots import Shot

print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():

    print("Hello from asteroids!")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = shots, drawable, updatable
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    field = AsteroidField()
    ship = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    ship.containers = (updatable, drawable)
    field.containers = asteroids
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for objects in asteroids:
            for shot in shots:
                if objects.collides_with(shot):
                    log_event("asteroid_shot")
                    objects.split()
                    shot.kill()
        for objects in asteroids:
            if ship.collides_with(objects):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for objects in drawable:
            objects.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
