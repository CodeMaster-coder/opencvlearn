import RPi.GPIO as GPIO  ##引入GPIO模块
import time  ##引入time库
from picamera import PiCamera
from detect import detect

print('准备开始接收')

i = 0

while True:
    print('等待')
    inpositionPin = 7  # 车辆到位信号输入针脚
    receivePin = 11  # 收到信号反馈输出针脚
    detectpin = 13  # 检测到发泡件信号输出针脚
    notDetectPin = 15  # 未检测到发泡件信号输出针脚

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(inpositionPin, GPIO.IN)
    GPIO.setup(receivePin, GPIO.OUT)
    if GPIO.input(inpositionPin) == GPIO.HIGH:
        print('发现低电压变化高电压')
        GPIO.output(receivePin, GPIO.HIGH)

        sig = detect('/home/pi/visiondetect/image/image%s.jpg' % a)
        print(sig)
        if sig == False:
            print('yes')
        else:
            print('no')
        time.sleep(5)
        #         GPIO.output(receivePin, GPIO.LOW)
        i = a
        GPIO.cleanup()
    time.sleep(3)








