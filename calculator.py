from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDesktopWidget
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        center_point = QDesktopWidget().availableGeometry().center()
        x_spot = center_point.x() - (410 / 2)
        y_spot = center_point.y() - (800 / 2)
        self.setWindowTitle("Calculator")
        self.setGeometry(int(x_spot), int(y_spot), 410, 805)    
        self.ui()
        self.show()

    def ui(self):

        # label
        self.label_1 = QLabel(self)
        self.label_1.setGeometry(5, 5, 400, 195)
        self.label_1.setStyleSheet("QLabel"
                                   "{"
                                   "border: 1px solid black;"
                                   "background: white;"
                                   "}")
        self.label_1.setAlignment(Qt.AlignRight)
        self.label_1.setFont(QFont('Arial', 15))
        self.label_1.setWordWrap(True)
        
        #buttons
        p1 = QPushButton("1", self)
        p2 = QPushButton("2", self)
        p3 = QPushButton("3", self)
        p4 = QPushButton("4", self)
        p5 = QPushButton("5", self)
        p6 = QPushButton("6", self)
        p7 = QPushButton("7", self)
        p8 = QPushButton("8", self)
        p9 = QPushButton("9", self)
        p0 = QPushButton("0", self)

        pplus = QPushButton("+", self)
        pminus = QPushButton("-", self)
        pmultiply = QPushButton("*", self)
        pdivide = QPushButton("/", self)


        p_parenthese_open = QPushButton("(", self)
        p_parenthese_close = QPushButton(")", self)
        pdote = QPushButton(".", self)
        pequal = QPushButton("=", self)
        pclear = QPushButton("AC", self)
        pdel = QPushButton("BACK", self)

        # button's location 
        pclear.setGeometry(5, 200, 100, 100)
        pdel.setGeometry(105, 200, 100, 100)
        p_parenthese_open.setGeometry(205, 200, 100, 100)
        p_parenthese_close.setGeometry(305, 200, 100, 100)

        p1.setGeometry(5, 300, 100, 100)
        p2.setGeometry(105, 300, 100, 100)
        p3.setGeometry(205, 300, 100, 100)
        pminus.setGeometry(305, 300, 100, 100)
        
        p4.setGeometry(5, 400, 100, 100)
        p5.setGeometry(105, 400, 100, 100)
        p6.setGeometry(205, 400, 100, 100)
        pmultiply.setGeometry(305, 400, 100, 100)
        
        p7.setGeometry(5, 500, 100, 100)
        p8.setGeometry(105, 500, 100, 100)
        p9.setGeometry(205, 500, 100, 100)
        pdivide.setGeometry(305, 500, 100, 100)
        
        p0.setGeometry(5, 600, 200, 100)
        pdote.setGeometry(205, 600, 100, 100)
        pplus.setGeometry(305, 600, 100, 100)
        
        pequal.setGeometry(5, 700, 400, 100)

        # button functions     
        p1.clicked.connect(self.num1)
        p2.clicked.connect(self.num2)
        p3.clicked.connect(self.num3)
        p4.clicked.connect(self.num4)
        p5.clicked.connect(self.num5)
        p6.clicked.connect(self.num6)
        p7.clicked.connect(self.num7)
        p8.clicked.connect(self.num8)
        p9.clicked.connect(self.num9)
        p0.clicked.connect(self.num0)

        pplus.clicked.connect(self.opplus)
        pminus.clicked.connect(self.opminus)
        pmultiply.clicked.connect(self.opmultiply)
        pdivide.clicked.connect(self.opdivide)

        p_parenthese_open.clicked.connect(self.parenthese_open)
        p_parenthese_close.clicked.connect(self.parenthese_close)
        pdote.clicked.connect(self.stdote)
        pequal.clicked.connect(self.opequal)
        pclear.clicked.connect(self.opclear)
        pdel.clicked.connect(self.opdel)

    # functions
    def num1(self):
        text = self.label_1.text()
        self.label_1.setText(text + "1")
    
    def num2(self):
        text = self.label_1.text()
        self.label_1.setText(text + "2")
    
    def num3(self):
        text = self.label_1.text()
        self.label_1.setText(text + "3")

    def num4(self):
        text = self.label_1.text()
        self.label_1.setText(text + "4")

    def num5(self):
        text = self.label_1.text()
        self.label_1.setText(text + "5")

    def num6(self):
        text = self.label_1.text()
        self.label_1.setText(text + "6")

    def num7(self):
        text = self.label_1.text()
        self.label_1.setText(text + "7")

    def num8(self):
        text = self.label_1.text()
        self.label_1.setText(text + "8")

    def num9(self):
        text = self.label_1.text()
        self.label_1.setText(text + "9")

    def num0(self):
        text = self.label_1.text()
        self.label_1.setText(text, "0")

    def opplus(self):
        text = self.label_1.text()
        self.label_1.setText(text + "+")

    def opminus(self):
        text = self.label_1.text()
        self.label_1.setText(text + "-")

    def opmultiply(self):
        text = self.label_1.text()
        self.label_1.setText(text + "*")

    def opdivide(self):
        text = self.label_1.text()
        self.label_1.setText(text + "/")

    def parenthese_open(self):
        text = self.label_1.text()
        self.label_1.setText(text + "(")

    def parenthese_close(self):
        text = self.label_1.text()
        self.label_1.setText(text + ")")

    def stdote(self):
        text = self.label_1.text()
        self.label_1.setText(text + ".")

    def opequal(self):
        text = self.label_1.text()
        ans = calculator(text)
        self.label_1.setText(str(int(ans)))

    def opclear(self):
        self.label_1.setText("")

    def opdel(self):
        text = self.label_1.text()
        self.label_1.setText(text[:len(text)-1])


def calculator(string):
    values = []
    ops = []
    i = 0
    while i < len(string):
        
        if string[i] == " ":
            i += 1
            continue
        
        elif string[i] == "(":
            ops.append(string[i])

        elif string[i].isdigit():
            val = ""
            while i < len(string) and string[i].isdigit():
                val += string[i]
                i += 1
            values.append(float(int(val)))
            i -= 1

        elif string[i] == ")":
            while len(ops) != 0 and ops[-1] != "(":
                num2 = values.pop()
                num1 = values.pop()
                operation = ops.pop()
                
                values.append(applyop(num1, num2, operation))

            ops.pop()
        
        else:
            while len(ops) != 0 and prec(ops[-1]) >= prec(string[i]):
                n2 = values.pop()
                n1 = values.pop()
                op = ops.pop()

                values.append(applyop(n1, n2, op))

            ops.append(string[i])
        i += 1
    

    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()

        values.append(applyop(val1, val2, op))
    
    return values[-1]


def prec(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    return 0


def applyop(n1, n2 , op):
    if op == "+": return n1 + n2
    if op == "-": return n1 - n2
    if op == "*": return n1 * n2
    if op == "/": return n1 / n2
                    

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

