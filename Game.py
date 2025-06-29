import pygame
from Jumper import Jumper
from Tile import Tile
from Ground import Ground
from FallingSprite import FallingSprite
from Flag import Flag

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.jumper = Jumper(screen)
        self.ground = Ground(screen)
        self.tiles = []
        self.tile_trajectories = []
        self.tile_touched = False
        self.scroll_start = False
        self.scroll_amount = 0
        self.timer = 0
        self.music_started = False
        self.falling_sprites = []
        self.flag = Flag(screen, 495, -13360)
        self.victory = False
        self.victory_music_playing = False
        
    
    def generate_tile(self, screen, x, y, x_velocity=0, max_displacement=0):
        self.tiles.append(Tile(screen, x, y, x_velocity, max_displacement))
        # if max_displacement:
        #     self.tile_trajectories.append([x-max_displacement, y+5, 100+max_displacement*2, 1])
        # else:
        #     self.tile_trajectories.append(0)

    def generate_tiles(self, screen):
        self.generate_tile(screen, 600, 600)
        self.generate_tile(screen, 500, 450)
        self.generate_tile(screen, 700, 300)
        self.generate_tile(screen, 600, 150, 2, 200)
        self.generate_tile(screen, 800, 0)
        self.generate_tile(screen, 750, -150, 2, 300)
        self.generate_tile(screen, 600, -300)
        self.generate_tile(screen, 600, -450, -2, 400)
        self.generate_tile(screen, 300, -600, -2, 300)
        self.generate_tile(screen, 200, -750, 1, 150)
        self.generate_tile(screen, 400, -900) # 10
        self.generate_tile(screen, 600, -1050)
        self.generate_tile(screen, 800, -1200, 2, 500)
        self.generate_tile(screen, 400, -1350)
        self.generate_tile(screen, 800, -1500, -2, 500)
        self.generate_tile(screen, 500, -1650)
        self.generate_tile(screen, 300, -1800, -1, 300)
        self.generate_tile(screen, 700, -1950, 2, 300)
        self.generate_tile(screen, 600, -2100)
        self.generate_tile(screen, 800, -2250)
        self.generate_tile(screen, 500, -2400, 3, 500) # 20
        self.generate_tile(screen, 400, -2550, -1, 50)
        self.generate_tile(screen, 600, -2700)
        self.generate_tile(screen, 700, -2850, -2, 200)
        self.generate_tile(screen, 500, -3000)
        self.generate_tile(screen, 700, -3150, 2, 1280)

        self.generate_tile(screen, 1155, -3300)
        # Second phase
        self.generate_tile(screen, 25, -3450)
        self.generate_tile(screen, 200, -3600)
        self.generate_tile(screen, 425, -3750)
        self.generate_tile(screen, 650, -3900)
        self.generate_tile(screen, 800, -4050, 2, 150)
        self.generate_tile(screen, 700, -4200, -2, 200)
        self.generate_tile(screen, 700, -4350, 3, 200) # 34
        self.generate_tile(screen, 800, -4500, -2, 250)
        self.generate_tile(screen, 800, -4650, 3, 150)
        self.generate_tile(screen, 950, -4800)
        self.generate_tile(screen, 1180, -4950)
        self.generate_tile(screen, 0, -5100)
        self.generate_tile(screen, 250, -5250) # 40
        self.generate_tile(screen, 500, -5400)
        # self.generate_tile(screen, 750, -5400)
        self.generate_tile(screen, 700, -5550)
        self.generate_tile(screen, 800, -5700, -2, 100)
        self.generate_tile(screen, 800, -5850, 2, 200)
        self.generate_tile(screen, 700, -6000)
        self.generate_tile(screen, 850, -6150)
        self.generate_tile(screen, 700, -6300)
        self.generate_tile(screen, 850, -6450)
        self.generate_tile(screen, 775, -6600)
        self.generate_tile(screen, 525, -6750)
        self.generate_tile(screen, 275, -6900)
        self.generate_tile(screen, 400, -7050)
        self.generate_tile(screen, 650, -7200)
        self.generate_tile(screen, 900, -7350)
        self.generate_tile(screen, 800, -7500, -2, 150)
        self.generate_tile(screen, 800, -7650, 2, 150)
        self.generate_tile(screen, 800, -7800)
        self.generate_tile(screen, 1050, -7950)
        self.generate_tile(screen, 900, -8100)
        self.generate_tile(screen, 700, -8250)
        self.generate_tile(screen, 500, -8400)
        self.generate_tile(screen, 300, -8550)
        self.generate_tile(screen, 100, -8700)
        self.generate_tile(screen, 275, -8850)
        self.generate_tile(screen, 450, -9000)
        self.generate_tile(screen, 625, -9150)
        ### Invisible tiles ###
        self.generate_tile(screen, 900, -9300) # 67
        self.generate_tile(screen, 700, -9400)
        self.generate_tile(screen, 500, -9500)
        self.generate_tile(screen, 300, -9600)
        ### Invisible tiles ###
        self.generate_tile(screen, 100, -9700)
        self.generate_tile(screen, 200, -9850)
        self.generate_tile(screen, 300, -10000)
        self.generate_tile(screen, 100, -10150)
        self.generate_tile(screen, 275, -10300, -2, 100)
        self.generate_tile(screen, 450, -10450)
        self.generate_tile(screen, 625, -10600)
        self.generate_tile(screen, 900, -10750)
        self.generate_tile(screen, 900, -10900, 3, 100)
        self.generate_tile(screen, 700, -11050, -3, 100)
        self.generate_tile(screen, 500, -11200, 3, 100)
        self.generate_tile(screen, 300, -11350, -3, 100)
        self.generate_tile(screen, 200, -11500)
        self.generate_tile(screen, 200, -11650) # 85
        self.generate_tile(screen, 25, -11800)
        self.generate_tile(screen, 25, -11950)
        self.generate_tile(screen, 1155, -12100)
        self.generate_tile(screen, 1000, -12250)
        self.generate_tile(screen, 1155, -12400)
        self.generate_tile(screen, 25, -12550)
        self.generate_tile(screen, 175, -12700)
        self.generate_tile(screen, 25, -12850)
        self.generate_tile(screen, 175, -13000)
        self.generate_tile(screen, 325, -13150)
        self.generate_tile(screen, 475, -13300)


    def draw_tile_trajectories(self):
        for trajectory in self.tile_trajectories:
            if trajectory:
                pygame.draw.rect(self.screen, (100, 100, 100), trajectory)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        if self.victory:
            self.jumper.draw_victory(self.screen, self.timer)
        else:
            self.jumper.draw(self.screen)
            self.ground.draw()
            for tile in self.tiles:
                if tile.id == 67:
                    print(f"Audio is at: {pygame.mixer.music.get_pos()}")
                    if self.scroll_amount == 2 and pygame.mixer.music.get_pos() >= 47900:
                        tile.draw()
                elif tile.id == 68:
                    if self.scroll_amount == 2 and pygame.mixer.music.get_pos() >= 47900+385:
                        tile.draw()
                elif tile.id == 69:
                    if self.scroll_amount == 2 and pygame.mixer.music.get_pos() >= 47900+2*385:
                        tile.draw()
                elif tile.id == 70:
                    if self.scroll_amount == 2 and pygame.mixer.music.get_pos() >= 47900+3*385:
                        tile.draw()
                # elif tile.id == 73:
                #     if self.timer >= 6710:
                #         tile.draw()
                else:
                    tile.draw()
            self.draw_tile_trajectories()
            self.flag.draw()
            for falling in self.falling_sprites:
                falling.draw()

    def move_tiles(self):
        for tile in self.tiles:
            if tile.max_displacement != 0:
                if tile.displacement >= tile.max_displacement or tile.x >= 1280 - tile.width or tile.displacement <= -tile.max_displacement or tile.x <= 0:
                    tile.x_velocity = -tile.x_velocity
                tile.displacement += tile.x_velocity
                tile.x += tile.x_velocity

    def scroll(self):
        if self.tile_touched or self.scroll_start:
            if self.scroll_amount != 2:
                self.scroll_amount = 1
            self.scroll_start = True
            self.ground.y += self.scroll_amount
            for tile in self.tiles:
                tile.y += self.scroll_amount
            self.jumper.y += self.scroll_amount
            for falling in self.falling_sprites[:]:
                if falling is not None:
                    falling.y += self.jumper.terminal_velocity / 2
                    if falling.update():
                        self.falling_sprites.remove(falling)
            for trajectory in self.tile_trajectories:
                if trajectory:
                    trajectory[1] += 1
            self.flag.y += self.scroll_amount

            if not self.music_started:
                self.music_started = True
                music = "assets/Long Away Home.wav"
                pygame.mixer.music.load(music)
                pygame.mixer.music.play()
                pygame.mixer.music.queue("assets/leap.wav")

    def update(self):
        if self.victory:
            self.flag.captured = True
            self.timer += 1
            if not self.victory_music_playing:
                self.victory_music_playing = True
                pygame.mixer.music.load("assets/Victory.wav")
                pygame.mixer.music.play()
            if not pygame.mixer.music.get_busy():
                pygame.quit()
                exit()
        else:
            self.tile_touched = self.jumper.update(self.screen, self.ground, self.tiles)
            for falling in self.falling_sprites[:]:
                if falling.update():
                    self.falling_sprites.remove(falling)
            if self.jumper.dead:
                self.game_over()
            if self.scroll_start:
                self.move_tiles()
            self.scroll()
            # print(f"Jumper position: {self.jumper.x}, {self.jumper.y}")
            if self.scroll_start:
                self.timer += 1
            # 1680 is where dinos start falling
            if self.timer == 1680:
                self.falling_sprites.append(FallingSprite(self.screen, 900, -50))
            if self.timer == 2060:
                self.falling_sprites.append(FallingSprite(self.screen, 200, -50))
            if self.timer == 3050:
                self.falling_sprites.append(FallingSprite(self.screen, 900, -50))
            if self.timer == 4300:
                self.falling_sprites.append(FallingSprite(self.screen, 350, -50))
            if self.timer == 5100:
                self.falling_sprites.append(FallingSprite(self.screen, 300, -50))
            if self.timer == 6150:
                self.falling_sprites.append(FallingSprite(self.screen, 200, -50))
            if self.timer == 6600:
                self.falling_sprites.append(FallingSprite(self.screen, 1080/2, -50))
            if self.timer == 8200:
                self.falling_sprites.append(FallingSprite(self.screen, 1080/2, -50))
            if self.timer == 8250:
                self.falling_sprites.append(FallingSprite(self.screen, 1080/2+200, -50))
            if self.timer == 8300:
                self.falling_sprites.append(FallingSprite(self.screen, 1080/2-200, -50))
            if pygame.mixer.music.get_pos() <= 50 and self.timer > 1000:
                self.scroll_amount = 2
            if self.jumper.collide_with_flag(self.flag):
                self.victory = True
                print("Victory!")

        # print(f"Timer: {self.timer}")

    def game_over(self):
        print("Game over!")
        pygame.quit()
        exit()