import struct

class LoBasicCompiler:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.errors = []
        #table of all operators, the operands the amount of bytes they cost in storage, and the type
        # being the type of data they strore
        self.table = [
            ["print string", {"bytes": [0x01], "operands": 20, "type": "string"}],#simple 20 character string
            ["print var", {"bytes": [0x02], "operands": 2, "type": "reference"}],#can be so cheap because of serial print reference
            ["var number", {"bytes": [0x10], "operands": 5, "type": "int32 with reference"}], #reference bit + 32 bit signed integer
            ["var string", {"bytes": [0x11], "operands": 21, "type": "string reference"}], #reference bit + 20 character ascii string
            ["var array", {"bytes": [0x12], "operands": 2, "type": "array reference"}], #reference bit + 1 byte unsigned positive integer 0-255
            ["var pin", {"bytes": [0x12], "operands": 2, "type": "pinaddr reference"}], #reference bit + 1 byte pin reference
        ]
        self.referenceTable = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19,
            "u": 20,
            "v": 21,
            "w": 22,
            "x": 23,
            "y": 24,
            "z": 25,
            "string1": 26,
            "string2": 27,
            "string3": 28,
            "string4": 29,
            "string5": 30,
            "string6": 31,
            "string7": 32,
            "string8": 33,
            "string9": 34,
            "string10": 35,
            "A0": 36,
            "A1": 37,
            "A2": 38,
            "A3": 39,
            "A4": 40,
            "A5": 41,
            "D1": 42,
            "D2": 43,
            "D5": 44,
            "D6": 45,
            "D7": 46,
            "D8": 47,
            "D9": 48,
            "D10": 49,
            "D11": 50,
            "D12": 51,
            "array1": 52, #the rest of the array follows from here
        }
    def compile(self):
        """given the code initialized in the constructor for the class return a byte array
        with operator codes and converted formatted data"""
        codeNearlyFormatted = self.code.strip().replace("\n", "").split(";")
        codeFormatted = []
        for instruction in codeNearlyFormatted:
            if len(instruction) == 0:
                continue #ignores empty lines
            if instruction[0] != "#": #remove all comments
                codeFormatted.append(instruction)
        #final conversion here
        bytesToWrite = []
        #for each command (namepsace of instruction + value)
        # this is the mainloop where we go through every instruction
        # and find the opcode and bytes that it requires
        programCounterRepresenter = 0
        for instruction in codeFormatted:
            #for eahc instruction (opcode)
            for instructNamespace in self.table:
                #if namespace matches the given verbose namepsace
                if instructNamespace[0] in instruction:
                    bytesToWrite.append(instructNamespace[1]["bytes"][0]) #append namespace
                    #make a string representing the values
                    instructionData = instruction.split(instructNamespace[0])[1] #get the data in string
                    if instructNamespace[1]["type"] == "string":
                        #convert the instruction to a bunch
                        # of 8 bit chars (max len 20)
                        #rewrite instructionData to remove
                        # excess string info
                        instructionData = instructionData.strip().strip("\"")
                        maxLength = 20
                        instructionData = instructionData[:maxLength]
                        for char in instructionData:
                            bytesToWrite.append(ord(char))
                    if instructNamespace[1]["type"] == "int32 with reference":
                            #set to a 32 bit integer
                            instructionNumber = int(instructionData.split("=")[1])
                            #there is one reference byte before the big endian integer.
                            # this statement here converts the instruction reference to bytes
                            # so that it can be recalled. 00 is a, 25 is z
                            alphabetToReferenceNumber = lambda c: ord(c) - ord('a')
                            bytesToWrite.append(alphabetToReferenceNumber(instructionData.split("=")[0].replace("=", "").strip()))
                            #now that we have it as an integer, place it in big endian
                            # order (most significant byte first)
                            bytesToWrite.append((instructionNumber >> 24) & 0xFF)
                            bytesToWrite.append((instructionNumber >> 16) & 0xFF)
                            bytesToWrite.append((instructionNumber >> 8) & 0xFF)
                            bytesToWrite.append(instructionNumber & 0xFF)
                    #at the end, increment the memory location by the program counter memory
                    programCounterRepresenter += instructNamespace[1]["operands"]
                    print(bytesToWrite)
        return bytesToWrite
    def compileTo(self, file="program.b"):
        open(file, "wb").write(bytes(self.compile()))
fileToConvert = "hey.lbas"
lo = LoBasicCompiler(code=open(fileToConvert, "r").read())
lo.compileTo()
