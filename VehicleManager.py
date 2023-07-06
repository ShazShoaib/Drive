import helper
import npCar
from settings import *
from npCar import *

class carManager:
    def __init__(self):
        self.alive = True
        self.car_list = []
        self.timer = 0
        self.car_rows = [False, False, False, False]
        C = car()
        self.car_list.append(C)
        C.x = SCREEN_WIDTH*5/123 + (SCREEN_WIDTH*28/123 - CAR1_WIDTH)/2
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
                        C.Vy = 4*C.Vy
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
            if helper.collide_check(player,car):
                print("DIED")
                exit(0)
        #    F,B,L,R = helper.collide_check(player,car)
        #    print(F,B,L,R)
        #    if F:
        #        player.y = car.y+car.h
        #    if B:
        #        player.y = car.y - player.h
