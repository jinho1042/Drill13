from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None
    image_file = 'ball21x21.png'

    def __init__(self, x, y, velocity):
        # 이미지는 클래스마다 한 번만 로드해서 공유한다
        if type(self).image is None:
            type(self).image = load_image(self.image_file)
        self.x, self.y = x, y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity
        # 화면 밖으로 나가면 월드에서 제거
        if self.x < -50 or self.x > get_canvas_width() + 50:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)


class SmallBall(Ball):
    image = None
    image_file = 'ball21x21.png'


class BigBall(Ball):
    image = None
    image_file = 'ball41x41.png'
