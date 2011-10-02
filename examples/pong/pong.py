from pyglet import app, resource, clock
from pyglet.sprite import Sprite
from pyglet.window import Window, key

window = Window()
keys = key.KeyStateHandler()
window.push_handlers(keys)

ball_image = resource.image('images/ball.png')
ball = Sprite(ball_image)
ball.x = window.width / 2 - ball.width/2
ball.y = window.height / 2 - ball.width/2
ball.speed_x = 200
ball.speed_y = 200

PADDLE_MARGIN = 10

paddle_image = resource.image('images/paddle.png')
paddle1 = Sprite(paddle_image)
paddle1.x = PADDLE_MARGIN
paddle1.y = window.height / 2 - paddle1.height / 2
paddle1.speed = 200
paddle2 = Sprite(paddle_image)
paddle2.x = window.width - paddle2.width - PADDLE_MARGIN
paddle2.y = window.height / 2 - paddle2.height / 2
paddle2.speed = 200

@window.event
def on_draw():
    window.clear()
    ball.draw()
    paddle1.draw()
    paddle2.draw()


def update(dt):
    ball.x = ball.x + ball.speed_x * dt
    ball.y = ball.y + ball.speed_y * dt

    if ball.x < (PADDLE_MARGIN + paddle1.width):
        ball.x = PADDLE_MARGIN + paddle1.width
        if ((ball.y + ball.height) > paddle1.y
            and (ball.y - ball.height) < (paddle1.y + paddle1.height)):
            ball.speed_x = ball.speed_x * -1
        else:
            ball.x = window.width / 2
            ball.y = window.height / 2

    if (ball.x + ball.width) > paddle2.x:
        ball.x = paddle2.x - ball.width
        if ((ball.y + ball.height) > paddle2.y
            and (ball.y - ball.height) < (paddle2.y + paddle2.height)):
            ball.speed_x = ball.speed_x * -1
        else:
            ball.x = window.width / 2
            ball.y = window.height / 2

    if (ball.y + ball.height) > window.height:
        ball.y = window.height - ball.height
        ball.speed_y = ball.speed_y * -1

    if ball.y < 0:
        ball.y = 0
        ball.speed_y = ball.speed_y * -1


    if keys[key.A] and paddle1.y < (window.height - paddle1.height):
        paddle1.y = paddle1.y + paddle1.speed * dt

    if keys[key.Z] and paddle1.y > 0:
        paddle1.y = paddle1.y - paddle1.speed * dt

    if keys[key.UP] and paddle2.y < (window.height - paddle2.height):
        paddle2.y = paddle2.y + paddle2.speed * dt

    if keys[key.DOWN] and paddle2.y > 0:
        paddle2.y = paddle2.y - paddle2.speed * dt

clock.schedule_interval(update, 1/60.0)

app.run()
