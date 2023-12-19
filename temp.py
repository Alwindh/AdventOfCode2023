import pyautogui as pag
import random
import time

clicks = 16
timer = 10

print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")

time.sleep(1)
for i in range(clicks):
    pag.click()
    time.sleep(timer + 1)
    time.sleep(random.uniform(0.1, 2.1))

print("done")
