from pyglet import app, resource, clock
from pyglet.sprite import Sprite
from pyglet.window import Window

window = Window()

ball_image = resource.image('images/ball.png')
ball = Sprite(ball_image)
ball.x = window.width / 2 - ball.width/2
ball.y = window.height / 2 - ball.width/2
ball.speed = 50

@window.event
def on_draw():
    window.clear()
    ball.draw()

def update(dt):
    ball.x = ball.x + ball.speed * dt

clock.schedule_interval(update, 1/60.0)

app.run()
