import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "bee"

MOVEMENT_SPEED = 5

TEXTURE_LEFT = 0
TEXTURE_RIGHT = 1


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.textures = []
        # загружаем текстуру поворота "лица" направо и налево
        # flipped_horizontally=True будет отражать картинку, которую мы загрузили, горизонтально
        texture = arcade.load_texture(":resources:images/enemies/bee.png")
        self.textures.append(texture)
        texture = arcade.load_texture(":resources:images/enemies/bee.png", flipped_horizontally=True)
        self.textures.append(texture)

        self.scale = SPRITE_SCALING

        # по умолчанию пчёлка повёрнута вправо 
        self.set_texture(TEXTURE_RIGHT)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Понять, в какую строну повёрнуто "лицо"
        if self.change_x < 0:
            self.texture = self.textures[TEXTURE_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[TEXTURE_RIGHT]

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
   

    def __init__(self, width, height, title):
       "

        super().__init__(width, height, title)

        # Устанавливаем рабочую директорию
        
        file_path = os.path.dirname(os.path.abspath('.'))
        os.chdir(file_path)

        # Переменные который должны храниться в списке спрайтов
        self.all_sprites_list = None

        # установить инфо об игроке
        self.player_sprite = None

        # Уствновить цвет задника
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        
        # список спрайтов
        self.all_sprites_list = arcade.SpriteList()

        # установки игрока
        self.player_sprite = Player()
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.all_sprites_list.append(self.player_sprite)

    def on_draw(self):
     
        
        arcade.start_render()

        # написоывать все спрайты
        self.all_sprites_list.draw()

    def on_update(self, delta_time):
        
        # Обновить все спрайты 
        self.all_sprites_list.update()

    def on_key_press(self, key, modifiers):
      
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
       
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
   
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()