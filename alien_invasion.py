import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Create instance of GameStats to store stats, create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
        #Make the Play button
        self.play_button = Button(self, "Play")

    
    def _check_events(self):
        """Respond to kb/m presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    
    def _check_play_button(self, mouse_pos):
        """Start a new game when Play button is pressed"""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset game stats
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            #Get rid of any old bullets and alien ships
            self.aliens.empty()
            self.bullets.empty()

            #Create a new fleet and recenter ship
            self._create_fleet()
            self.ship.center_ship()

            #Hide mouse cursor during game
            pygame.mouse.set_visible(False)
                
    
    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """Create a new bullet and put into bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Updates bullet positions and gets rid of old bullets"""
        self.bullets.update()

        #Delete old bullets to conserve resources
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        

    def _check_bullet_alien_collisions(self):
        #Check for bullets that have hit aliens and get rid of both
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        #Create a new fleet if all old alien ships are gone
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #Increase level counter
            self.stats.level += 1
            self.sb.prep_level()


    def _create_fleet(self):
        """Create a fleet of aliens"""

        #Create an alien and find the number of aliens in a row
        #One alien-sized space in between sprites
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        #Determine the number of alien rows
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height- (3*alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)

        #Create the fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

        
    def _create_alien(self, alien_number, row_number):
        """Create alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    
    def _update_aliens(self):
        """Update the positions of fleet aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        #Detect ship collisions with aliens
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #Check for aliens to hit bottom of the screen
        self._check_aliens_bottom()


    def _check_fleet_edges(self):
        """Do something if an alien is at the edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _check_aliens_bottom(self):
        """Check if aliens touch the bottom of screen and diagnose ship with kill"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


    def _change_fleet_direction(self):
        """Drop fleet downscreen and change direction of motion"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _ship_hit(self):
        """Respond to aliens hitting the ship"""

        #Decrement ships_left
        if self.stats.ships_left > 0:
            #Decrement ship counter
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #Create new fleet to reset new life
            self._create_fleet()
            self.ship.center_ship()

            #Pause
            sleep(.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
    def _update_screen(self):
        """Handles screen refreshing"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Draw the score information
        self.sb.show_score()
        
        #Draw the Play button for game activation
        if not self.stats.game_active:
            self.play_button.draw_button()

        #Make most recently drawn screen visible
        pygame.display.flip()
        
    
    def run_game(self):
        """Start game loop"""

        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()


if __name__ == '__main__':
    #make game instance

    ai = AlienInvasion()
    ai.run_game()