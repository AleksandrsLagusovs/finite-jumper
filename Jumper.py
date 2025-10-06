
import pygame

class Jumper:
 
    def __init__(self, screen):
      
        self.screen = screen
        self.x = 400
        self.y = 500
        self.width = pygame.image.load("assets/down.png").get_width()
        self.height = pygame.image.load("assets/down.png").get_height()
        self.previous_height = self.y
        self.x_velocity = 0
        self.y_velocity = 1
        self.terminal_velocity = 12
        self.gravity = 0.5
        self.crouch_time = 0
        self.crouching = False
        self.crouch_duration = 20
        self.moving_right = False
        self.moving_left = False
        self.last_direction = "right"
        self.bounce_velocity = -13  # Fixed bounce velocity
        self.jumping = pygame.image.load("assets/jumping.png")
        self.up = pygame.image.load("assets/up.png")
        self.down = pygame.image.load("assets/down.png")
        self.tile_touched = False
        self.dead = False
        self.angle = 0

    def draw(self, screen):
    
        if self.crouching:
            image = self.jumping
        elif self.y_velocity > 0:
            image = self.down
        else:
            image = self.up
        # Check if moving left or right and update last_direction
        if self.moving_left:
            image = pygame.transform.flip(image, True, False)
            self.last_direction = "left"
        elif self.moving_right:
            self.last_direction = "right"
        else:
            # Use the last direction if not moving
            if self.last_direction == "left":
                image = pygame.transform.flip(image, True, False)

        screen.blit(image, (self.x, self.y))

    def draw_victory(self, screen, time):
     
        # Alternate between "jumping" and "up" images every 20 frames
        if time % 40 < 20:
            image = self.down
        else:
            image = self.up
        screen.blit(image, (self.x, self.y))


    def collide_with_tile(self, tiles):
       
        for tile in tiles:
            if ((self.x + self.width > tile.x and self.x < tile.x + tile.width and
                self.y + self.height >= tile.y and self.y + self.height <= tile.y + tile.height) and
                self.y_velocity >= 0 and self.y > 0):
                # Align the jumper's feet with the top of the tile
                self.y = tile.y - self.height+5
                return tile
        return None
    
    def collide_with_ground(self, ground):
      
        if self.y + self.height >= ground.y:
            return True
        return False
    
    def collide_with_flag(self, flag):
      
        if (self.x + self.width > flag.x and self.x < flag.x + flag.width and
            self.y + self.height >= flag.y and self.y < flag.y + flag.height):
            return True
        return False
    
    def rotate(self):
      
        self.angle += 10
        if self.angle >= 360:
            self.angle = 0
        self.image = pygame.transform.rotate(pygame.image.load("assets/down.png"), self.angle)

    def update(self, screen, ground, tiles):
        
        if self.y > 850:
            self.dead = True

        self.previous_height = self.y

        # Apply gravity
        if self.y_velocity < self.terminal_velocity:
            self.y_velocity += self.gravity

        # Bouncing off the ground
        if self.collide_with_ground(ground) and self.y_velocity >= 0 and not self.tile_touched:
            if self.y + self.height > self.previous_height + 720:
                self.dead = True
            self.y_velocity = self.bounce_velocity
            self.crouching = True

        # Bouncing off a tile
        elif self.collide_with_tile(tiles) is not None and self.y_velocity >= 0:
            tile = self.collide_with_tile(tiles)
            self.tile_touched = True
            self.crouching = True

        # Crouching
        if self.crouching:
            self.crouch_time += 1
            self.y_velocity = 0
            tile = self.collide_with_tile(tiles)
            if tile is not None and tile.x_velocity != 0:
                self.x += tile.x_velocity
            if self.crouch_time >= self.crouch_duration:
                self.crouching = False
                self.crouch_time = 0
                self.y_velocity = self.bounce_velocity

        # Vertical movement
        self.y += self.y_velocity

        # Horizontal movement
        if not self.crouching:
            if self.moving_left:
                self.x -= 5
                if self.x < 0:
                    self.x = 1280
            if self.moving_right:
                self.x += 5
                if self.x > 1280:
                    self.x = 0

        self.draw(screen)
        return self.tile_touched