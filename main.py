import sys
from scipy.optimize import linprog
from PyQt5.QtWidgets import *


objective_function = [-1, 10, -1]
constraints = [[1, -5.5, -7], [1, 14.5, 7]]
constraints_equal = [-13, 15]

# objective_function = [-1, -2, -3, 4]
# constraints = [[1, 1, -1, 1], [1, 14, 10, -10]]
# constraints_equal = [2, 24]

# objective_function = [-1, 4, -3, -10]
# constraints = [[1, 1, -1, 1], [1, 14, 10, -10]]
# constraints_equal = [0, 11]
#
# objective_function = [-1, 5, 1, -1]
# constraints = [[1, 3, 3, 1], [2, 0, 3, -1]]
# constraints_equal = [3, 4]
#
# objective_function = [-1, -10, 1, -5]
# constraints = [[1, 2, -1, -1], [-1, 2, 3, 1], [1, 5, 1, -1]]
# constraints_equal = [1, 2, 5]
# #
# objective_function = [-1, -1, -1, -1]
# constraints = [[4, 2, 5, -1], [5, 3, 6, -2], [3, 2, 4, -1]]
# constraints_equal = [5, 5, 4]

# objective_function = [-1, -1, 1, -1, 2]
# constraints = [[8, 1, 1, 1, -2], [6, 1, 2, 3, -4], [10, 1, 3, 6, -7]]
# constraints_equal = [10, 20, 30]

# objective_function = [-1, -2, -1, 2, -1, 2]
# constraints = [[1, -1, 1, -1, 1, -1], [2, 3, -2, -3, 2, 3], [3, 2, -1, -4, 3, 2, 10]]
# constraints_equal = [7, 0, 10]

# objective_function = [-2,-3,-4]
# constraints = [[3,2,1],[2,5,3]]
# constraints_equal = [10,15]





class Simplex(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.objectiveBtn()
        self.constraintsBtn()
        self.constraintsEqualBtn()
        self.solveBtn()
        self.helpBtn()
        # self.showFullScreen()
        # self.setFixedSize(self.size())
        self.setWindowTitle('Optimization problem')
        self.show()

    def objectiveBtn(self):
        self.objective_btn = QPushButton('Objective function', self)
        self.objective_btn.setToolTip("Press to enter the objective function coefficients")
        self.objective_btn.move(20, 20)
        self.objective_btn.clicked.connect(self.objectiveDialog)
        self.objective_line = QTextBrowser(self)
        self.objective_line.setGeometry(500, 28, 500, 28)
        self.objective_line.move(200, 20)

    def constraintsBtn(self):
        self.constraints_btn = QPushButton('Constrains', self)
        self.constraints_btn.setToolTip("Press to enter the constrains coefficients")
        self.constraints_btn.move(20, 60)
        self.constraints_btn.clicked.connect(self.constraintsDialog)
        self.constraints_line = QTextBrowser(self)
        self.constraints_line.setGeometry(500, 28, 500, 28)
        self.constraints_line.move(200, 60)

    def constraintsEqualBtn(self):
        self.constraints_equal_btn = QPushButton('Constrains equal', self)
        self.constraints_equal_btn.setToolTip("Press to enter the constrains equal coefficients")
        self.constraints_equal_btn.move(20, 100)
        self.constraints_equal_btn.clicked.connect(self.constraintsEqualDialog)
        self.constraints_equal_line = QTextBrowser(self)
        self.constraints_equal_line.setGeometry(500, 28, 500, 28)
        self.constraints_equal_line.move(200, 100)

    def solveBtn(self):
        self.solve_btn = QPushButton('Solve', self)
        self.solve_btn.setToolTip("Press to solve optimization problem")
        self.solve_btn.move(20, 140)
        self.solve_btn.clicked.connect(self.solveProblem)
        self.solve_line = QTextBrowser(self)
        self.solve_line.setGeometry(500, 140, 500, 140)
        self.solve_line.move(200, 140)

    def helpBtn(self):
        self.help_btn = QPushButton('Help', self)
        self.help_btn.setToolTip("Press to open help of the program")
        self.help_btn.move(20, 180)
        self.help_btn.clicked.connect(self.helpDialog)

    def objectiveDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter objective function:')
        if ok and self.checkSimpleList(str(text)):
            global objective_function
            objective_function = [float(elem) for elem in text.split(',')]
            # text = ''
            # for i in range(len(objective_function)):
            #     text += '{:+g}*x_{}'.format(objective_function[i], i)
            # text += ' -> min'
            self.objective_line.setText(str(text))

    def constraintsDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter constrains:')
        if ok and self.checkList(str(text)):
            global constraints
            constraints = [[float(el) for el in elem.split(',')] for elem in text.split(';')]
            self.constraints_line.setText(str(text))

    def constraintsEqualDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter constrains equals:')
        if ok and self.checkSimpleList(str(text)):
            global constraints_equal
            constraints_equal = [float(elem) for elem in text.split(',')]
            self.constraints_equal_line.setText(str(text))

    def helpDialog(self):
        QMessageBox.information(self, "Optimization problem",
                                "Read more information on https://en.wikipedia.org/wiki/Optimization_problem")

    def solveProblem(self):
        try:
            res = linprog(objective_function, constraints, constraints_equal)
            message = res.message
            if res.status == 0:
                message += "\nOptimum value for the objective function is {}".format(res.fun)
                message += '\nThe point at which the value has its minimum is {}'.format(tuple(res.x))
                print(res)
        except Exception:
            message = 'The system of conditions contradictory objectives'
        self.solve_line.setText(str(message))

    def checkSimpleList(self, text):
        try:
            temp = [float(elem) for elem in text.split(',')]
        except Exception:
            return False
        return True

    def checkList(self, text):
        try:
            temp = [[float(el) for el in elem.split(',')] for elem in text.split(';')]
        except Exception:
            return False
        return True

def main():
    app = QApplication(sys.argv)
    simplex = Simplex()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()