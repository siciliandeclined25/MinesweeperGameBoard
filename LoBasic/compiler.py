class LoBasicCompiler:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.errors = []
        self.table = [
            ["print string", {"bytes": [0x01], "operands": 20, "type": "string"}],#simple 20 character string
            ["print var", {"bytes": [0x02], "operands": 2, "type": "reference"}],#can be so cheap because of serial print reference
            ["var number", {"bytes": [0x10], "operands": 5, "type": "int32 reference"}], #reference bit + 32 bit signed integer
            ["var string", {"bytes": [0x11], "operands": 21, "type": "string reference"}], #reference bit + 20 character ascii string
            ["var array", {"bytes": [0x12], "operands": 2, "type": "array reference"}], #reference bit + 1 byte unsigned positive integer 0-255
            ["var pin", {"bytes": [0x12], "operands": 2, "type": "pinaddr reference"}], #reference bit + 1 byte pin reference
        ]

    def compile(self):
        """given the code initialized in the constructor for the class return a byte array
        with operator codes and converted formatted data"""
        codeNearlyFormatted = self.code.strip().replace("\n", "").split(";")
        codeFormatted = []
        print(codeNearlyFormatted)
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
                    #at the end, increment the memory location by the program counter memory
                    programCounterRepresenter += instructNamespace[1]["operands"]
                    input(programCounterRepresenter)
        return bytesToWrite
    def compileTo(self, file="program.b"):
        open(file, "wb").write(bytes(self.compile()))
fileToConvert = "hey.lbas"
lo = LoBasicCompiler(code=open(fileToConvert, "r").read())
print(lo.compileTo())
