import time
import keyboard
from PIL import ImageGrab


def screenshot():
    # 2023년 3월 30일 오후 10시 20분 30초 > _20230330_102030
    curr_time = time.strftime("_%y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("imge{}.png".format(curr_time))

keyboard.add_hotkey("e", screenshot) # 사용자가 e 키를 누르면 스크린 샷 저장

keyboard.wait("esc") # 사용자가 esc 누를 때 까지 프로그램 수행