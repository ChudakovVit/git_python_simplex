import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QInputDialog, QApplication, QTextBrowser)

objective_function = ""
constrains = ""

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
            objective_function = str(text)

    def constrainsDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter constrains:')
        if ok:
            self.constrains_line.setText(str(text))
            global constrains
            constrains = str(text)

    def solveBtn(self):
        self.solve_btn = QPushButton('Solve', self)
        self.solve_btn.move(20, 100)
        self.solve_btn.clicked.connect(self.solveProblem)

        """test textBox"""
        self.solve_line = QTextBrowser(self)
        self.solve_line.setGeometry(250, 28, 250, 28)
        self.solve_line.move(200, 100)

    def solveProblem(self):
        self.solve_line.setText(objective_function + " " + constrains)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    simplex = Simplex()
    sys.exit(app.exec_())