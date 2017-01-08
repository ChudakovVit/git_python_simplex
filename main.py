import sys
from scipy.optimize import linprog
from PyQt5.QtWidgets import (QWidget, QPushButton, QInputDialog, QApplication, QTextBrowser)

class Simplex(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.objectiveBtn()
        self.constrainsBtn()
        self.solveBtn()

        self.resize(480, 300)
        self.setWindowTitle('Simplex solver')
        self.show()

    def objectiveBtn(self):
        self.objective_btn = QPushButton('Objective function', self)
        self.objective_btn.move(20, 20)
        self.objective_btn.clicked.connect(self.objectiveDialog)
        self.objective_line = QTextBrowser(self)
        self.objective_line.setGeometry(250, 28, 250, 28)
        self.objective_line.move(200, 20)

    def constrainsBtn(self):
        self.constrains_btn = QPushButton('Constrains', self)
        self.constrains_btn.move(20, 60)
        self.constrains_btn.clicked.connect(self.constrainsDialog)
        self.constrains_line = QTextBrowser(self)
        self.constrains_line.setGeometry(250, 28, 250, 28)
        self.constrains_line.move(200, 60)

    def objectiveDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter objective function:')
        if ok:
            self.objective_line.setText(str(text))
            global objective_function
            objective_function = [int(elem) for elem in text.split(',')]

    def constrainsDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter constrains:')
        if ok:
            self.constrains_line.setText(str(text))
            global constrains
            constrains = [[int(el) for el in elem.split(',')] for elem in text.split(';')]

    def solveBtn(self):
        self.solve_btn = QPushButton('Solve', self)
        self.solve_btn.move(20, 100)
        self.solve_btn.clicked.connect(self.solveProblem)

        """test textBox"""
        self.solve_line = QTextBrowser(self)
        self.solve_line.setGeometry(250, 28, 250, 28)
        self.solve_line.move(200, 100)

    def solveProblem(self):
        print("ob_f ", objective_function)
        print("cons ", constrains)
        c = [-2, -1, -3, -1]
        A = [[1, 2, 5, -1], [1, -1, -1, 2]]
        b = [4, 1]
        x0_bnds = (None, None)
        x1_bnds = (None, None)
        x2_bnds = (None, None)
        x3_bnds = (None, None)
        res = linprog(objective_function, constrains, b, bounds=(x0_bnds, x1_bnds, x2_bnds, x3_bnds))
        print("res ", res)
        self.solve_line.setText(str(res.fun))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    simplex = Simplex()
    sys.exit(app.exec_())