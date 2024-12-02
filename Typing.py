import keyboard
import time
def thing(text, wait):
    for i in text:
        time.sleep(wait)
        keyboard.write(i)
x=input("Text:")
y=float(input("Wait time between letters:"))
z=int(input("Repeat times:"))
time.sleep(15)
while z>0:
    thing(x,y)
    z=z-1
