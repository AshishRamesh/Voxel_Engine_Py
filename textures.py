import pygame as pg
import moderngl as mgl 

class Textures:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        self.texture_0 = self.load('frame.png')
        self.texture_0.use(location=0)
        print(self.ctx.error)  # Check if any OpenGL errors are raised.


    def load(self, file_name):
        texture = pg.image.load(f'assets/{file_name}')
        texture = pg.transform.flip(texture, flip_x = True, flip_y=False)

        texture = self.ctx.texture(
            size = texture.get_size(),
            components=4,
            data=pg.image.tostring(texture, 'RGBA', False)
        )
        texture.anisotropy = 32.0
        texture.build_mipmaps()
        texture.filter = (mgl.LINEAR ,mgl.LINEAR)
        print(self.ctx.error)  # Check if any OpenGL errors are raised.

        return texture