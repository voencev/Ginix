import machine, os,uos
from machine import Pin,SPI
import sdcard

print("sdcard test...")
# 失败的方式
# Traceback (most recent call last):
#   File "main.py", line 18, in <module>
#   File "sdcard.py", line 54, in __init__
#   File "sdcard.py", line 82, in init_card
# OSError: no SD card
# SD_CS = Pin(5)
# sd = sdcard.SDCard(SPI(2,sck=Pin(17), mosi=Pin(23),miso=Pin(19)), SD_CS)
# # 初始化⽂件系统
# vfs = os.VfsFat(sd)# fat挂载卡到⽬录下
# os.mount(sd,"/sd")# SD/sd
# dirs=os.listdir('/sd')
# print("sdcard test 1...")
# for file in dirs:   
#     print(file)
# print("sdcard test end...")

# 方式二
#失败
sd = machine.SDCard(slot=2, width=1, sck=18, miso=19, mosi=23, cs=5)
print("sdcard test 1...")
uos.mount(sd, "/sd")
print("sdcard test end...")
# 错误消息
# E (2540) sdmmc_sd: sdmmc_init_sd_if_cond: send_if_cond (1) returned 0x108
# Traceback (most recent call last):
#   File "main.py", line 37, in <module>
# OSError: 16

# spixxx = machine.SPI(2, baudrate=10000000, polarity=0, phase=0)
# sd = machine.SDCard(slot=2, width=1, spi=spixxx, cs=5)
# print("sdcard test 1...")
# uos.mount(sd, "/sd")
# print("sdcard test end...")
# 错误消息
# Traceback (most recent call last):
#   File "main.py", line 47, in <module>
# TypeError: extra keyword arguments given

# sd = machine.SDCard(slot=2)
# print("sdcard test 1...")
# os.mount(sd, '/sd') # 挂载 SD 卡到 /sd 目录
# print("sdcard test end...")
#失败错误消息
# E (2530) sdmmc_sd: sdmmc_init_sd_if_cond: send_if_cond (1) returned 0x108
# Traceback (most recent call last):
#   File "main.py", line 58, in <module>
# OSError: 16