import pygame
from pygame.sprite import Group
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # https://discord.com/channels/551921866173054977/1278020140323049662/1278020140323049662
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # player.update(delta_time)
        for obj in updatable:
            obj.update(delta_time)
        screen.fill('black')
        for obj in asteroids:
            if obj.collision(player):
                print('Game over')
                return
            for shot in shots:
                if obj.collision(shot):
                    obj.split()
                    shot.kill()
        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
