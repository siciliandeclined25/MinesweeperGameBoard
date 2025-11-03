
int clockPin = 2;
int dataPin = 3;

bool clockState = false;

const int numInputPins = 16; 
int inputPins[numInputPins] = { 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, };

int waitTime = 50;

void setup() {
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT); 

  for (int inputPin : inputPins) {
    pinMode(inputPin, INPUT);
  }
}

void changeClockState() {
  clockState = !clockState; // Alternate clock
  digitalWrite(clockPin, clockState ? HIGH : LOW); // Update new clock
}

void loop() {
  unsigned long long output = 0; // 16 * 4 bytes each, long is 64, essentially a buffer
  
  // First in last out, so check and insert in reverse order
  for (int i = numInputPins - 1; i >= 1; i--) {
    if (digitalRead(inputPins[i]) == HIGH) {
      output <<= 4; // Shift 4 bits
      output |= i; // Add index bits
    }
  }

  // Zero pin's bytes alone will not show up if not explicitly set
  bool zeroPinActive = false; 
  if (digitalRead(inputPins[0]) == HIGH) {
    zeroPinActive = true;
    output <<= 4; // Shift 4 bits
  }

  // Early exit if no input
  if (output == 0 && !zeroPinActive) {
    delay(waitTime);
    return;
  }
  
  while (output != 0 || zeroPinActive) {
    if (zeroPinActive) zeroPinActive = false;

    digitalWrite(dataPin, HIGH); // Header for each nibble
    changeClockState();
    delay(waitTime);

    // Process nibble(4 bits reversed)
    for (int i = 3; i >= 0; i--) {
      bool currentBit = (output & (1 << i)); // Get i in nibble
      digitalWrite(dataPin, currentBit ? HIGH : LOW); // Write data
      changeClockState();

      delay(waitTime);
    }
    output >>= 4; // Next nibble
  }

  digitalWrite(dataPin, LOW); // Set next header to false
  changeClockState();
  delay(waitTime);
}
