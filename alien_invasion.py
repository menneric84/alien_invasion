import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets
    bullets = Group()
    # Make an alien fleet
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for hte game.
    while True:
        # Watch for keyboard and mouse pygame.examples.eventlist.main()
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # Make the most recently drawn screen visible
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()