from machine import Pin
import time

clockPin = Pin(1, Pin.IN);
inputPin = Pin(2, Pin.IN);

def readNBit(N=4):
    buttonValue = 0;
    for i in range(N):
        while clockPin.value() == 0:
            time.sleep(0.00001);
        
        buttonValue = (buttonValue << 1) | inputPin.value();

        while clockPin.value() == 1:
            time.sleep(0.00001);
    
    return buttonValue & 0xF;

while True:
    buttonPressed = readNBit();
    print("Button value:", buttonPressed, f"({buttonPressed:04b})")