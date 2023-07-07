import helper
import npCar
from settings import *
from npCar import *
from speedManager import *

class carManager:
    def __init__(self):
        self.alive = True
        self.car_list = []
        self.timer = 0
        self.SM = speedMan()
        self.car_rows = [False, False, False, False]
        self.pos_list = [
            SCREEN_WIDTH * 5 / 123 + (SCREEN_WIDTH * 28 / 123 - CAR1_WIDTH) / 2 + 0 * SCREEN_WIDTH * 28 / 123,
            SCREEN_WIDTH * 5 / 123 + (SCREEN_WIDTH * 28 / 123 - CAR1_WIDTH) / 2 + 1 * SCREEN_WIDTH * 28 / 123,
            SCREEN_WIDTH * 5 / 123 + (SCREEN_WIDTH * 28 / 123 - CAR1_WIDTH) / 2 + 2 * SCREEN_WIDTH * 28 / 123,
            SCREEN_WIDTH * 5 / 123 + (SCREEN_WIDTH * 28 / 123 - CAR1_WIDTH) / 2 + 3 * SCREEN_WIDTH * 28 / 123
        ]

    def update(self):

        # delete objects
        for i in reversed(range(len(self.car_list))):
            if self.car_list[i].y > SCREEN_HEIGHT:
                car_pos = self.car_list[i].x
                del self.car_list[i]

                for i in range(len(self.pos_list)):
                    if car_pos == self.pos_list[i]:
                        self.car_rows[i] = False


        # insert objects
        C = npCar.car()
        probability = random.randint(0, 120)
        if probability == 0:
            pos = random.randint(0, 3)
            for i in range(3):
                if self.car_rows[pos] == False:
                    self.car_list.append(C)
                    C.x = self.pos_list[pos]
                    C.y = -CAR1_HEIGHT
                    self.car_rows[pos] = True
                    if pos == 1 or pos == 0:
                        C.angle = C.angle + 180
                        C.Vy = 2*C.Vy + self.SM.getSpeed()/2
                    break
                else:
                    pos = pos - 1

        for car in self.car_list:
            car.update()

    def render(self,window):
        for car in self.car_list:
            car.render(window)

    def collision_check(self,player):

        for car in self.car_list:
            F, B, L, R = helper.check_collision2(player,car,x_buffer=12)

            if F:
                print("DIED")
                exit(0)
            if B:
                player.Vy = -player.Vy + car.Vy
            if L:
                player.Vx = -player.Vx + car.Vx
            if R:
                player.Vx = -player.Vx + car.Vx

