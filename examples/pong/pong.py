from pyglet import app, resource, clock
from pyglet.sprite import Sprite
from pyglet.window import Window

window = Window()

ball_image = resource.image('images/ball.png')
ball = Sprite(ball_image)
ball.x = window.width / 2 - ball.width/2
ball.y = window.height / 2 - ball.width/2
ball.speed_x = 50
ball.speed_y = 50

PADDLE_MARGIN = 10

paddle_image = resource.image('images/paddle.png')
paddle1 = Sprite(paddle_image)
paddle1.x = PADDLE_MARGIN
paddle1.y = window.height / 2 - paddle1.height / 2
paddle2 = Sprite(paddle_image)
paddle2.x = window.width - paddle2.width - PADDLE_MARGIN
paddle2.y = window.height / 2 - paddle2.height / 2

@window.event
def on_draw():
    window.clear()
    ball.draw()
    paddle1.draw()
    paddle2.draw()


def update(dt):
    ball.x = ball.x + ball.speed_x * dt
    ball.y = ball.y + ball.speed_y * dt

    if ball.x < 0  or (ball.x +  ball.width) > window.width:
        ball.speed_x = ball.speed_x * -1

    if ball.y < 0 or (ball.y + ball.width) > window.height:
        ball.speed_y = ball.speed_y * -1

clock.schedule_interval(update, 1/60.0)

app.run()
