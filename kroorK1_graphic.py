import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel,
                             QGridLayout, QInputDialog, QApplication,
                             QHBoxLayout)
from PyQt5.QtGui import QPainter, QColor

from parserfail import CrossParser
import logic

main_window = None
choose_size_dialog = None


class CellWidget(QWidget):
    def __init__(self, letter=None):
        super().__init__()
        self.__letter = letter

        if self.__letter != "_":
            layout = QHBoxLayout()
            layout.addWidget(QLabel(letter), alignment=Qt.AlignCenter)
            self.setLayout(layout)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.fill_rectangles(qp)
        qp.end()

    def fill_rectangles(self, qp):
        if self.__letter == "_":
            qp.fillRect(0, 0, super().width(), super().height(),
                        QColor(0, 0, 0))
        else:
            qp.drawRect(QRect(0, 0, self.width(), self.height()))


class MainWindow(QWidget):
    def __init__(self, matrix):
        super().__init__()
        self.initUI(matrix)

    def initUI(self, matrix):
        grid_layout = QGridLayout()

        width = len(matrix)
        if width > 0:
            height = len(matrix[0])

            for x in range(width):
                for y in range(height):
                    grid_layout.addWidget(CellWidget(matrix[x][y]), x, y)

        self.setLayout(grid_layout)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.geo_name = ''
        self.wr_name = ''

    def initUI(self):
        self.btn = QPushButton('Maybe u wanna Crossword?\n Click here!', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.get_inform)

        self.le = QLineEdit(self)
        self.le.move(20, 60)

        self.lin = QLineEdit(self)
        self.lin.move(20, 85)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Crossword Solver')

        self.btn_next = QPushButton('Lets do it!', self)
        self.btn_next.move(200, 110)
        self.btn_next.clicked.connect(start)

        self.show()

    def get_inform(self):
        text_double, ok = QInputDialog.getText(self, "Just another title", 'Please, enter GEOMETRY[space]TEXT: ')

        if ok:
            self.geo_name = str(text_double).split()[0]
            self.wr_name = str(text_double).split()[1]
            self.le.setText(str(self.geo_name))
            self.lin.setText(str(self.wr_name))



def start():
    global main_window
    geometry_file = ex.geo_name
    words_file = ex.wr_name
    parser = CrossParser()
    parser.know_geometry(geometry_file)
    parser.know_words(words_file)
    horizontal_dictionary = parser.words_place_hor()
    vertical_dictionary = parser.words_place_vert()
    parser.form_word_place(vertical_dictionary, horizontal_dictionary)
    parser.new_view()

    logicall = logic.Logic(parser)
    matrix = logicall.fill()
    # matrix = [['m', '_', 's'], ['o', '_', 'i'], ['r', '_', 's'],
    #           ['e', '_', 'k'], ['_', '_', 'a']]
    # print(matrix)
    choose_size_dialog.close()
    main_window = MainWindow(matrix)
    main_window.show()


if __name__ == '__main__':
    application = QApplication(sys.argv)

    choose_size_dialog = QtWidgets.QDialog()
    layout = QtWidgets.QVBoxLayout()
    ex = Example()

    sys.exit(application.exec_())





'''import time
import sys
import argparse
from parserfail import CrossParser
import logic
from PyQt5.QtWidgets import (QWidget, QLineEdit, QApplication, QVBoxLayout,
                             QPushButton, QLabel, QGridLayout, QInputDialog)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Maybe u wanna Crossword?', self)
        self.btn.move(80, 50)
        self.btn.clicked.connect(self.makeCross)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Crossword Solver')
        self.show()

    def makeCross(self):
        txt, ok = QInputDialog.getText(self, "Just another title",
                                        'Please, enter GEOMETRY.txt[space]TEXT.txt: ')

        if ok:
        '''








'''letters = []

def my_func():
    geo_f = line_edit1.text()
    words_f = line_edit2.text()
    parser2 = CrossParser()
    parser2.know_geometry(geo_f)
    parser2.know_words(words_f)
    dictionary_hor = parser2.words_place_hor()
    dictionary_vert = parser2.words_place_vert()
    parser2.form_word_place(dictionary_vert, dictionary_hor)
    parser2.new_view()

    logicall = logic.Logic(parser2)
    mat = logicall.fill()

    if mat == 0:
        print("not solvable")
    else:
        for line in mat:
            print("".join(line))
    window.close()


    for line in mat:
        for letter in line:
            global letters
            letters.append(letter)

    ex = Example()


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('Crossword!', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
        #################

        grid = QGridLayout()
        self.setLayout(grid)

        positions = [(i,j) for i in range(4) for j in range(5)]

        for position, name in zip(positions, letters):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.show()
        time.sleep(1)


app = QApplication(sys.argv)
window = QWidget()
window.setLayout(QVBoxLayout())
line_edit1 = QLineEdit()
txt1 = QLabel('[geometry_name.txt]')
# lbl1.move(15, 10)
line_edit2 = QLineEdit()
txt2 = QLabel("[words_name.txt]")
window.layout().addWidget(line_edit1)
window.layout().addWidget(txt1)
window.layout().addWidget(line_edit2)
window.layout().addWidget(txt2)
button = QPushButton('Вывести текст')
# button.clicked.connect(lambda: print(line_edit1.text()))
window.layout().addWidget(button)
window.show()
button.clicked.connect(my_func)
a = ""
button.clicked = my_func
sys.exit(app.exec_())



def main():
    if sys.argv[1] == '--help':
        funk_help()
    else:
        parser2 = CrossParser()
        parser2.know_geometry(sys.argv[1])
        parser2.know_words(sys.argv[2])
        dictionary_hor = parser2.words_place_hor()
        dictionary_vert = parser2.words_place_vert()
        parser2.form_word_place(dictionary_vert, dictionary_hor)
        parser2.new_view()

    logicall = logic.Logic(parser2)
    mat = logicall.fill()

    if mat == 0:
        print("not solvable")
    else:
        for line in mat:
            print("".join(line))

    with open('ans.txt', 'w') as f:
        for line in mat:
            f.write(''.join(line)+'/n')

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		names = []
		grid = QGridLayout()
		self.setLayout(grid)

		logicall = logic.Logic(parser2)
		mat = logicall.fill()
		if mat == 0:
			print("not solvable")
		else:
			for line in mat:
				names.append(line)
				print("".join(line))

		positions = [(i, j) for i in range(2) for j in range(10)]

		for position, name in zip(positions, names):
			if name == '':
				continue
			button = QPushButton(name)
			grid.addWidget(button, *position)

		self.move(300, 150)
		self.setWindowTitle('Greed')
		self.show()





if __name__ == "__main__":
	main()
	
	   app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())'''
