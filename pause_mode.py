import game_framework
import game_world
import play_mode
from pico2d import *

image = None


def init():
    global image
    image = load_image('pause.png')


def finish():
    global image
    del image


def update():
    # 게임 월드를 업데이트하지 않으므로 플레이 화면이 멈춘다
    pass


def render():
    clear_canvas()
    game_world.render()        # 멈춘 플레이 화면을 그대로 보여주고
    image.draw(400, 300)       # 그 위에 일시정지 이미지를 띄운다
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
        elif event.type == SDL_KEYUP:
            # 일시정지 중에 뗀 방향키를 소년에게 알려줘야 재개 후 혼자 달리지 않는다
            play_mode.boy.handle_event(event)


def pause(): pass
def resume(): pass
