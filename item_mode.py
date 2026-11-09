import game_framework
import game_world
import play_mode
from pico2d import *

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def update():
    # 일시정지 모드와 달리 월드를 계속 업데이트하므로 소년이 움직일 수 있다
    game_world.update()


def render():
    clear_canvas()
    game_world.render()        # 진행 중인 플레이 화면 위에
    image.draw(400, 300)       # 아이템 선택창을 띄운다
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            play_mode.boy.item = None
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            play_mode.boy.item = 'SmallBall'
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            play_mode.boy.item = 'BigBall'
            game_framework.pop_mode()
        else:
            # 나머지 입력(방향키 등)은 소년에게 넘겨서 계속 조작할 수 있게 한다
            play_mode.boy.handle_event(event)


def pause(): pass
def resume(): pass
