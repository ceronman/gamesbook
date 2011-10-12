import math

from pyglet import app, resource, clock
from pyglet.sprite import Sprite
from pyglet.text import Label
from pyglet.window import Window, key

window = Window()

MAX_BALL_SPEED = 500
INITIAL_BALL_SPEED = 400

ball_image = resource.image('images/ball.png')
ball = Sprite(ball_image)
ball.x = window.width / 2 - ball.width/2
ball.y = window.height / 2 - ball.width/2

ball.speed_x = INITIAL_BALL_SPEED
ball.speed_y = INITIAL_BALL_SPEED

PADDLE_MARGIN = 10

paddle_image = resource.image('images/paddle.png')
paddle1 = Sprite(paddle_image)
paddle1.x = PADDLE_MARGIN
paddle1.y = window.height / 2 - paddle1.height / 2
paddle1.speed = 400
paddle2 = Sprite(paddle_image)
paddle2.x = window.width - paddle2.width - PADDLE_MARGIN
paddle2.y = window.height / 2 - paddle2.height / 2
paddle2.speed = 400

score_1 = 0
score_2 = 0

score_label_1 = Label('0',
                      font_size=48,
                      x = window.width/4,
                      y = window.height,
                      anchor_x = 'center',
                      anchor_y = 'top')

score_label_2 = Label('0',
                      font_size=48,
                      x = 3 * window.width/4,
                      y = window.height,
                      anchor_x = 'center',
                      anchor_y = 'top')

state = 'playing'

pause_label = Label('PAUSED',
                    font_size=36,
                    x = window.width/2,
                    y = window.height/2,
                    anchor_x = 'center', anchor_y = 'center')

@window.event
def on_draw():
    window.clear()
    if state == 'playing' or state == 'scored':
        ball.draw()
        paddle1.draw()
        paddle2.draw()
        score_label_1.draw()
        score_label_2.draw()
    if state == 'paused':
        pause_label.draw()

@window.event
def on_key_press(symbol, modifiers):
    global state
    if state == 'scored':
        state = 'playing'
    elif symbol == key.P:
        state = 'paused' if state == 'playing' else 'playing'

keys = key.KeyStateHandler()
window.push_handlers(keys)

def update(dt):
    global state

    if state == 'paused' or state == 'scored':
        return

    elif state == 'playing':
        ball.x = ball.x + ball.speed_x * dt
        ball.y = ball.y + ball.speed_y * dt

        if ball.x < (PADDLE_MARGIN + paddle1.width):
            ball.x = PADDLE_MARGIN + paddle1.width
            if ((ball.y + ball.height) > paddle1.y
                and (ball.y - ball.height) < (paddle1.y + paddle1.height)):
                ball.speed_x = ball.speed_x * -1
                ball_center = ball.y + ball.height / 2
                paddle_center = paddle1.y + paddle1.height / 2
                paddle_distance = abs(paddle_center - ball_center)
                speed_y = MAX_BALL_SPEED * 2 * paddle_distance / paddle1.height
                ball.speed_y = math.copysign(speed_y, ball.speed_y)
            else:
                global score_2
                score_2 = score_2 + 1
                score_label_2.text = str(score_2)
                ball.x = window.width / 2
                ball.y = window.height / 2
                ball.speed_x = ball.speed_x * -1
                ball.speed_y = INITIAL_BALL_SPEED
                state = 'scored'

        if (ball.x + ball.width) > paddle2.x:
            ball.x = paddle2.x - ball.width
            if ((ball.y + ball.height) > paddle2.y
                and (ball.y - ball.height) < (paddle2.y + paddle2.height)):
                ball.speed_x = ball.speed_x * -1
                ball_center = ball.y + ball.height / 2
                paddle_center = paddle2.y + paddle2.height / 2
                paddle_distance = abs(paddle_center - ball_center)
                speed_y = MAX_BALL_SPEED * 2 * paddle_distance / paddle2.height
                ball.speed_y = math.copysign(speed_y, ball.speed_y)
            else:
                global score_1
                score_1 = score_1 + 1
                score_label_1.text = str(score_1)
                ball.x = window.width / 2
                ball.y = window.height / 2
                ball.speed_x = ball.speed_x * -1
                ball.speed_y = INITIAL_BALL_SPEED
                state = 'scored'

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
