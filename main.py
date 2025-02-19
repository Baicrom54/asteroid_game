import pygame
from constants import *
from player import Player
import random
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    bullets=pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Shot.containers=(bullets,updatable,drawable)
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable,)
    player=Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroid_field1=AsteroidField()
    dt=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for ent in updatable:
            ent.update(dt)
        for bullet in bullets:
            for ast in asteroids:
                condition_player=ast.detect_collision(player)
                if condition_player:
                    print("Game Over")
                    return
                condition_bullet=bullet.detect_collision(ast)
                if condition_bullet:
                    bullet.kill()
                    ast.split() 
        pygame.Surface.fill(screen,(0,0,0))
        for ent in drawable:
            ent.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000

if __name__ == "__main__":
    main()