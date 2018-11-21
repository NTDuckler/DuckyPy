class DuckyPy:
    from adafruit_hid.keyboard import Keyboard
    from adafruit_hid.keycode import Keycode
    import time

    kbd = Keyboard()

    def string(self, arg):
        l = list(arg)
        for x in range(0, len(l)):
            if l[x] == "A":
                self.writeLetterU(self.Keycode.A)
            if l[x] == "B":
                self.writeLetterU(self.Keycode.B)
            if l[x] == "C":
                self.writeLetterU(self.Keycode.C)
            if l[x] == "D":
                self.writeLetterU(self.Keycode.D)
            if l[x] == "E":
                self.writeLetterU(self.Keycode.E)
            if l[x] == "F":
                self.writeLetterU(self.Keycode.F)        
            if l[x] == "G":
                self.writeLetterU(self.Keycode.G)
            if l[x] == "H":
                self.writeLetterU(self.Keycode.H)
            if l[x] == "I":
                self.writeLetterU(self.Keycode.I)            
            if l[x] == "J":
                self.writeLetterU(self.Keycode.J)            
            if l[x] == "K":
                self.writeLetterU(self.Keycode.K)            
            if l[x] == "L":
                self.writeLetterU(self.Keycode.L)
            if l[x] == "M":
                self.writeLetterU(self.Keycode.M)
            if l[x] == "N":
                self.writeLetterU(self.Keycode.N)
            if l[x] == "O":
                self.writeLetterU(self.Keycode.O)
            if l[x] == "P":
                self.writeLetterU(self.Keycode.P)
            if l[x] == "Q":
                self.writeLetterU(self.Keycode.Q)
            if l[x] == "R":
                self.writeLetterU(self.Keycode.R)
            if l[x] == "S":
                self.writeLetterU(self.Keycode.S)
            if l[x] == "T":
                self.writeLetterU(self.Keycode.T)
            if l[x] == "U":
                self.writeLetterU(self.Keycode.U)
            if l[x] == "V":
                self.writeLetterU(self.Keycode.V)
            if l[x] == "W":
                self.writeLetterU(self.Keycode.W)
            if l[x] == "X":
                self.writeLetterU(self.Keycode.X)
            if l[x] == "Y":
                self.writeLetterU(self.Keycode.Z)
            if l[x] == "Z":
                self.writeLetterU(self.Keycode.Y)
            if l[x] == "a":
                self.writeLetter(self.Keycode.A)
            if l[x] == "b":
                self.writeLetter(self.Keycode.B)
            if l[x] == "c":
                self.writeLetter(self.Keycode.C)
            if l[x] == "d":
                self.writeLetter(self.Keycode.D)
            if l[x] == "e":
                self.writeLetter(self.Keycode.E)
            if l[x] == "f":
                self.writeLetter(self.Keycode.F)        
            if l[x] == "g":
                self.writeLetter(self.Keycode.G)
            if l[x] == "h":
                self.writeLetter(self.Keycode.H)
            if l[x] == "i":
                self.writeLetter(self.Keycode.I)            
            if l[x] == "j":
                self.writeLetter(self.Keycode.J)            
            if l[x] == "k":
                self.writeLetter(self.Keycode.K)            
            if l[x] == "l":
                self.writeLetter(self.Keycode.L)
            if l[x] == "m":
                self.writeLetter(self.Keycode.M)
            if l[x] == "n":
                self.writeLetter(self.Keycode.N)
            if l[x] == "o":
                self.writeLetter(self.Keycode.O)
            if l[x] == "p":
                self.writeLetter(self.Keycode.P)
            if l[x] == "q":
                self.writeLetter(self.Keycode.Q)
            if l[x] == "r":
                self.writeLetter(self.Keycode.R)
            if l[x] == "s":
                self.writeLetter(self.Keycode.S)
            if l[x] == "t":
                self.writeLetter(self.Keycode.T)
            if l[x] == "u":
                self.writeLetter(self.Keycode.U)
            if l[x] == "v":
                self.writeLetter(self.Keycode.V)
            if l[x] == "w":
                self.writeLetter(self.Keycode.w)
            if l[x] == "x":
                self.writeLetter(self.Keycode.X)
            if l[x] == "y":
                self.writeLetter(self.Keycode.Z)
            if l[x] == "z":
                self.writeLetter(self.Keycode.Y)
            if l[x] == " ":
                self.writeLetter(self.Keycode.SPACE)
            if l[x] == ".":
                self.writeLetter(self.Keycode.PERIOD)
            if l[x] == ":":
                self.writeLetterU(self.Keycode.PERIOD)
            if l[x] == ";":
                self.writeLetterU(self.Keycode.COMMA)
            if l[x] == ",":
                self.writeLetter(self.Keycode.COMMA)
            if l[x] == "/":
                self.writeLetterU(self.Keycode.SEVEN) 
            if l[x] == "?":
                self.writeLetterU(self.Keycode.MINUS) 
            if l[x] == "-":
                self.writeLetter(self.Keycode.FORWARD_SLASH)
            if l[x] == "_":
                self.writeLetterU(self.Keycode.FORWARD_SLASH)
            if l[x] == "(":
                self.writeLetterU(self.Keycode.EIGHT)
            if l[x] == ")":
                self.writeLetterU(self.Keycode.NINE)
            if l[x] == "=":
                self.writeLetterU(self.Keycode.ZERO)  
            if l[x] == "[":
                self.writeLetter(self.Keycode.RIGHT_ALT, self.Keycode.EIGHT)
            if l[x] == "]":
                self.writeLetter(self.Keycode.RIGHT_ALT, self.Keycode.NINE)
            if l[x] == "1":
                self.writeLetter(self.Keycode.ONE)
            if l[x] == "2":
                self.writeLetter(self.Keycode.TWO)
            if l[x] == "3":
                self.writeLetter(self.Keycode.THREE)
            if l[x] == "4":
                self.writeLetter(self.Keycode.FOUR)
            if l[x] == "5":
                self.writeLetter(self.Keycode.FIVE)
            if l[x] == "6":
                self.writeLetter(self.Keycode.SIX)
            if l[x] == "7":
                self.writeLetter(self.Keycode.SEVEN)
            if l[x] == "8":
                self.writeLetter(self.Keycode.EIGHT)
            if l[x] == "9":
                self.writeLetter(self.Keycode.NINE)
            if l[x] == "0":
                self.writeLetter(self.Keycode.ZERO)

    def writeLetter(self, arg):
        self.kbd.send(arg)

    def writeLetterU(self, arg):
        self.kbd.send(self.Keycode.SHIFT, arg)

    def desktop(self):
        self.kbd.send(self.Keycode.GUI, Keycode.D)

    def closeApp(self):
        self.kbd.send(self.Keycode.ALT, Keycode.F4)

    def windows(self):
        self.kbd.send(self.Keycode.GUI)

    def winR(self):
        self.kbd.send(self.Keycode.GUI, Keycode.R)

    def escape(self):
        self.kbd.send(self.Keycode.ESCAPE)

    def enter(self):
        self.kbd.send(self.Keycode.ENTER)

    def ctrl(self):
        self.kbd.send(self.Keycode.CONTROL)

    def ctrlI(self, arg):
        self.kbd.send(self.Keycode.CONTROL, arg)

    def menu(self):
        self.kbd.send(self.Keycode.SHIFT, self.Keycode.F10)