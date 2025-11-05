import time

clockPin = 0
inputPin = 0

def readNBit(N=4):
    buttonValue = 0;
    global clockPin
    global inputPin
    previousClockPin = 0;
    clockPin = 0;
    for i in range(N):
        while clockPin == previousClockPin:
            time.sleep(0.00001);
            clockPin = 1 if input("clock input") == "1" else 0
        inputPin = 1 if input("tell me what the input pin is") == "1" else 0
        buttonValue = (buttonValue << 1) | inputPin;
        previousClockPin = clockPin

    return buttonValue & 0xF;

while True:
    buttonPressed = readNBit();
    print("Button value:", buttonPressed, f"({buttonPressed:04b})")