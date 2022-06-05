import time
Loop = 1

# LIST
# 1. 'find the 2nd grade point avrg' program
# 2. 'hystogram ! ' program
# 3. 'Multiplication table' program
# 4. 'Salary and avr salary' program
# 5. 'jenas galb' program
# 6. 'Upside down !' program
# 7. '|Abs| ghadr motlag' program
# 8. 'Name into ascii code' program
# 9. '→0936.txt← create irancell number' program
# 10. 'conver asci code to chr and vice versa!' program


class final:
    def __init__(self):  # chose program
        while True:
            try:
                self.MenuNum = input(
                    "hi and welcome please chose the number from 1-10 exercises :  ")
                if self.MenuNum.lower() == "end":
                    self.MenuNum = str(self.MenuNum)
                    print("► Bye ◄")
                    break
                if int(self.MenuNum) not in range(11):
                    raise ValueError
            except:
                print("-"*15)
                print("please Enter a valied number")
                print("-"*15)
            else:
                self.MenuNum = int(self.MenuNum)
                break

    def Ex1(self):
        # decor
        print("▬"*15)
        for i in range(3, 0, -1):
            print(
                f"\rrunning 'find the 2nd grade point avrg (3)' program in → {i} ", end="")
            time.sleep(1)
        else:
            print("\r" + " "*60, end="\r")
        # program
        while True:
            try:
                self.num = input("chand daneshjo ?  ")
                if self.num.lower() == "end":
                    global Loop
                    Loop = 0
                    self.num = 0
                    print("► Bye ◄")
                    break
                int(self.num)
            except:
                print("please enter a valid number :) ")
            else:
                self.num = int(self.num)
                break
        self.BigOne = 0
        self.Big2 = 0
        self.Sh_D1 = 0
        self.Sh_D2 = 0
        while self.num:
            self.num -= 1
            while True:
                try:
                    self.moadel = input("moadel ra vared konid : ")
                    if self.moadel.lower() == "end":
                        Loop = 0
                        print("► Bye ◄")
                        break
                    float(self.moadel)
                except:
                    print("please enter a valid number :) ")
                else:
                    self.moadel = float(self.moadel)
                    break
            if Loop == 0:
                break
            while True:
                try:
                    self.shomare = input("shomare daneshjo ra vared konid : ")
                    if self.shomare.lower() == "end":
                        Loop = 0
                        print("► Bye ◄")
                        break
                    int(self.shomare)
                except:
                    print("please enter a valid number :) ")
                else:
                    self.shomare = int(self.shomare)
                    break
            if Loop == 0:
                break
            if self.moadel > self.BigOne:
                self.Big2 = self.BigOne  # update 2vomin moadel
                self.BigOne = self.moadel  # save bozorg tarin moadel
                self.Sh_D2 = self.Sh_D1  # update sh_d big2
                self.Sh_D1 = self.shomare  # save sh_d bigone
            if self.moadel > self.Big2 and self.moadel < self.BigOne:  # hal bug update nashodam big2
                self.Big2 = self.moadel
                self.Sh_D2 = self.shomare  # update sh_d big2
        if Loop != 0:
            print("-"*15 + "\n" +
                  f"2vomin moadel kelas {self.Big2} e be shomare daneshjoii {self.Sh_D2}" + "\n" + "▬"*15)

    def Ex2(self):
        # decor
        print("▬"*15)
        for i in range(3, 0, -1):
            print(f"\rrunning 'histogram (4)' program in → {i} ", end="")
            time.sleep(1)
        else:
            print("\r" + " "*60, end="\r")
        # program
        self.L1 = [1, 5, 3, 4, 6, 2]
        for i in self.L1:
            try:
                i = int(i)
            except:
                print(f"{i} ← is not a valid number please don't change list :)")
                continue
            print(f"{i} : ", end="")
            while i:
                i -= 1
                print("*", end="")
            print("")
        else:
            print("▬"*15)

    def Ex3(self):
        # decor
        print("▬"*15)
        for i in range(3, 0, -1):
            print(
                f"\rrunning 'Multiplication table (13)' program in → {i} ", end="")
            time.sleep(1)
        else:
            print("\r" + " "*60, end="\r")
        # program
        try:
            for i in range(1, 11):
                self.adad = i
                self.adad2 = 11 * i
                self.step = i
                for i in range(self.adad, self.adad2, self.step):
                    print("%4i" % (i), end="")
                else:
                    print("")
            else:
                print("▬"*15)
        except:
            print("dont change anything please litteraly there is nothing to change :(\ngoing back to main menu :)")
            print("▬"*15)

    def Ex4(self):
        # decor
        print("▬"*15)
        for i in range(3, 0, -1):
            print(
                f"\rrunning 'Salary and avr salary (7)' program in → {i} ", end="")
            time.sleep(1)
        else:
            print("\r" + " "*60, end="\r")
        # program
        L1 = [1000000, 1100000, 600000, 1700000, 1500000, 1600000,
              700000, 800000, 900000, 1400000, 1300000, 1200000]
        self.Total = 0
        for i in L1:
            try:
                i = int(i)
            except:
                L1.remove(i)
                print(
                    f"corrupted target detected !  → {i} ← destroy it !\n"+"-"*15)
                continue
            self.Total += i
        self.avr = self.Total/12
        print("salary is:%12i" % (self.Total))
        print("avrage salary is:%14.2f" % (self.avr))
        print("▬"*15)

    def Ex5(self):
        # decor
        print("▬"*15)
        for i in range(3, 0, -1):
            print(f"\rrunning 'jenas galb (15)' program in → {i} ", end="")
            time.sleep(1)
        else:
            print("\r" + " "*60, end="\r")
        # program

        def jenas(t):
            for i in t:
                try:
                    if isinstance(i, int):
                        continue
                except:
                    pass
                tool = len(i)
                if i == i[-1:-(tool+1):-1]:
                    print(i, end=" - ")
        t = ("salas", "pop", "raar", "ssaa", 2, "234", "Sdfgt")  # vorodi ha
        jenas(t)
        print("\n" + "▬"*15)

    def Ex6(self):
        # decor
        print("▬"*15)
        for i in range(3, 0, -1):
            print(f"\rrunning 'Upside down ! (19)' program in → {i} ", end="")
            time.sleep(1)
        else:
            print("\r" + " "*60, end="\r")
        self.reshte = "SaLaM ChEtOrY ChEkHaBaR"

        def updw(reshte):
            print(f"({self.reshte}) changed to ↓↓ ")
            if isinstance(self.reshte, int):
                print("sharmande adad nmishe bdi :)")
                self.reshte = ""
            for i in self.reshte:
                if ord(i) >= 65 and ord(i) <= 90:
                    print(chr(ord(i) + 32), end="")
                elif ord(i) >= 97 and ord(i) <= 122:
                    print(chr(ord(i) - 32), end="")
                elif i == " ":
                    print(" ", end="")
                else:
                    print("reshte adadi dadi na ? hesab nist ! ", end="\r")
        updw(self.reshte)
        print("\n" + "▬"*15)

    def Ex7(self):
        # decor
        print("▬"*15)
        for i in range(3, 0, -1):
            print(f"\rrunning '|Abs| (25)' program in → {i} ", end="")
            time.sleep(1)
        else:
            print("\r" + " "*60, end="\r")
        # program
        self.L1 = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]
        for i in self.L1:
            try:
                if isinstance(i, str):
                    self.L1.remove(i)
                    print(f"Danger !!! infected Target →{i}← Destroyed :)")
            except:
                pass
        print(list(filter(lambda x: x > 0, self.L1)))
        print("▬"*15)

    def Ex8(self):
        # decor
        print("▬"*15)
        for i in range(3, 0, -1):
            print(
                f"\rrunning 'Name into ascii code (28)' program in → {i} ", end="")
            time.sleep(1)
        else:
            print("\r" + " "*60, end="\r")
        # program

        def codeSaz():
            self.z = 0
            while True:
                self.vorodi = input("gimme ur full name : ")
                if self.vorodi.lower() == "end":
                    global Loop
                    Loop = 0
                    print("► Bye ◄")
                    break
                try:
                    self.vorodi = int(self.vorodi)
                    if isinstance(self.vorodi, int):
                        print("you should Enter your name not numbers !!!")
                except:
                    break
            if Loop != 0:
                for i in self.vorodi:
                    self.z += 1
                    if ord(i) >= 65 and ord(i) <= 90:
                        print(ord(i), end="")
                    elif ord(i) >= 97 and ord(i) <= 122:
                        print(ord(i), end="")
                    else:
                        print(i, end="")
                    if self.z != len(self.vorodi):
                        print("_", end="")
        codeSaz()
        if Loop != 0:
            print("\n" + "▬"*15)

    def Ex9(self):
        # decor
        print("▬"*15)
        for i in range(10, 0, -1):
            print(
                f"\rrunning 'creat irancell numbers file (31)' program in → {i} \n you have time to use ctr+C ! This is a heavy file!", end="")
            time.sleep(1)
        else:
            print("\r" + " "*60, end="\r")
        # program
        with open("0936.txt", "w") as F:
            self.B = 1000000
            for i in range(8999999):
                self.B += 1
                F.write("0936")
                F.write(f"{self.B}\n")
        print("file created ! →0936.txt← 2pish shomare dige ro nnvshtm fgt copy paste va avz krdn 1 adde \n" + "▬"*15)

    def Ex10(self):
        # decor
        print("▬"*15)
        for i in range(3, 0, -1):
            print(
                f"\rrunning 'conver asci code to chr and vice versa! (17)' program in → {i} ", end="")
            time.sleep(1)
        else:
            print("\r" + " "*90, end="\r")
        # program

        def tabdil(A, B):  # A ord migire chr mide  / B chr migire ord mide
            # Estefade as metod →→ SPLIT ←← dar in masale mojaz →hast← !!! (17)
            L = A.split(" ")
            for i in L:
                try:
                    i = int(i)
                    print(chr(i), end=" ")
                except:
                    print(
                        f" → → {i}  ← ← please don't change number to str :) ", end=" ")
            else:
                print("")
            try:
                for i in B:
                    print(ord(i), end=" ")
            except:
                print("please don't change str to Number :)")
        tabdil(A="65 66 67", B="xyz")  # changeable stuff for Error handeling
        print("\n" + "▬"*15)


print("-"*60)
print("don't forget to reset program after each change Thanks :)")
print("-"*60)
while Loop:  # Loop menu and End
    C = final()
    if C.MenuNum == 1:
        C.Ex1()
    elif C.MenuNum == 2:
        C.Ex2()
    elif C.MenuNum == 3:
        C.Ex3()
    elif C.MenuNum == 4:
        C.Ex4()
    elif C.MenuNum == 5:
        C.Ex5()
    elif C.MenuNum == 6:
        C.Ex6()
    elif C.MenuNum == 7:
        C.Ex7()
    elif C.MenuNum == 8:
        C.Ex8()
    elif C.MenuNum == 9:
        C.Ex9()
    elif C.MenuNum == 10:
        C.Ex10()
    else:
        break
# ba vared krdn "End"(.lower) Loop init class break va be loop bala ↑ moraje va vared else mishvd dar geyr in sorat barname mored nzr ejra mishvd
