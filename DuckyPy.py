class DuckyPy:
    from adafruit_hid.keyboard import Keyboard
    from adafruit_hid.keycode import Keycode
    import time

    kbd = Keyboard()
    
    def getkeycodede(self, arg):
            if arg == "A":
                return self.Keycode.SHIFT, self.Keycode.A;
            if arg == "B":
                return self.Keycode.SHIFT, self.Keycode.B;
            if arg == "C":
                return self.Keycode.SHIFT, self.Keycode.C;
            if arg == "D":
                return self.Keycode.SHIFT, self.Keycode.D;
            if arg == "E":
                return self.Keycode.SHIFT, self.Keycode.E;
            if arg == "F":
                return self.Keycode.SHIFT, self.Keycode.F;        
            if arg == "G":
                return self.Keycode.SHIFT, self.Keycode.G;
            if arg == "H":
                return self.Keycode.SHIFT, self.Keycode.H;
            if arg == "I":
                return self.Keycode.SHIFT, self.Keycode.I;            
            if arg == "J":
                return self.Keycode.SHIFT, self.Keycode.J;            
            if arg == "K":
                return self.Keycode.SHIFT, self.Keycode.K;            
            if arg == "L":
                return self.Keycode.SHIFT, self.Keycode.L;
            if arg == "M":
                return self.Keycode.SHIFT, self.Keycode.M;
            if arg == "N":
                return self.Keycode.SHIFT, self.Keycode.N;
            if arg == "O":
                return self.Keycode.SHIFT, self.Keycode.O;
            if arg == "P":
                return self.Keycode.SHIFT, self.Keycode.P;
            if arg == "Q":
                return self.Keycode.SHIFT, self.Keycode.Q;
            if arg == "R":
                return self.Keycode.SHIFT, self.Keycode.R;
            if arg == "S":
                return self.Keycode.SHIFT, self.Keycode.S;
            if arg == "T":
                return self.Keycode.SHIFT, self.Keycode.T;
            if arg == "U":
                return self.Keycode.SHIFT, self.Keycode.U;
            if arg == "V":
                return self.Keycode.SHIFT, self.Keycode.V;
            if arg == "W":
                return self.Keycode.SHIFT, self.Keycode.W;
            if arg == "X":
                return self.Keycode.SHIFT, self.Keycode.X;
            if arg == "Y":
                return self.Keycode.SHIFT, self.Keycode.Z;
            if arg == "Z":
                return self.Keycode.SHIFT, self.Keycode.Y;
            if arg == "a":
                return self.Keycode.A;
            if arg == "b":
                return self.Keycode.B;
            if arg == "c":
                return self.Keycode.C;
            if arg == "d":
                return self.Keycode.D;
            if arg == "e":
                return self.Keycode.E;
            if arg == "f":
                return self.Keycode.F;        
            if arg == "g":
                return self.Keycode.G;
            if arg == "h":
                return self.Keycode.H;
            if arg == "i":
                return self.Keycode.I;            
            if arg == "j":
                return self.Keycode.J;            
            if arg == "k":
                return self.Keycode.K;            
            if arg == "l":
                return self.Keycode.L;
            if arg == "m":
                return self.Keycode.M;
            if arg == "n":
                return self.Keycode.N;
            if arg == "o":
                return self.Keycode.O;
            if arg == "p":
                return self.Keycode.P;
            if arg == "q":
                return self.Keycode.Q;
            if arg == "r":
                return self.Keycode.R;
            if arg == "s":
                return self.Keycode.S;
            if arg == "t":
                return self.Keycode.T;
            if arg == "u":
                return self.Keycode.U;
            if arg == "v":
                return self.Keycode.V;
            if arg == "w":
                return self.Keycode.W;
            if arg == "x":
                return self.Keycode.X;
            if arg == "y":
                return self.Keycode.Z;
            if arg == "z":
                return self.Keycode.Y;
            if arg == " ":
                return self.Keycode.SPACE;
            if arg == ".":
                return self.Keycode.PERIOD;
            if arg == ":":
                return self.Keycode.SHIFT, self.Keycode.PERIOD;
            if arg == ";":
                return self.Keycode.SHIFT, self.Keycode.COMMA;
            if arg == ",":
                return self.Keycode.COMMA;
            if arg == "/":
                return self.Keycode.SHIFT, self.Keycode.SEVEN;
            if arg == "\\":
                return self.Keycode.RIGHT_ALT, self.Keycode.MINUS; 
            if arg == "?":
                return self.Keycode.SHIFT, self.Keycode.MINUS; 
            if arg == "-":
                return self.Keycode.FORWARD_SLASH;
            if arg == "_":
                return self.Keycode.SHIFT, self.Keycode.FORWARD_SLASH;
            if arg == "(":
                return self.Keycode.SHIFT, self.Keycode.EIGHT;
            if arg == ";":
                return self.Keycode.SHIFT, self.Keycode.NINE;
            if arg == "=":
                return self.Keycode.SHIFT, self.Keycode.ZERO;  
            if arg == "[":
                return self.Keycode.RIGHT_ALT, self.Keycode.EIGHT;
            if arg == "]":
                return self.Keycode.RIGHT_ALT, self.Keycode.NINE;
            if arg == "@":
                return self.Keycode.SHIFT, self.Keycode.TWO;
            if arg == "%":
                return self.Keycode.SHIFT, self.Keycode.FIVE;
            if arg == "1":
                return self.Keycode.ONE;
            if arg == "2":
                return self.Keycode.TWO;
            if arg == "3":
                return self.Keycode.THREE;
            if arg == "4":
                return self.Keycode.FOUR;
            if arg == "5":
                return self.Keycode.FIVE;
            if arg == "6":
                return self.Keycode.SIX;
            if arg == "7":
                return self.Keycode.SEVEN;
            if arg == "8":
                return self.Keycode.EIGHT;
            if arg == "9":
                return self.Keycode.NINE;
            if arg == "0":
                return self.Keycode.ZERO;
    
    def writeOneOrMultiple(self, arg):
        if isinstance(arg, int):
            self.kbd.send(arg)
        elif len(arg) == 2:
            self.kbd.send(arg[0], arg[1])
        elif len(arg) == 3:
            self.kbd.send(arg[0], arg[1], arg[2])
    
    def string(self, arg):
        le = list(arg)
        for x in range(0, len(le)):
            ler = self.getkeycodede(le[x])
            self.writeOneOrMultiple(ler)

    def desktop(self):
        self.kbd.send(self.Keycode.GUI, self.Keycode.D)

    def closeApp(self):
        self.kbd.send(self.Keycode.ALT, self.Keycode.F4)

    def windows(self):
        self.kbd.send(self.Keycode.GUI)

    def winR(self):
        self.kbd.send(self.Keycode.GUI, self.Keycode.R)

    def escape(self):
        self.kbd.send(self.Keycode.ESCAPE)

    def enter(self):
        self.kbd.send(self.Keycode.ENTER)

    def ctrl(self):
        self.kbd.send(self.Keycode.CONTROL)

    def ctrlI(self, arg):
        self.kbd.send(self.Keycode.CONTROL, arg)
        
    def cmd(self):
        self.winR()
        self.time.sleep(0.3)
        self.string("cmd.exe")
        self.enter()
    
    def menu(self):
        self.kbd.send(self.Keycode.SHIFT, self.Keycode.F10)