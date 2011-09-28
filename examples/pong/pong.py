from pyglet import app, resource
from pyglet.sprite import Sprite
from pyglet.window import Window

window = Window()

ball_image = resource.image('images/ball.png')
ball = Sprite(ball_image)
ball.x = window.width / 2 - ball.width/2
ball.y = window.height / 2 - ball.width/2

@window.event
def on_draw():
    window.clear()
    ball.draw()

app.run()
