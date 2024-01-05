from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os

os.system("cls")


class Calculator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowIcon(QIcon("C:\\Users\\USER\\Downloads\\475497.ico"))
        self.setWindowTitle("Calculator")
        self.setMinimumSize(335, 600)
        self.setMaximumSize(335, 600)
        self.setFont(QFont("Calibri", 22))

        self.setStyleSheet("background-color: black;")

        # buttonlarni ko'rinishini sozlamalari
        first_row_3_button = """
            font-family: Arial; 
            font-weight: bold;
            color: black; 
            background-color: #D4D4D2;
            border-radius : 35px; 
            font-size: 25px
            """

        number_settings = """
            font-family: Arial; 
            font-weight: bold;
            color: white; 
            background-color: #303030;
            border-radius : 35px; 
            font-size: 30px
            """

        button_settings = """
            font-family: Arial; 
            font-weight: bold;
            color: white; 
            background-color: #FF9500;
            border-radius : 35px; 
            font-size: 40px
            """

        # asosiy sonlarni kiritiladigan konsole
        self.label = QLabel(self)
        self.label.setGeometry(0, 60, 320, 70)
        self.label.setWordWrap(True)
        self.label.setStyleSheet(
            """
            font-size: 60px;
            color: white; 
            border : 4px white; 
            background : black;
            """
        )
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont("Arial", 15))
        self.label.setText("0")

        # kichina natija uchun
        self.little_result = QLabel(self)
        self.little_result.setGeometry(-5, 140, 320, 70)
        self.little_result.setWordWrap(True)
        self.little_result.setStyleSheet(
            """
            font-size: 30px;
            color: white; 
            border : 4px white; 
            background : black;
            """
        )

        self.little_result.setAlignment(Qt.AlignRight)
        self.little_result.setFont(QFont("Arial", 15))
        self.little_result.setText("0")

        # <------------------------------------- BIRINCHI TUGMALAR QATORI ------------------------------------->

        # button AC
        self.btn_AC = QPushButton(self)
        self.btn_AC.setGeometry(20, 190, 70, 70)
        self.btn_AC.setText("AC")
        self.btn_AC.setStyleSheet(first_row_3_button)

        # button +/-
        self.btn_plus_minus = QPushButton(self)
        self.btn_plus_minus.setGeometry(98, 190, 70, 70)
        self.btn_plus_minus.setText("+/-")
        self.btn_plus_minus.setStyleSheet(first_row_3_button)

        # button '%'
        self.btn_percent = QPushButton(self)
        self.btn_percent.setGeometry(177, 190, 70, 70)
        self.btn_percent.setText("%")
        self.btn_percent.setStyleSheet(first_row_3_button)

        # button ÷
        self.btn_division = QPushButton(self)
        self.btn_division.setGeometry(255, 190, 70, 70)
        self.btn_division.setText("÷")
        self.btn_division.setStyleSheet(button_settings)

        # <------------------------------------- IKKINCHI TUGMALAR QATORI ------------------------------------->

        # button 7
        self.num_btn_7 = QPushButton(self)
        self.num_btn_7.setGeometry(20, 270, 70, 70)
        self.num_btn_7.setText("7")
        self.num_btn_7.setStyleSheet(number_settings)

        # button 8
        self.num_btn_8 = QPushButton(self)
        self.num_btn_8.setGeometry(98, 270, 70, 70)
        self.num_btn_8.setText("8")
        self.num_btn_8.setStyleSheet(number_settings)

        # button 9
        self.num_btn_9 = QPushButton(self)
        self.num_btn_9.setGeometry(177, 270, 70, 70)
        self.num_btn_9.setText("9")
        self.num_btn_9.setStyleSheet(number_settings)

        # button '×'
        self.btn_multiply = QPushButton(self)
        self.btn_multiply.setGeometry(255, 270, 70, 70)
        self.btn_multiply.setText("×")
        self.btn_multiply.setStyleSheet(button_settings)

        # <------------------------------------- UCHINCHI TUGMALAR QATORI ------------------------------------->

        # button 4
        self.num_btn_4 = QPushButton(self)
        self.num_btn_4.setGeometry(20, 350, 70, 70)
        self.num_btn_4.setText("4")
        self.num_btn_4.setStyleSheet(number_settings)

        # button 5
        self.num_btn_5 = QPushButton(self)
        self.num_btn_5.setGeometry(98, 350, 70, 70)
        self.num_btn_5.setText("5")
        self.num_btn_5.setStyleSheet(number_settings)

        # button 6
        self.num_btn_6 = QPushButton(self)
        self.num_btn_6.setGeometry(177, 350, 70, 70)
        self.num_btn_6.setText("6")
        self.num_btn_6.setStyleSheet(number_settings)

        # button '-'
        self.btn_minus = QPushButton(self)
        self.btn_minus.setGeometry(255, 350, 70, 70)
        self.btn_minus.setText("-")
        self.btn_minus.setStyleSheet(button_settings)

        # <------------------------------------- TO'RTINCHI TUGMALAR QATORI ------------------------------------->

        # button bir
        self.num_btn_1 = QPushButton(self)
        self.num_btn_1.setGeometry(20, 430, 70, 70)
        self.num_btn_1.setText("1")
        self.num_btn_1.setStyleSheet(number_settings)

        # button ikki
        self.num_btn_2 = QPushButton(self)
        self.num_btn_2.setGeometry(98, 430, 70, 70)
        self.num_btn_2.setText("2")
        self.num_btn_2.setStyleSheet(number_settings)

        # button uch
        self.num_btn_3 = QPushButton(self)
        self.num_btn_3.setGeometry(177, 430, 70, 70)
        self.num_btn_3.setText("3")
        self.num_btn_3.setStyleSheet(number_settings)

        # button '+'
        self.btn_plus = QPushButton(self)
        self.btn_plus.setGeometry(255, 430, 70, 70)
        self.btn_plus.setText("+")
        self.btn_plus.setStyleSheet(button_settings)

        # <------------------------------------- BESHINCHI TUGMALAR QATORI ------------------------------------->

        # button 0
        self.num_btn_0 = QPushButton(self)
        self.num_btn_0.setGeometry(20, 510, 150, 70)
        self.num_btn_0.setText("0")
        self.num_btn_0.setStyleSheet(number_settings)

        # button ','
        self.btn_comma = QPushButton(self)
        self.btn_comma.setGeometry(180, 510, 70, 70)
        self.btn_comma.setText(",")
        self.btn_comma.setStyleSheet(number_settings)

        # button '='
        self.btn_equal = QPushButton(self)
        self.btn_equal.setGeometry(257, 510, 70, 70)
        self.btn_equal.setText("=")
        self.btn_equal.setStyleSheet(button_settings)

        # <------------------------------------------- CLICK BUTTONS ------------------------------------------->

        # numbers
        self.num_btn_0.clicked.connect(lambda: self.action("0"))
        self.num_btn_1.clicked.connect(lambda: self.action("1"))
        self.num_btn_2.clicked.connect(lambda: self.action("2"))
        self.num_btn_3.clicked.connect(lambda: self.action("3"))
        self.num_btn_4.clicked.connect(lambda: self.action("4"))
        self.num_btn_5.clicked.connect(lambda: self.action("5"))
        self.num_btn_6.clicked.connect(lambda: self.action("6"))
        self.num_btn_7.clicked.connect(lambda: self.action("7"))
        self.num_btn_8.clicked.connect(lambda: self.action("8"))
        self.num_btn_9.clicked.connect(lambda: self.action("9"))

        # operations
        self.btn_plus.clicked.connect(self.action_plus)
        self.btn_minus.clicked.connect(self.action_minus)
        self.btn_multiply.clicked.connect(self.action_multiply)
        self.btn_division.clicked.connect(self.action_division)
        self.btn_equal.clicked.connect(self.action_equal)
        self.btn_percent.clicked.connect(self.action_percent)
        self.btn_comma.clicked.connect(self.action_comma)
        self.btn_plus_minus.clicked.connect(self.action_plus_minus)
        self.btn_AC.clicked.connect(self.action_AC)

    # kichkina label uchun, natija
    def little_label_calculation(self):
        equation = self.label.text()
        box = ""

        for i in range(len(equation)):
            if equation[i] == "÷":
                box += "/"
            elif equation[i] == "×":
                box += "*"
            elif equation[i] == ",":
                box += "."
            else:
                box += equation[i]
        print(box)
        try:
            ans = eval(box)
            self.little_result.setText(str(ans))

        except ZeroDivisionError:
            self.little_result.setText("Can't divide by zero")
        except:
            print("Error in method 'action'")

    # sonlarni tekshirib qo'shib ketish
    def action(self, num):
        if self.check():
            self.add_num(num)
            self.little_label_calculation()

    # sonni qo'shib ketish uchun method
    def add_num(self, num):
        if self.label.text() == "0":
            text = ""
            self.label.setText(text + num)
        else:
            text = self.label.text()
            self.label.setText(text + num)

    # 8 ta dan ortiq son kiritlmaslik uchun method
    def check(self):
        text = self.label.text()
        if len(text) > 8:
            return False
        return True

    # amallarni tekshirish
    def check_op(self, op):
        operations = ["÷", "×", "+", "%", ",", "-"]
        text = self.label.text()
        if text[-1] != op:
            if text[-1] in operations:
                self.label.setText(text[:-1] + op)
            else:
                self.label.setText(text + op)

    # amallarni yozish uchun methodlar
    def action_plus(self):
        self.check_op("+")

    def action_minus(self):
        self.check_op("-")

    def action_multiply(self):
        self.check_op("×")

    def action_division(self):
        self.check_op("÷")

    def action_comma(self):
        self.check_op(",")

    def action_percent(self):
        self.check_op("%")

    # manfiy sonni musbat qilish | musbat sonni manfiy qilish
    def action_plus_minus(self):
        text = self.label.text()
        op = ["÷", "×", "+", "/", "*"]
        box = 0
        for i in range(len(text) - 1, 0, -1):
            if text[i] in op:
                box = i
                break
        # birinchi kiritilgan sonni o'zgartirish
        try:
            if int(text) < 0:
                text = abs(int(text))
                self.label.setText(str(text))
            elif int(text) > 0:
                text = -1 * int(text)
                self.label.setText(str(text))
        # oxirgi kiritilgan sonni o'zgartirish
        except:
            try:
                if int(text[box + 1 :]) > 0:
                    text = text[: box + 1] + "-" + text[box + 1 :]
                    self.label.setText(str(text))
                else:
                    text = text[: box + 1] + text[box + 1 :]
                    self.label.setText(str(text))
                self.little_label_calculation()

            except:
                print("Error in method 'action_plus_minus'")

    def action_AC(self):
        self.label.setText("0")
        self.little_result.setText("0")

    # natijani ekranga chiqarish
    def action_equal(self):
        equation = self.label.text()
        box = ""

        # amallarni eval chunadiagn qilib o'zgartirish
        for i in range(len(equation)):
            if equation[i] == "÷":
                box += "/"
            elif equation[i] == "×":
                box += "*"
            elif equation[i] == ",":
                box += "."
            else:
                box += equation[i]
        try:
            ans = eval(box)
            self.label.setText(str(ans))
            self.little_result.setText("")
        except ZeroDivisionError:
            self.label.setText("0")
            self.little_result.setText("Can't divide by zero")
        except:
            print("Error in method 'action equal'")


# instance olish
app = QApplication([])
program = Calculator()
program.show()
sys.exit(app.exec_())
