from turtle import delay
from unittest import result
import pyautogui as pt
import random
import time 
a = 3
b = 18
class Clicker:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = 0.1
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=.8)  # region=(0, 84, 1277, 793)
            pt.moveTo(position[0] + 15, position[1] + 15, duration=self.speed)
            pt.doubleClick()

        except:
            print('No image found...')
            return 0

class Clicker_xiu:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = 0.001
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=.8)  # region=(0, 84, 1277, 793)
            pt.moveTo(position[0] + 45, position[1] + 90, duration=self.speed)
            pt.doubleClick()

        except:
            print('No image found...')
            return 0


if __name__ == '__main__':
    # Initialises the clicker
    click_tai = Clicker_xiu('images/tai_small.png', speed=0.001)
    click_xiu = Clicker_xiu('images/xiu_small.png', speed=0.001)
    click_money = Clicker('images/call_1k.png', speed=0.001)
    click_ok = Clicker('images/datcuoc_small.png', speed=0.001)

    total = 0
    shot = 0
    count = 0
    round = 0
    sleep1 = 68
    sleep2 = 58
    while True:
        time_dat = 70
        global current_result
        current_result = " "

        ans = random.randint(3, 18)

        if ans <= 10:
            now_result = "XIU"
        else:
            now_result = "TAI"

        round += 1    
        print("Round: ", round)

        print("DỰ ĐOÁN: ", ans, "==> " + now_result)

        count = 0
        if ans <= 10:
            if shot >= 1:
                print("=====> ĐẶT XỈU")
                time_dat = 65
                if click_xiu.nav_to_image() == 0:
                    count += 1
                
                if click_money.nav_to_image() == 0:
                    count += 1
                
                if click_ok.nav_to_image() == 0:
                    count += 1
        
        else:
            if shot >= 1:
                print("=====> ĐẶT TÀI")
                time_dat = 65
                if click_tai.nav_to_image() == 0:
                    count += 1
                
                if click_money.nav_to_image() == 0:
                    count += 1

                if click_ok.nav_to_image() == 0:
                    count += 1

        
        
        time.sleep(time_dat)

        if pt.pixel(1792, 877)[2] >= 225 and pt.pixel(1792, 877)[2] <= 255:
            current_result = "TAI"
        if pt.pixel(1792, 877)[2] >= 169 and pt.pixel(1792, 877)[2] <= 196:
            current_result = "XIU"

        print("KẾT QUẢ: ", current_result)
        if now_result == current_result:
            shot += 1
            total += 1
            print("===== THẮNG =====")
        else:
            print("===== THUA =====")
            shot = 0
        print("===== TỶ LỆ: " + str(float(total / round) * 100) + "% =====")
        print("~")








        
