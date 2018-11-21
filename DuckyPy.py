class DuckyPy:
    from adafruit_hid.keyboard import Keyboard
    from adafruit_hid.keycode import Keycode
    import time

    kbd = Keyboard()

    def string(self, arg):
        l = list(arg)
        for x in range(0, len(l)):
            if l[x] == "A":
                writeLetterU(Keycode.A)
            if l[x] == "B":
                writeLetterU(Keycode.B)
            if l[x] == "C":
                writeLetterU(Keycode.C)
            if l[x] == "D":
                writeLetterU(Keycode.D)
            if l[x] == "E":
                writeLetterU(Keycode.E)
            if l[x] == "F":
                writeLetterU(Keycode.F)        
            if l[x] == "G":
                writeLetterU(Keycode.G)
            if l[x] == "H":
                writeLetterU(Keycode.H)
            if l[x] == "I":
                writeLetterU(Keycode.I)            
            if l[x] == "J":
                writeLetterU(Keycode.J)            
            if l[x] == "K":
                writeLetterU(Keycode.K)            
            if l[x] == "L":
                writeLetterU(Keycode.L)
            if l[x] == "M":
                writeLetterU(Keycode.M)
            if l[x] == "N":
                writeLetterU(Keycode.N)
            if l[x] == "O":
                writeLetterU(Keycode.O)
            if l[x] == "P":
                writeLetterU(Keycode.P)
            if l[x] == "Q":
                writeLetterU(Keycode.Q)
            if l[x] == "R":
                writeLetter(Keycode.R)
            if l[x] == "S":
                writeLetterU(Keycode.S)
            if l[x] == "T":
                writeLetterU(Keycode.T)
            if l[x] == "U":
                writeLetterU(Keycode.U)
            if l[x] == "V":
                writeLetterU(Keycode.V)
            if l[x] == "W":
                writeLetterU(Keycode.W)
            if l[x] == "X":
                writeLetterU(Keycode.X)
            if l[x] == "Y":
                writeLetterU(Keycode.Z)
            if l[x] == "Z":
                writeLetterU(Keycode.Y)
            if l[x] == "a":
                writeLetter(Keycode.A)
            if l[x] == "b":
                writeLetter(Keycode.B)
            if l[x] == "c":
                writeLetter(Keycode.C)
            if l[x] == "d":
                writeLetter(Keycode.D)
            if l[x] == "e":
                writeLetter(Keycode.E)
            if l[x] == "f":
                writeLetter(Keycode.F)        
            if l[x] == "g":
                writeLetter(Keycode.G)
            if l[x] == "h":
                writeLetter(Keycode.H)
            if l[x] == "i":
                writeLetter(Keycode.I)            
            if l[x] == "j":
                writeLetter(Keycode.J)            
            if l[x] == "k":
                writeLetter(Keycode.K)            
            if l[x] == "l":
                writeLetter(Keycode.L)
            if l[x] == "m":
                writeLetter(Keycode.M)
            if l[x] == "n":
                writeLetter(Keycode.N)
            if l[x] == "o":
                writeLetter(Keycode.O)
            if l[x] == "p":
                writeLetter(Keycode.P)
            if l[x] == "q":
                writeLetter(Keycode.Q)
            if l[x] == "r":
                writeLetter(Keycode.R)
            if l[x] == "s":
                writeLetter(Keycode.S)
            if l[x] == "t":
                writeLetter(Keycode.T)
            if l[x] == "u":
                writeLetter(Keycode.U)
            if l[x] == "v":
                writeLetter(Keycode.V)
            if l[x] == "w":
                writeLetter(Keycode.w)
            if l[x] == "x":
                writeLetter(Keycode.X)
            if l[x] == "y":
                writeLetter(Keycode.Z)
            if l[x] == "z":
                writeLetter(Keycode.Y)
            if l[x] == " ":
                writeLetter(Keycode.SPACE)
            if l[x] == ".":
                writeLetter(Keycode.PERIOD)
            if l[x] == ":":
                writeLetterU(Keycode.PERIOD)
            if l[x] == ";":
                writeLetterU(Keycode.COMMA)
            if l[x] == ",":
                writeLetter(Keycode.COMMA)
            if l[x] == "/":
                writeLetterU(Keycode.SEVEN) 
            if l[x] == "?":
                writeLetterU(Keycode.MINUS) 
            if l[x] == "-":
                writeLetter(Keycode.FORWARD_SLASH)
            if l[x] == "_":
                writeLetterU(Keycode.FORWARD_SLASH)
            if l[x] == "(":
                writeLetterU(Keycode.EIGHT)
            if l[x] == ")":
                writeLetterU(Keycode.NINE)
            if l[x] == "=":
                writeLetterU(Keycode.ZERO)  
            if l[x] == "[":
                writeLetter(Keycode.RIGHT_ALT, Keycode.EIGHT)
            if l[x] == "]":
                writeLetter(Keycode.RIGHT_ALT, Keycode.NINE)
            if l[x] == "1":
                writeLetter(Keycode.ONE)
            if l[x] == "2":
                writeLetter(Keycode.TWO)
            if l[x] == "3":
                writeLetter(Keycode.THREE)
            if l[x] == "4":
                writeLetter(Keycode.FOUR)
            if l[x] == "5":
                writeLetter(Keycode.FIVE)
            if l[x] == "6":
                writeLetter(Keycode.SIX)
            if l[x] == "7":
                writeLetter(Keycode.SEVEN)
            if l[x] == "8":
                writeLetter(Keycode.EIGHT)
            if l[x] == "9":
                writeLetter(Keycode.NINE)
            if l[x] == "0":
                writeLetter(Keycode.ZERO)

    def writeLetter(self, arg):
        kbd.send(arg)

    def writeLetterU(self, arg):
        kbd.send(Keycode.SHIFT, arg)

    def desktop(self):
        kbd.send(Keycode.GUI, Keycode.D)

    def closeApp(self):
        kbd.send(Keycode.ALT, Keycode.F4)

    def windows(self):
        kbd.send(Keycode.GUI)

    def winR(self):
        kbd.send(Keycode.GUI, Keycode.R)

    def escape(self):
        kbd.send(Keycode.ESCAPE)

    def enter(self):
        kbd.send(Keycode.ENTER)

    def ctrl(self):
        kbd.send(Keycode.CONTROL)

    def ctrlI(self, arg):
        kbd.send(Keycode.CONTROL, arg)

    def menu(self):
        kbd.send(Keycode.SHIFT, Keycode.F10)