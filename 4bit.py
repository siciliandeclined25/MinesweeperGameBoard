from gpiozero import DigitalInputDevice
import time

clockPin:DigitalInputDevice = DigitalInputDevice(10)
inputPin:DigitalInputDevice = DigitalInputDevice(11)

clockDelay:float = 0.00001

def readNBit(N=4):
    buttonValue:int = 0;
    previousClockPinValue:int = 0;
    for i in range(N):
        while clockPin.value == previousClockPinValue:
            time.sleep(clockDelay);
        
        buttonValue = (buttonValue << 1) | inputPin.value();
        previousClockPinValue = clockPin.value
    
    return buttonValue & 0xF;

while True:
    buttonPressed:int = readNBit();
    print("Button value:", buttonPressed, f"({buttonPressed:04b})")