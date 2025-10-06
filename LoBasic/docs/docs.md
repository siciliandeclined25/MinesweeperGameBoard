## Getting Started

To get started with LoBASIC, follow these steps:
1. Install the Arduino IDE.
2. Download the LoBASIC library.
3. Create a new Arduino sketch.
4. Import the lobasic.h file
5. Convert an LBAS program with compiler.py
6. Add the compilied version to the SD card

**Why compile a BASIC inspired language?**
THe implicit problem with writing on an Arduino Uno is size. This language attempts to be the most well verbose tiny language for the Uno/Nano (2 KB of SRAM).

Here's an example of a simple LoBASIC program that displays "hello" on the serial monitor endlessly:

```
start:
    print "hello"
    goto start
```

This program emphasises a few important syntax elments.
* simple one word keywords
* defined labels that can be referenced for branching and looping
* support for strings and other data types

LoBasic is a REPL language, meaning that there is no compile time, but that instructions are read each line.

KEYWORDS:

**print**
 - displays (through the serial monitor) an outputted string (5 bytes) does not support multiple types
 - USAGE: print string (string), print var (string), (int)
 - EXAMPLE:
 ```
 print string "hello"
 print var string1
 ```

**comments**
- comments can be placed only on newlines with # to signify their identity
```
print "harold is a dog";
#harold is my pet dog;
print "i like him";
```
**var**
 - declares a variable and it's value within the program (note that the variable will exist predefinition but will be defined as its initial value.)
 - four types of variables can be accessed
  - 32 bit signed integers (a-z). defined as var a = 10;
  - 10 strings with 20 character support. defined as var string1 = "hello";
  - 1 array of 256 1 byte unsigned positive integers. defined as var array[10] = 125; (note, iterating loops can be accessed by using the keyword for x,y in array)
  - all pins on the board. takes boolean true/false value. defined as var p3 = true;
```
var number a  = 10;
var string string1 = "hello";
var array 10 = 125;
var pin 3 = true;
```
**evar**
- declares a value into the EEPROM of the Arduino (1 bit int only)
- can be accessed/declared later
```
evar 1 = 10;
#this is stored at 1 of the memory;
```
**int -- ++**
- lobasic supports ++ and -- operators such as C++ and C that deincrement or reincrement the value
- an added syntaxical benefit is the by operator will make it de/increment the increment value
```
var a = 10;
--a;
#a = 9 now;
--a by 2;
# a = 7;
++a;
# a = 8;
++a by 5;
# a = 13;
```

**if then blocks**
- logic is built through if then blocks.
- if the boolean statement is true the next line will be executed up until the end block
- if not, execution will resume after the end block
- takes one boolean expression
- boolean expression is compared to a value.
- example (if P10 is true) would check for a high connection in P10
- special mode allowed for variables to consider < or > values using greater than or less than keywords
```
if a is 5 then;
    print "a is 5";
end;
if a is greater than 5 then;
    print "a is greater than 5";
end;
```

**else**
- at the end of an end statement, if the previous boolean statement evaluated as false, then the else block is true
- else block is then executed up until end then returns back
- otherwise, the pointer jump to the next line after referenced
```
if P10 is true then;
    print "P10 is high";
end;
else;
    print "P10 is low";
end;
```
**terminate**
- ends the program
- serial monitor will notify when this block is hit
'''
print "code is over"
terminate
'''
**goto**
- goto switches the program counter to a new place in the program.
- labels are defined by a 5 char string with a colon (:) at the end (ex, start:)
- labels are indexed before runtime. if you reference an unbound label, the program counter will not jump.
- labels are just pointers. the code inside labels will be run if the program counter encounters them. recommended practice is to put labels near the end of your program.
```
start:
var x = 0;
var y = 1;
var a = 10;
print "let's calc fib numbers"
--a;
if a == 0 then;
    goto last;
end;
else;
    goto calc;

calc:
var s = x + y; #our sum
var x = y;
var y = s;
goto start;

last:
print "done";
```
**return**
- alternatively, the program counter will store the last jumped point.
- this does *not* stack. that mean that if you have two labels, you cannot return to the original program loop using two return blocks, as it will return to the previous time goto was used.
```
print "reseting screen"
goto reset
print "done!"
terminate
reset:
var P10 = true;
return
```
## Libraries
 > The proceeding documentation is specifically for the graphics module made for KU IEEE '26's Minesweeper and the graphical libraries that are used. This is used to plug into a TFT touchsreen with a particular setup. Usage of this is not advised outside of the scope of the project. Write your own compatible libraries
# g
This library provides basic graphical output with a TFT screen, as well as defining functions

**gdraw**
- draws a preprogrammed image at the location of x, y defined in LoBasic
- images are defined by a 8 bit value (00000000) that output one of 256 images.
```
var x = 10;
var y = 75;
gdraw 01010010;
#draws a smiley face (preprogrammed)
```

**gtext**
- displays a string at the location of x, y defined in LoBasic
- strings have the same length requirement
```
var string1 = "hello world";
gtext string1;
#uses same x, y;
```

**gcolor**
- sets the color of the next drawn object
- color is defined by a byte value (00000000) that output one of 256 colors.
- bytes 7, 8 are red
- bytes 5, 6 are green
- bytes 3, 4 are blue
- bytes 2, 1 are transparency

```
var x = 10;
var y = 75;
gcolor 01010010;
gdraw 01010010;
#draws a smiley face (with the color value rgba(128, 128, 0, 192))
```
**gc (variable)**
- enables or disables whether the gcolor is on
```
gc true;
gc false;
```

**gfill**
- fills the screen with a color based on the byte values discussed in colors
```
gc = true;
gcolor = 11000011;
gfill;
#the screen is now red with no transparency;
```
**gprint**
- prints a string at the location of x, y defined in LoBasic
- strings have the same length requirement
```
var string1 = "hello world";
gtext string1;
#uses same x, y;
```
# b
b is a library that accesses and reads the button values given the board.

**bdo**
- defines a label that is jumped to when the button is pressed, skipping the instruction currently.
```
bdo1 hello;
#this next code will say no endlessly until the button is pressed
loop:
print "no";
goto loop;
hello:
print "yes";
terminate;
#end the program and stop the loop;
```

**bcheck**
- checks to see if the button is pressed
- replaces a certain value with a true or false value
- numbered for each button 1-x
```
if bcheck1 is true then;
print "button pressed";
end;
```
