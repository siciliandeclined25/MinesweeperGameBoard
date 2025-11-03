int clockPin = 2;
int dataPin = 3;

const int numInputPins = 16; 
bool clock = false;

int inputPins[numInputPins] = { 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, };

int waitTime = 50;

void setup() {
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT); 

  for (int inputPin : inputPins) {
    pinMode(inputPin, INPUT);
  }
}

void changeClock() {
  clock = !clock; // Alternate clock
  digitalWrite(clockPin, clock ? HIGH : LOW); // Update new clock
}

void loop() {
  unsigned long long output = 0; // 16 * 4 bytes each, long is 64, essentially a buffer
  
  // Bits are read the other way
  for (int i = numInputPins - 1; i >= 1; i--) {
    if (digitalRead(inputPins[i]) == HIGH) {
      output <<= 4; // Shift 4 bits
      output |= i; // Add bytes of index
    }
  }

  // First bytes will not show up if not explicitly set
  bool firstOutput = false; 
  if (digitalRead(inputPins[0]) == HIGH) {
    firstOutput = true;
    output <<= 4; // Shift 4 bits
  }

  // Early exit if no input
  if (output == 0 && !firstOutput) {
    delay(waitTime);
    return;
  }
  
  while (output != 0 || firstOutput) {
    if (firstOutput) firstOutput = false;

    digitalWrite(dataPin, HIGH); // Header for each nibble
    changeClock();
    delay(waitTime);

    // Process nibble(4 bits reversed)
    for (int i = 0; i < 4; i++) {
      digitalWrite(dataPin, (output & (1 << (3 - i))) ? HIGH : LOW); // Write data
      changeClock();

      delay(waitTime);
    }
    output >>= 4; // Next nibble
  }

  digitalWrite(dataPin, LOW); // Set next header to false
  changeClock();
  delay(waitTime);
}
